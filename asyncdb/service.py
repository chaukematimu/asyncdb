from typing import Optional

from sqlalchemy import NullPool
from sqlalchemy.engine.result import Result
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.sql.expression import Delete, Update
from sqlalchemy.sql.selectable import Select
from sqlmodel.ext.asyncio.session import AsyncSession

from asyncdb.config import settings


class Transaction:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def __aenter__(self) -> "Transaction":
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is None:
            await self.commit()
        else:
            await self.rollback()

        await self.close()

    async def rollback(self):
        await self.session.rollback()

    async def commit(self):
        await self.session.commit()

    async def close(self):
        await self.session.close()


class DBStorage:
    def __init__(
            self: "DBStorage",
            session: AsyncSession,
            transaction: Transaction
    ) -> None:
        self.session = session
        self.transaction = transaction

    async def select(self, q: Select) -> Result:
        async with self.transaction:
            return await self.session.execute(q)

    async def add(self, model) -> None:
        async with self.transaction:
            self.session.add(model)

    async def delete(self, q: Delete) -> None:
        async with self.transaction:
            await self.session.execute(q)

    async def update(self, q: Update):
        async with self.transaction:
            await self.session.execute(q)


async def get_database_storage() -> DBStorage:
    if Database.async_session is None:
        await Database.connect()
    return DBStorage(
        session=Database.async_session,
        transaction=Transaction(session=Database.async_session)
    )


class Database:
    async_session: Optional[AsyncSession] = None

    @classmethod
    async def connect(cls):
        engine = create_async_engine(settings.PSQL_DSN, echo=True, poolclass=NullPool)
        async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
        cls.async_session = async_session()

    @classmethod
    async def disconnect(cls):
        if cls.async_session is not None:
            await cls.async_session.close()
