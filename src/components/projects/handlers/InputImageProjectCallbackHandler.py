from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from components.images.infrastructure.repositories.core.IPicturesRepository import IPicturesRepository
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.views.PortfolioView import PortfolioView
from components.projects.infrastructure.models.BaseProjectsModel import BaseProjectsModel
from components.projects.infrastructure.repositories.core.IProjectsRepository import IProjectsRepository


class InputImageProjectCallbackHandler:

    def __init__(
        self,
        portfolio_repository: IPortfolioRepository,
        project_repository: IProjectsRepository,
    ):
        self.__portfolio_repository = portfolio_repository
        self.__project_repository = project_repository

    async def __call__(self, call: CallbackQuery, state: FSMContext):
        user_data = await state.get_data()
        project_name = user_data.get('project_name')
        project_description = user_data.get('project_description')
        user_id = call.from_user.id

        portfolio_id = user_data.get('portfolio_id')
        if not portfolio_id:
            await call.message.answer("❌ Не удалось определить ваш портфель. Пожалуйста, начните процесс заново.")
            await state.clear()
            return

        project_id = await self.__project_repository.add(
            project=BaseProjectsModel(
                name=project_name,
                text=project_description,
                created_by=user_id
            ),
            portfolio_id=portfolio_id
        )

        portfolio_info = await self.__portfolio_repository.get_by_id(id=portfolio_id)

        text, keyboard = await PortfolioView()(
            portfolio=portfolio_info,
            user_id=call.from_user.id
        )

        await call.message.delete()
        await call.message.answer(text="Проект успешно добавлен")
        await call.message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        await state.clear()