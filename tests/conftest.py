import os
from uuid import uuid4

import pytest
from Crypto.PublicKey import RSA

os.environ["PSQL_DSN"] = "postgresql+asyncpg://asyncdb:asyncdb@localhost/asyncdb"
from asyncdb.models import User, Client
from asyncdb.service import DBStorage

rsa = RSA.generate(2048)


@pytest.fixture(autouse=True)
def settings():
    from asyncdb.config import settings as _settings

    return _settings


@pytest.fixture
async def db() -> DBStorage:
    from asyncdb.service import get_database_storage

    return await get_database_storage()


@pytest.fixture
def user_password():
    return "123"


@pytest.fixture
async def user(db: "DBStorage", user_password: str) -> User:
    user = User(is_superuser=True, is_active=True, username="admin@admin.com")
    user.set_password(user_password)
    await db.add(user)

    return user


@pytest.fixture
async def client(db: "DBStorage", user: "User") -> Client:
    client_id = uuid4()
    client_secret = uuid4()
    grant_types = [
        "authorization_code",
        "client_credentials",
        "password",
        "refresh_token",
    ]
    response_types = [
        "code",
        "id_token",
        "none",
        "token",
    ]

    redirect_uris = ["https://localhost"]

    scope = "read write openid email profile"

    client = Client(
        client_id=str(client_id),
        client_secret=str(client_secret),
        response_types=response_types,
        grant_types=grant_types,
        redirect_uris=redirect_uris,
        scope=scope,
        user_id=user.id,
    )

    await db.add(client)

    return client
