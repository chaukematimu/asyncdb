import pytest
from sqlalchemy import select

from asyncdb.models import User
from asyncdb.service import DBStorage


@pytest.mark.asyncio
async def test_add_user(db: "DBStorage", user: "User"):
    q_results = await db.select(
        select(User).where(User.username == "admin@admin.com")
    )
    assert q_results.one_or_none() is not None
