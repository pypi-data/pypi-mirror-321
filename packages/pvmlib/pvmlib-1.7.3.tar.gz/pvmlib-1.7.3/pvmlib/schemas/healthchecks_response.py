from pydantic import BaseModel, Field
from typing import Dict

class ReadinessResponse(BaseModel):
    status: str = Field(
        ...,
        title="Status",
        description="Status of the service"
    )
    code: int = Field(
        ...,
        title="Code",
        description="HTTP status code"
    )
    dependencies: Dict[str, str] = Field(
        ...,
        title="Dependencies",
        description="Status of the service dependencies"
    )

responses_readiness = {
    200: {
        "description": "Service is ready",
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/ReadinessResponse"
                },
                "example": {
                    "status": "ready",
                    "code": 200,
                    "dependencies": {
                        "mongodb": "ready",
                        "verificarToken": "ready"
                    }
                }
            }
        }
    },
    500: {
        "description": "Service is not ready",
        "content": {
            "application/json": {
                "example": {
                    "status": "not ready",
                    "code": 500,
                    "dependencies": {
                        "mongodb": "not ready",
                        "verificarToken": "not ready"
                    }
                }
            }
        }
    }
}

class LivenessResponse(BaseModel):
    status: str = Field(
        ...,
        title="Status",
        description="Status of the service"
    )
    code: int = Field(
        ...,
        title="Code",
        description="HTTP status code"
    )

responses_liveness = {
    200: {
        "description": "Service is alive",
        "content": {
            "application/json": {
                "schema": {
                    "$ref": "#/components/schemas/LivenessResponse"
                },
                "example": {
                    "status": "alive",
                    "code": 200
                }
            }
        }
    },
    500: {
        "description": "Service is not alive",
        "content": {
            "application/json": {
                "example": {
                    "status": "not alive",
                    "code": 500
                }
            }
        }
    }
}
