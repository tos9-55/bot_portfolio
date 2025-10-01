from contextlib import asynccontextmanager
from typing import AsyncGenerator

from databases import Database

from system.connection_pool.factories.core.ISessionFactory import ISessionFactory
from system.connection_pool.session.core.IDatabaseSession import IDatabaseSession
from system.connection_pool.session.impl.PostgresSession import PostgresSession


class SessionFactory(ISessionFactory):

    def __init__(
        self,
        database: Database
    ):
        self._database = database

    async def connect(self):
        await self._database.connect()

    async def disconnect(self):
        await self._database.disconnect()

    @asynccontextmanager
    async def __call__(self) -> AsyncGenerator[IDatabaseSession, None]:
        transaction = await self._database.transaction().__aenter__()
        session = PostgresSession(self._database)
        try:
            yield session
            await transaction.__aexit__(None, None, None)
        except Exception as e:
            await transaction.__aexit__(type(e), e, e.__traceback__)
            raise