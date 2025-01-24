from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import database_manager
from .logs import LoggerSingleton

logger = LoggerSingleton().get_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await database_manager.connect_to_mongo()
    except Exception as e:
        raise e

    yield
    await database_manager.disconnect_from_mongo()