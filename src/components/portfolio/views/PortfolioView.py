from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.formatting import Text, Bold

from components.portfolio.infrastructure.models.PortfolioModel import PortfolioModel


class PortfolioView:

    async def __call__(self, portfolio: PortfolioModel, user_id: int):
        text = Text(
            "📂 ", Bold("Название портфолио: "), portfolio.name, "\n\n",
            "📝 ", Bold("Описание:\n"),
            portfolio.text, "\n\n",
            "📅 ", Bold("Дата создания: "), str(portfolio.created_at.strftime("%d/%m/%Y, %H:%M")), "\n",
            "🔄 ", Bold("Дата обновления: "), str(portfolio.updated_at.strftime("%d/%m/%Y, %H:%M"))
        )
        inline_keyboard = []
        if portfolio.created_by == user_id:
            inline_keyboard.append([
                InlineKeyboardButton(text="🔗 Поделиться портфолио", callback_data=f"share_portfolio_{portfolio.id}")
            ])
            inline_keyboard.append([
                InlineKeyboardButton(text="🪣 Удалить", callback_data=f"remove_portfolio_{portfolio.id}")
            ])
        inline_keyboard.append([
            InlineKeyboardButton(text="📋 Проекты", callback_data=f"see_projects_{portfolio.id}")
        ])
        if portfolio.created_by == user_id:
            inline_keyboard.append([
                InlineKeyboardButton(text="🔙 Назад", callback_data=f"see_all_portfolio")
            ])
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=inline_keyboard
        )
        return text.as_markdown(), keyboard