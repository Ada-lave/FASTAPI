from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI
from fastapi import Depends
from auth.auth import auth_backend
from fastapi_users import FastAPIUsers
from pydantic import BaseModel, Field
from auth.manager import get_user_manager
from auth.database import User
from auth.schemas import UserRead, UserCreate
from uuid import UUID
from auth.database import create_db_and_tables


app = FastAPI(
    title='Trading app'
)

fastapi_users = FastAPIUsers[User, UUID](
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
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected_route")
def protected(user: User = Depends(current_user)):
    return f"Hello {user.email}"