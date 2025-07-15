from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.connection_api.db.base import get_db
from src.connection_api import schemas
from src.connection_api import services

router = APIRouter()


@router.post("/puzzles/", response_model=schemas.PuzzleShow)
async def create_new_puzzle(
    puzzle: schemas.PuzzleCreate,
    db: AsyncSession = Depends(get_db)
):
    return await services.create_puzzle(db=db, puzzle=puzzle)