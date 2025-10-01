from typing import Optional

from components.user.infrastructure.models.UserModel import UserModel


class IUserRepository:

    async def add(self, user: UserModel):
        raise NotImplementedError()

    async def get_all(self):
        raise NotImplementedError()

    async def get_by_id(self, user_id: int) -> Optional[UserModel]:
        raise NotImplementedError()