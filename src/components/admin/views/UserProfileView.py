from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from components.user.infrastructure.models.UserModel import UserModel


class UserProfileView:

    async def __call__(self, user: UserModel):
        username = f"@{user.username}" if user.username else "Без username"
        status = "Администратор" if user.is_admin else "Пользователь"
        text = (
            "Профиль пользователя\n\n"
            f"Имя пользователя: {username}\n"
            f"ID: {user.user_id}\n"
            f"Статус: {status}"
        )

        toggle_text = (
            "🔓 Выдать права администратора"
            if not user.is_admin else
            "🔒 Забрать права администратора"
        )

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="📂 Портфолио",
                        callback_data=f"admin_user_portfolios_{user.user_id}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=toggle_text,
                        callback_data=f"admin_user_toggle_admin_{user.user_id}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="🔙 Назад к списку",
                        callback_data="all_users"
                    )
                ]
            ]
        )

        return text, keyboard
