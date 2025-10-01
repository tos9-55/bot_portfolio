from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class AdminPanelView:

    async def __call__(self):
        text = (
            "АДМИН-ПАНЕЛЬ"
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Все пользователи", callback_data="all_users")
                ]
            ]
        )
        return text, keyboard