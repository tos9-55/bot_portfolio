from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InputTextProjectView:

    async def __call__(self):
        text = (
            "📝 **Введите описание вашего проекта:**"
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🔙 Назад", callback_data="cancel_portfolio_input_name")
                ]
            ]
        )
        return text, keyboard