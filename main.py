from fastapi import FastAPI

from src.endpoints import router as template_router
from src.db import init_db
from contextlib import asynccontextmanager


# App Config
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run init_db() during the startup of the app
    init_db()  # Initialize the database tables
    yield  # Continue running the app
    # Optional: Place cleanup logic here (on shutdown if necessary)

# App Config
app = FastAPI(
    title="FastAPI Template",
    description="FastAPI template for building APIs",
    version="1.0.0",
    lifespan=lifespan  # Register the lifespan handler
)

# Endpoints
app.include_router(template_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)