class IDatabaseSession:

    async def execute(self, query, values=None):
        raise NotImplementedError()

    async def fetch_one(self, query, values=None):
        raise NotImplementedError()

    async def fetch_all(self, query, values=None):
        raise NotImplementedError()

    async def commit(self):
        raise NotImplementedError()

    async def rollback(self):
        raise NotImplementedError()