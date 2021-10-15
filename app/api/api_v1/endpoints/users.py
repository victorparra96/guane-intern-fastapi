from typing import List

from fastapi import HTTPException, APIRouter
from schemas.users import User_Pydantic, UserIn_Pydantic, User
from security import get_password_hash
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()


class Status(BaseModel):
    message: str


@router.get("/", response_model=List[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())


@router.post("/", response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = await User.create(
        name=user.name, last_name=user.last_name,
        email=user.email,
        hashed_password=get_password_hash(user.hashed_password),
        username=user.username)
    return await User_Pydantic.from_tortoise_orm(user_obj)


@router.get(
    "/{user_id}",
    response_model=User_Pydantic,
    responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@router.put(
    "/{user_id}",
    response_model=User_Pydantic,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_user(user_id: int, user: UserIn_Pydantic):
    await User.filter(id=user_id).update(
        name=user.name, last_name=user.last_name,
        email=user.email,
        hashed_password=get_password_hash(user.hashed_password),
        username=user.username
    )
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@router.delete(
    "/{user_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}})
async def delete_user(user_id: int):
    deleted_count = await User.filter(id=user_id).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found")
    return Status(message=f"Deleted user {user_id}")
