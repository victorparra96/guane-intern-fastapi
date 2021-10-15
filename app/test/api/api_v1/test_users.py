import pytest
import asyncio
from typing import Generator
from fastapi.testclient import TestClient
from app.main import app
from schemas.users import User
from app.test.utils.utils import random_email, random_lower_string

from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["models"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()


def test_create_user(
        client: TestClient,
        event_loop: asyncio.AbstractEventLoop):

    name, last_name, email, password, username = [
        random_lower_string,
        random_lower_string,
        random_email,
        random_lower_string,
        random_lower_string
    ]

    data = {
        "name": name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "username": username
    }

    response = client.post("/api/v1/users", json=data)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == username
    assert "id" in data
    user_id = data["id"]

    async def get_user_by_db():
        user = await User.get(id=user_id)
        return user

    user_obj = event_loop.run_until_complete(get_user_by_db())
    assert user_obj.id == user_id
