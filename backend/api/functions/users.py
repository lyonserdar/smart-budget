from api import models, schemas
from api.models.users import User
from api.security import get_password_hash, verify_password
from sqlalchemy.orm import Session


def get_user(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> User:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate) -> User:
    db_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        username=user.email,
        name=user.name,
        disabled=False,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db, email: str, password: str) -> User | None:
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
