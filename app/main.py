from contextlib import asynccontextmanager

from uvicorn import run
from fastapi import FastAPI

from core.models import db_assistant

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_assistant.dispose()

app = FastAPI(
    lifespan=lifespan
)

if __name__ == "__main__":
    run("main:app", reload=True)