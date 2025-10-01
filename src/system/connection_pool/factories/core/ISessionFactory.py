from typing import AsyncGenerator

from system.connection_pool.session.core.IDatabaseSession import IDatabaseSession


class ISessionFactory:

    async def connect(self):
        raise NotImplementedError()

    async def disconnect(self):
        raise NotImplementedError()

    async def __call__(self) -> AsyncGenerator[IDatabaseSession, None]:
        raise NotImplementedError()
