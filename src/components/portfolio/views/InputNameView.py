from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InputNameView:

    async def __call__(self):
        text = (
            "📂 **Введите название вашего портфолио:**"
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🔙 Назад", callback_data="cancel_portfolio_input_name")
                ]
            ]
        )
        return text, keyboard