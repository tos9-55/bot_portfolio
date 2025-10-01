from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery

from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.projects.infrastructure.repositories.core.IProjectsRepository import IProjectsRepository
from components.projects.views.SeeAllProjectsView import SeeAllProjectsView


class SeePortfolioProjectsHandler:

    def __init__(
        self,
        portfolio_repository: IPortfolioRepository,
        projects_repository: IProjectsRepository
    ):
        self.__portfolio_repository = portfolio_repository
        self.__projects_repository = projects_repository

    async def __call__(self, call: CallbackQuery):
        portfolio_id = int(call.data.split("_")[-1])

        portfolio_info = await self.__portfolio_repository.get_by_id(id=portfolio_id)
        projects = await self.__projects_repository.get_all_by_portfolio_id(portfolio_id=portfolio_id)

        text, keyboard = await SeeAllProjectsView()(
            project_list=projects,
            portfolio_id=portfolio_id,
            user_id=call.from_user.id,
            created_by_portfolio=portfolio_info.created_by
        )

        await call.message.edit_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
