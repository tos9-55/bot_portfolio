from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class InputPicturesProjectView:

    async def __call__(self):
        text = (
            "📸 **Отправьте фотографию вашего проекта.** Вы можете прикрепить ОДНУ фотографию"
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Продолжить без фотографий", callback_data="continue")
                ],
                [
                    InlineKeyboardButton(text="🔙 Назад", callback_data="cancel_portfolio_input_name")
                ]
            ]
        )
        return text, keyboard