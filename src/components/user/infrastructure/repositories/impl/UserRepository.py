from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.dialects.mysql import insert

from components.user.infrastructure.models.UserModel import UserModel
from components.user.infrastructure.models.UserModelTable import UserModelTable
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository
from system.connection_pool.factories.core.ISessionFactory import ISessionFactory


class UserRepository(IUserRepository):

    def __init__(
        self,
        session_factory: ISessionFactory
    ):
        self.__session_factory = session_factory

    async def add(self, user: UserModel):
        query = (
            insert(UserModelTable)
            .values(user.model_dump())
        )
        async with self.__session_factory() as session:
            await session.execute(query)

    async def get_all(self):
        query = (
            select(UserModelTable)
            .limit(50)
        )
        async with self.__session_factory() as session:
            user_info_list: List[UserModelTable] = await session.fetch_all(query)
        return [UserModel(
            user_id=user_info.user_id,
            is_admin=user_info.is_admin,
            username=user_info.username
        ) for user_info in user_info_list]

    async def get_by_id(self, user_id: int) -> Optional[UserModel]:
        query = (
            select(UserModelTable)
            .where(UserModelTable.user_id == user_id)
        )
        async with self.__session_factory() as session:
            user_info: UserModelTable = await session.fetch_one(query)

        return None if not user_info else UserModel(
            user_id=user_info.user_id,
            is_admin=user_info.is_admin,
            username=user_info.username
        )