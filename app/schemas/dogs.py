from tortoise.contrib.pydantic import pydantic_model_creator

from models import Dog

Dog_Pydantic = pydantic_model_creator(Dog)
DogIn_Pydantic = pydantic_model_creator(
    Dog,
    name="DogIn",
    exclude_readonly=True)
