from api import schemas
from api.dependencies import oauth2_scheme
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
)


@router.post("/")
async def create_item(account: schemas.Account):
    return account


@router.get("/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.get("/{account_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
