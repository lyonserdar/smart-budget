from api.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bank_name = Column(String)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    account_type_id = Column(Integer, ForeignKey("account_types.id"))

    owner = relationship("User", back_populates="accounts")
    account_type = relationship("AccountType", back_populates="accounts")


class AccountType(Base):
    __tablename__ = "account_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="account_types")
    accounts = relationship("Account", back_populates="account_type")
