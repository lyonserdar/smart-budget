from api import schemas
from api.models import Item
from sqlalchemy.orm import Session


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user_items(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(Item)
        .filter(Item.owner_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
