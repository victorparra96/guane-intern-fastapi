import requests

from typing import List

from fastapi import HTTPException, APIRouter, Depends
from schemas.dogs import Dog_Pydantic, DogIn_Pydantic, Dog
from schemas.users import User
from security import get_current_user
from pydantic import BaseModel

from tortoise.contrib.fastapi import HTTPNotFoundError

router = APIRouter()


class Status(BaseModel):
    message: str


@router.get("/", response_model=List[Dog_Pydantic])
async def get_dogs():
    return await Dog_Pydantic.from_queryset(Dog.all())


@router.get("/is_adopted", response_model=List[Dog_Pydantic])
async def get_dogs_is_adopted():
    return await Dog_Pydantic.from_queryset(Dog.filter(is_adopted=True))


@router.post("/", response_model=Dog_Pydantic)
async def create_dog(
        dog: DogIn_Pydantic,
        current_user: User = Depends(get_current_user)):
    URL = 'https://dog.ceo/api/breeds/image/random'
    data = requests.get(URL)
    data = data.json()
    if data['status'] == 'success':
        user_obj = await Dog.create(
            name=dog.name, picture=data['message'],
            is_adopted=dog.is_adopted, idUser_id=dog.idUser_id)
    else:
        user_obj = await Dog.create(
            name=dog.name,
            is_adopted=dog.is_adopted, idUser_id=dog.idUser_id)
    return await Dog_Pydantic.from_tortoise_orm(user_obj)


@router.get(
    "/{dog_name}",
    response_model=Dog_Pydantic,
    responses={404: {"model": HTTPNotFoundError}}
)
async def get_dog_by_name(dog_name: str):
    return await Dog_Pydantic.from_queryset_single(Dog.get(name=dog_name))


@router.put(
    "/{dog_name}",
    response_model=Dog_Pydantic,
    responses={404: {"model": HTTPNotFoundError}}
)
async def update_dog(dog_name: str, dog: DogIn_Pydantic):
    URL = 'https://dog.ceo/api/breeds/image/random'
    data = requests.get(URL)
    data = data.json()
    if data['status'] == 'success':
        await Dog.filter(name=dog_name).update(
            name=dog.name, picture=data['message'],
            is_adopted=dog.is_adopted, idUser_id=dog.idUser_id)
        return await Dog_Pydantic.from_queryset_single(Dog.get(name=dog.name))
    else:
        await Dog.filter(name=dog_name).update(
            name=dog.name,
            is_adopted=dog.is_adopted, idUser_id=dog.idUser_id)
        return await Dog_Pydantic.from_queryset_single(Dog.get(name=dog.name))


@router.delete(
    "/{dog_name}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}})
async def delete_dog(dog_name: str):
    deleted_count = await Dog.filter(name=dog_name).delete()
    if not deleted_count:
        raise HTTPException(
            status_code=404,
            detail=f"Dog {dog_name} not found")
    return Status(message=f"Deleted dog {dog_name}")
