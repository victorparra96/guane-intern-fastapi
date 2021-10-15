from fastapi import APIRouter

from api.api_v1.endpoints import users, dogs, login, tasks

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(dogs.router, prefix="/dogs", tags=["dogs"])
api_router.include_router(login.router, prefix="/login/token", tags=["login"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
