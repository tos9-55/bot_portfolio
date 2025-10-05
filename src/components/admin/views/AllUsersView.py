from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from components.user.infrastructure.models.UserModel import UserModel


class AllUsersView:

    async def __call__(self, users: List[UserModel]):
        text = "Список пользователей:\n\nВыберите пользователя, чтобы открыть его профиль."

        inline_keyboard = []
        for user in users:
            username = f"@{user.username}" if user.username else "Без username"
            button_text = f"{username} (ID: {user.user_id})"
            inline_keyboard.append([
                InlineKeyboardButton(
                    text=button_text,
                    callback_data=f"admin_user_profile_{user.user_id}"
                )
            ])

        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard) if inline_keyboard else None
        return text, keyboard
