from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.views.AllPortfolioView import AllPortfolioView


class InputNamePortfolioCallbackHandler:

    def __init__(
        self,
        portfolio_repository: IPortfolioRepository
    ):
        self.__portfolio_repository = portfolio_repository

    async def __call__(self, call: CallbackQuery, state: FSMContext):
        if call.data == "cancel_portfolio_input_name":
            await state.clear()

            portfolio_list = await self.__portfolio_repository.get_all_by_user_id(
                user_id=call.from_user.id
            )
            text, keyboard = await AllPortfolioView()(
                portfolio_list=portfolio_list
            )
            await call.message.edit_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)