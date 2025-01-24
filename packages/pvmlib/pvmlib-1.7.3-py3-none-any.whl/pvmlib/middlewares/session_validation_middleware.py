    
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from pvmlib.logs import LoggerSingleton
import requests
import json
import os

IGNORE_SESSION = os.getenv("IGNORE_SESSION", "False")
URL_ENDPOINTS_SERVICE = os.getenv("URL_ENDPOINT_SERVICES")

class SessionValidationMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.logger = LoggerSingleton().get_logger()
     
    async def dispatch(self, request: Request, call_next):
        if "healthcheck" in request.url.path:
            return await call_next(request)
        
        if IGNORE_SESSION == "True":
            return await call_next(request)
        
        path = '/puntodeventa/api/v1/verificar-token'
        url = f'{URL_ENDPOINTS_SERVICE}{path}'

        headers = {
            "Content-Type": "application/json",
            "Authorization": request.headers.get("Authorization"),
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        try:
            response = requests.post(url=url, headers=headers)
            response.raise_for_status()
            response_data = response.json()
            self.logger.info(f"Response from token verification: {response_data}")
            if response.status_code == 200:
                return await call_next(request)
            else:
                return JSONResponse(
                    status_code=401,
                    content=response_data
                )
        except requests.RequestException as e:
            self.logger.error(f"RequestException: {str(e)}")
            response_error = json.loads(e.response.text)
            return JSONResponse(
                status_code=401,
                content=response_error
            )