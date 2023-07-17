from typing import Optional
import uuid
from fastapi_users import schemas
from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey, Integer
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase, SQLAlchemyBaseOAuthAccountTable, SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship, Mapped
from models.models import Base
from models.models import Role
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER


class UserCreate(schemas.BaseUserCreate):
    role_id: int


class UserRead(schemas.BaseUser[int]):
    pass
