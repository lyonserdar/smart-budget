from api.schemas import Item
from pydantic import BaseModel


# Shared Properties
class UserBase(BaseModel):
    email: str
    name: str | None = None
    username: str | None = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: str | None = None


# Additional properties to return via API
class User(UserBase):
    id: int | None = None
    items: list[Item] = []

    class Config:
        orm_mode = True


# Additional properties stored in DB
class UserInDB(User):
    hashed_password: str
    disabled: bool | None = False
