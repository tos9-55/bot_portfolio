from typing import Optional, Any

from databases import Database

from system.connection_pool.session.core.IDatabaseSession import IDatabaseSession


class PostgresSession(IDatabaseSession):

    def __init__(self, database: Database):
        self._database = database
        self._transaction: Optional[Any] = None

    async def execute(self, query, values=None):
        return await self._database.execute(query=query, values=values)

    async def fetch_one(self, query, values=None):
        return await self._database.fetch_one(query=query, values=values)

    async def fetch_all(self, query, values=None):
        return await self._database.fetch_all(query=query, values=values)

    async def commit(self):
        pass

    async def rollback(self):
        if self._transaction:
            await self._transaction.rollback()