from audioop import lin2adpcm

from api import schemas
from api.models import AccountType, Item
from sqlalchemy.orm import Session


def create_account_type(
    db: Session, account_type: schemas.AccountTypeCreate, user_id: int
):
    db_obj = AccountType(**account_type.dict(), owner_id=user_id)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_user_account_types(
    db: Session, user_id: int, skip: int = 0, limit: int = 100
):
    return (
        db.query(AccountType)
        .filter(AccountType.owner_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_user_account_type(
    db: Session,
    user_id: int,
    account_type_id: int,
    skip: int = 0,
    limit: int = 100,
):
    return (
        db.query(AccountType)
        .filter(
            AccountType.owner_id == user_id, AccountType.id == account_type_id
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_user_account_type_by_name(
    db: Session,
    user_id: int,
    account_type_name: str,
    skip: int = 0,
    limit: int = 100,
):
    return (
        db.query(AccountType)
        .filter(
            AccountType.owner_id == user_id,
            AccountType.name == account_type_name,
        )
        .offset(skip)
        .limit(limit)
        .all()
    )
