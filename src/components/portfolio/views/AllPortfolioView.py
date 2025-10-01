from typing import List

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from components.portfolio.infrastructure.models.PortfolioModel import PortfolioModel


class AllPortfolioView:

    async def __call__(self, portfolio_list: List[PortfolioModel]):
        text = (
            "📂 Ваши IT-Портфолио\n\n" +
            "Вот список ваших IT-портфолио. Вы можете просматривать, редактировать или удалять их по необходимости."
        )

        inline_keyboard = []
        for portfolio in portfolio_list:
            inline_keyboard.append(
                [
                    InlineKeyboardButton(
                        text=portfolio.name, callback_data=f"see_portfolio_{portfolio.id}"
                    )
                ]
            )
        inline_keyboard.append([
            InlineKeyboardButton(text="🆕 Создать портфолио", callback_data="create_portfolio")
        ])
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
        return text, keyboard