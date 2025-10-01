from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InputNameProjectView:

    async def __call__(self):
        text = (
            "📝 **Введите название вашего проекта:**"
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="🔙 Назад", callback_data="cancel_portfolio_input_name")
                ]
            ]
        )
        return text, keyboard