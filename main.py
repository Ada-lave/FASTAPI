from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI
from auth.auth import auth_backend
from fastapi_users import FastAPIUsers
from pydantic import BaseModel, Field
from auth.manager import get_user_manager
from auth.database import User
from auth.schemas import UserRead, UserCreate


app = FastAPI(
    title='Trading app'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=['auth']
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"]
)