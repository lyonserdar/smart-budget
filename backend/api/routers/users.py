from api import functions, schemas
from api.dependencies import get_current_active_user, get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = functions.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )
    return functions.create_user(db=db, user=user)


@router.get("/me", response_model=schemas.User)
async def read_users_me(
    current_user: schemas.User = Depends(get_current_active_user),
):
    return current_user


@router.get("/me/items/")
async def read_own_items(
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    return functions.get_user_items(db, current_user.id)
