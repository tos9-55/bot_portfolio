from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InputTextView:

    async def __call__(self):
        text = (
            "📝 **Опишите ваше портфолио:**"
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🔙 Назад", callback_data="cancel_portfolio_input_text")
                ]
            ]
        )
        return text, keyboard