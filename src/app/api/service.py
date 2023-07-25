from fastapi import APIRouter
from db.session import init_models
from db.models import User

service_router = APIRouter()


@service_router.get("/health")
async def health():
    return


@service_router.get("/ping")
async def pong():
    return {"ping": "pong!"}


@service_router.get("/init-db")
async def init_db():
    await init_models()
