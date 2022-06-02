from api import functions, schemas
from api.dependencies import get_current_active_user, get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
)


@router.get("/types")
async def get_account_types(
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    return functions.get_user_account_types(db, current_user.id)


@router.post("/types")
async def create_account_type(
    account_type: schemas.AccountTypeCreate,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    db_obj = functions.get_user_account_type_by_name(
        db, current_user.id, account_type.name
    )
    if db_obj:
        raise HTTPException(
            status_code=400, detail="Account type already exists"
        )
    return functions.create_account_type(db, account_type, current_user.id)


@router.get("/types/{account_type_id}")
async def get_account_types(
    account_type_id: int,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    return functions.get_user_account_type(db, current_user.id, account_type_id)


@router.get("/")
async def get_accounts(
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    return functions.get_user_accounts(db, current_user.id)


@router.post("/")
async def create_account(
    account: schemas.AccountCreate,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    if not functions.get_user_account_type(
        db, current_user.id, account.account_type_id
    ):
        raise HTTPException(status_code=400, detail="Unknown account type id")

    if functions.get_user_account_by_name(db, current_user.id, account.name):
        raise HTTPException(
            status_code=400, detail="Account with same name already exists"
        )

    return functions.create_account(db, account, current_user.id)


@router.get("/{account_id}")
async def get_account_types(
    account_id: int,
    current_user: schemas.User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    return functions.get_user_account(db, current_user.id, account_id)
