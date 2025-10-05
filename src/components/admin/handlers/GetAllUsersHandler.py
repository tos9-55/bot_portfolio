from aiogram.types import CallbackQuery

from components.admin.views.AllUsersView import AllUsersView
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository


class GetAllUsersHandler:

    def __init__(
        self,
        user_repository: IUserRepository
    ):
        self.__user_repository = user_repository

    async def __call__(self, call: CallbackQuery):
        user_info = await self.__user_repository.get_by_id(user_id=call.from_user.id)
        if not user_info:
            return
        if not user_info.is_admin:
            return

        users = await self.__user_repository.get_all()
        text, keyboard = await AllUsersView()(
            users=users
        )
        await call.answer()
        await call.message.edit_text(text=text, reply_markup=keyboard)
