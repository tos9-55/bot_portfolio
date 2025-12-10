from aiogram.types import CallbackQuery

from components.admin.views.UserProfileView import UserProfileView
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository


class ToggleUserAdminHandler:

    def __init__(
        self,
        user_repository: IUserRepository
    ):
        self.__user_repository = user_repository

    async def __call__(self, call: CallbackQuery):
        current_user = await self.__user_repository.get_by_id(user_id=call.from_user.id)
        if not current_user or not current_user.is_admin:
            await call.answer("Нет доступа", show_alert=True)
            return

        user_id = int(call.data.split("_")[-1])
        if user_id == call.from_user.id:
            await call.answer("Нельзя изменять собственные права", show_alert=True)
            return

        user_info = await self.__user_repository.get_by_id(user_id=user_id)
        if not user_info:
            await call.answer("Пользователь не найден", show_alert=True)
            return

        await self.__user_repository.set_admin_status(
            user_id=user_id,
            is_admin=not user_info.is_admin
        )

        updated_user = await self.__user_repository.get_by_id(user_id=user_id)
        text, keyboard = await UserProfileView()(user=updated_user)
        status_message = (
            "Права администратора выданы"
            if updated_user.is_admin else
            "Права администратора отобраны"
        )
        await call.answer(status_message)
        await call.message.edit_text(text=text, reply_markup=keyboard)
