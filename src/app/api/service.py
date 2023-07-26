from fastapi import APIRouter, Depends
from db.session import init_models, get_session
from db.models import User, UserRole
from sqlalchemy.ext.asyncio import AsyncSession

service_router = APIRouter()


@service_router.get("/health")
async def health():
    return


@service_router.get("/ping")
async def pong():
    return {"ping": "pong!"}


@service_router.post("/init-db")
async def init_db(db_session: AsyncSession = Depends(get_session)):
    await init_models()
    superadmin = User(first_name="superadmin", last_name="superadmin", email="superadmin@mail.com",
                      hashed_password="12345", roles=[role.value for role in UserRole])

    db_session.add(superadmin)
    await db_session.flush()
