from tortoise.contrib.pydantic import pydantic_model_creator

from models import User

User_Pydantic = pydantic_model_creator(User)
UserIn_Pydantic = pydantic_model_creator(
    User,
    name="UserIn",
    exclude_readonly=True)
UserOut_pydantic = pydantic_model_creator(
    User,
    name="UserOut",
    exclude=("hashed_password", ))
