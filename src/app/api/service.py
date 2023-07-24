from fastapi import APIRouter

service_router = APIRouter()


@service_router.get("/health")
async def health():
    return


@service_router.get("/ping")
async def pong():
    return {"ping": "pong!"}
