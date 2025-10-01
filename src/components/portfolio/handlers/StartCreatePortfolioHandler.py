from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from components.portfolio.states.CreatePortfolioStates import CreatePortfolioStates
from components.portfolio.views.InputNameView import InputNameView


class StartCreatePortfolioHandler:

    async def __call__(self, call: CallbackQuery, state: FSMContext) -> None:
        text, keyboard = await InputNameView()()
        await state.set_state(CreatePortfolioStates.waiting_for_name)
        await call.message.edit_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)