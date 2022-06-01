from api import schemas
from api.dependencies import oauth2_scheme
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.post("/")
async def create_item(item: schemas.ItemCreate):
    return item


@router.get("/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
