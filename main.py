from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.db import init_db
from src.endpoints import router as template_router


# App Config
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run init_db() during the startup of the app
    init_db()  # Initialize the database tables
    yield  # Continue running the app


# App Config
app = FastAPI(
    title="FastAPI Template",
    description="FastAPI template for building APIs",
    version="1.0.0",
    lifespan=lifespan,  # Register the lifespan handler
)

# Endpoints
app.include_router(template_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
