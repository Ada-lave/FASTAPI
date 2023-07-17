from typing import Optional
from uuid import UUID
from fastapi import Depends, Request, exceptions
from fastapi_users import BaseUserManager, UUIDIDMixin, models, schemas
from auth.database import User 

from auth.database import User, get_user_db

SECRET = 'SECRET'


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"user  {user.id} has registered")

    


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)