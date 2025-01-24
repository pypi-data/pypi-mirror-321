from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from pvmlib.schemas.success_schema import ResponseGeneralSchema, ResponseMetaSchema
from pvmlib.code_diccionary import HTTP_STATUS_CODE
import json
from datetime import datetime
import uuid

class AddDataMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if "healthcheck" in request.url.path:
            return await call_next(request)
        
        start_time = datetime.now()
        
        response = await call_next(request)
        time_elapsed = (datetime.now() - start_time).total_seconds() * 1000
        response_body = [section async for section in response.__dict__['body_iterator']]
        response_body = json.loads(response_body[0].decode())
        
        status_message = HTTP_STATUS_CODE.get(response.status_code, "Unknown Status Code")

        new_response_body = ResponseGeneralSchema(
            type=response_body["type"] if "type" in response_body else 0,
            message=response_body["message"] if "message" in response_body else status_message,
            code=response_body["code"] if "code" in response_body else 0  ,
            data=response_body["data"] if "data" in response_body else response_body["error"],
            meta=ResponseMetaSchema(
                id_transaction=str(uuid.uuid4()),
                status=status_message,
                time_elapsed=time_elapsed
            )
        )

        return JSONResponse(content=new_response_body.model_dump(), status_code=response.status_code)