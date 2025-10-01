from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.views.PortfolioView import PortfolioView


class SeePortfolioCallbackHandler:

    def __init__(
        self,
        portfolio_repository: IPortfolioRepository
    ):
        self.__portfolio_repository = portfolio_repository

    async def __call__(self, call: CallbackQuery, state: FSMContext):
        portfolio_id = int(call.data.split("_")[-1])

        portfolio_info = await self.__portfolio_repository.get_by_id(id=portfolio_id)

        text, keyboard = await PortfolioView()(
            portfolio=portfolio_info,
            user_id=call.from_user.id
        )

        await call.message.edit_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)