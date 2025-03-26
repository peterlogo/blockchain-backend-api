from fastapi import FastAPI
from contextlib import asynccontextmanager
from .data.setup_db import initialize_db
from .routes import root

@asynccontextmanager
async def startup_event(app: FastAPI):
    await initialize_db()
    yield
    await app.state.db.close()


app = FastAPI(lifespan=startup_event)


app.include_router(root.router)