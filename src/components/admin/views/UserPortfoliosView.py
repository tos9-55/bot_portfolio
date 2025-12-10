from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from components.portfolio.infrastructure.models.PortfolioModel import PortfolioModel
from components.user.infrastructure.models.UserModel import UserModel


class UserPortfoliosView:

    async def __call__(self, user: UserModel, portfolios: List[PortfolioModel]):
        username = f"@{user.username}" if user.username else "Без username"
        text = (
            "Портфолио пользователя\n\n"
            f"Имя пользователя: {username}\n"
            f"ID: {user.user_id}\n\n"
        )

        inline_keyboard = []
        if portfolios:
            text += "Выберите портфолио для просмотра."
            for portfolio in portfolios:
                inline_keyboard.append([
                    InlineKeyboardButton(
                        text=portfolio.name,
                        callback_data=f"see_portfolio_{portfolio.id}"
                    )
                ])
        else:
            text += "У пользователя пока нет портфолио."

        inline_keyboard.append([
            InlineKeyboardButton(
                text="🔙 Назад к профилю",
                callback_data=f"admin_user_profile_{user.user_id}"
            )
        ])

        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return text, keyboard
