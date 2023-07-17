from datetime import datetime
import uuid
from typing import List
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import MetaData,Table,Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False)
    email: Mapped[str] = Column(String, nullable=False)
    hashed_password: Mapped[str] = Column(String, nullable=False)
    is_active: Mapped[bool] = Column(Boolean, nullable=False, default=True)
    is_superuser: Mapped[bool] = Column(Boolean, nullable=False, default=False)
    is_verified: Mapped[bool] = Column(Boolean, nullable=False, default=False)
    
    role: Mapped[List['Role']] = relationship()
    role_id: Mapped[int] = Column(ForeignKey('role.id'))
    


class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = Column(Integer, primary_key=True, nullable=False, unique=True)
    name: Mapped[String] = Column(String, nullable=False)
    permissions: Mapped[JSON] = Column(JSON)

    
    