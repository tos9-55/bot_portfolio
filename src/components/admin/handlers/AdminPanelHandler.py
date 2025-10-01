from aiogram.types import Message

from components.admin.views.AdminPanelView import AdminPanelView
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository


class AdminPanelHandler:
    def __init__(
        self,
        user_repository: IUserRepository
    ):
        self.__user_repository = user_repository

    async def __call__(self, message: Message):
        user_info = await self.__user_repository.get_by_id(user_id=message.from_user.id)
        if not user_info:
            return
        if not user_info.is_admin:
            return

        text, keyboard = await AdminPanelView()()
        await message.answer(text=text, reply_markup=keyboard)