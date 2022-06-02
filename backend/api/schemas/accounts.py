from pydantic import BaseModel


class AccountBase(BaseModel):
    name: str | None = None
    bank_name: str | None = None
    description: str | None = None
    account_type_id: int | None = None


class AccountCreate(AccountBase):
    name: str
    account_type_id: int


class AccountUpdate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class AccountInDB(Account):
    pass


class AccountTypeBase(BaseModel):
    name: str | None = None


class AccountTypeCreate(AccountTypeBase):
    name: str


class AccountTypeUpdate(AccountTypeBase):
    pass


class AccountType(AccountTypeBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class AccountTypeInDB(AccountType):
    pass
