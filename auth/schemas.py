from typing import Optional
from fastapi_users import schemas

class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    username: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        from_attributes = True


class UserRead(schemas.BaseUser[int]):
    id: int
    role_id: int
    email: str
    username: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
