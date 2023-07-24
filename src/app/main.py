from fastapi import FastAPI
import uvicorn
from settings import settings
from api.service import service_router

app = FastAPI()

app.include_router(service_router, tags=["Service"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.APP_PORT, reload=True)
