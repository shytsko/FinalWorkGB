from fastapi import FastAPI
import uvicorn
from settings import settings

app = FastAPI()


@app.get("/")
async def index():
    return {"msg": "Hello world!!!!!", "db": settings.REAL_DATABASE_URL}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.APP_PORT, reload=True)
