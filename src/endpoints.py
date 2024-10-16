from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db import get_db

# Create an APIRouter instance
router = APIRouter()


@router.get("/health")
def health():
    return {"message": "OK!"}


# Get the lowest bid endpoint
@router.get("/endpoint")
async def endpoint(db: Session = Depends(get_db)):
    pass
