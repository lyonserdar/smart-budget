from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str | None = None
    description: str | None = None


class ItemCreate(ItemBase):
    title: str

class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True

class ItemInDB(Item):
    pass