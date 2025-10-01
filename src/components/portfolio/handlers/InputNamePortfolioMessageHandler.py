from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from components.portfolio.states.CreatePortfolioStates import CreatePortfolioStates
from components.portfolio.views.InputTextView import InputTextView


class InputNamePortfolioMessageHandler:

    async def __call__(self, message: Message, state: FSMContext):
        portfolio_name = message.text.strip()
        if not portfolio_name:
            await message.answer("Пожалуйста, введите корректное название портфолио.")
            return
        await state.update_data(portfolio_name=portfolio_name)

        text, keyboard = await InputTextView()()

        await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        await state.set_state(CreatePortfolioStates.waiting_for_text)
