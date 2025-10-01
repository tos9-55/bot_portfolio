from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.views.AllPortfolioView import AllPortfolioView


class DeletePortfolioCallbackHandler:

    def __init__(
        self,
        portfolio_repository: IPortfolioRepository
    ):
        self.__portfolio_repository = portfolio_repository

    async def __call__(self, call: CallbackQuery, state: FSMContext):
        portfolio_id = int(call.data.split("_")[-1])

        portfolio_info = await self.__portfolio_repository.get_by_id(id=portfolio_id)

        if portfolio_info.created_by != call.from_user.id:
            await call.message.answer(text="Это не ваше портфолио!")
            return

        await self.__portfolio_repository.delete(portfolio_id=portfolio_id)

        await call.message.answer(text="Портфолио успешно удалено!")

        portfolio_list = await self.__portfolio_repository.get_all_by_user_id(
            user_id=call.from_user.id
        )
        text, keyboard = await AllPortfolioView()(
            portfolio_list=portfolio_list
        )
        await call.message.edit_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
