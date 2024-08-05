from contextlib import asynccontextmanager

from uvicorn import run
from fastapi import FastAPI

from core.models import db_assistant, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with db_assistant.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    # shutdown
    await db_assistant.dispose()

app = FastAPI(
    lifespan=lifespan
)

if __name__ == "__main__":
    run("main:app", reload=True)
