from aiogram.enums import ParseMode
from aiogram.types import Message

from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.views.AllPortfolioView import AllPortfolioView


class SeeAllPortfolioMessageHandler:

    def __init__(
        self,
        portfolio_repository: IPortfolioRepository
    ):
        self.__portfolio_repository = portfolio_repository

    async def __call__(self, message: Message):
        portfolio_list = await self.__portfolio_repository.get_all_by_user_id(
            user_id=message.from_user.id
        )
        text, keyboard = await AllPortfolioView()(
            portfolio_list=portfolio_list
        )
        await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
