from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from components.images.infrastructure.models.BasePicturesModel import BasePicturesModel
from components.images.infrastructure.repositories.core.IPicturesRepository import IPicturesRepository
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.views.PortfolioView import PortfolioView
from components.projects.infrastructure.models.BaseProjectsModel import BaseProjectsModel
from components.projects.infrastructure.repositories.core.IProjectsRepository import IProjectsRepository


class InputImageProjectMessageHandler:

    def __init__(
        self,
        portfolio_repository: IPortfolioRepository,
        project_repository: IProjectsRepository,
        pictures_repository: IPicturesRepository
    ):
        self.__portfolio_repository = portfolio_repository
        self.__project_repository = project_repository
        self.__pictures_repository = pictures_repository

    async def __call__(self, message: Message, state: FSMContext):
        if not message.photo:
            await message.answer("❗ Пожалуйста, отправьте фотографии вашего проекта.")
            return

        user_data = await state.get_data()
        project_name = user_data.get('project_name')
        project_description = user_data.get('project_description')
        user_id = message.from_user.id

        portfolio_id = user_data.get('portfolio_id')  # Предположим, что portfolio_id сохранён ранее
        if not portfolio_id:
            await message.answer("❌ Не удалось определить ваш портфель. Пожалуйста, начните процесс заново.")
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
        await state.update_data(project_id=project_id)
        if message.photo:
            file_id = message.photo[-1].file_id
            picture_id = await self.__pictures_repository.add(picture=BasePicturesModel(
                file_id=file_id,
                created_by=user_id
            ))
            await self.__project_repository.add_photo(
                project_id=project_id,
                picture_id=picture_id
            )

        portfolio_info = await self.__portfolio_repository.get_by_id(id=portfolio_id)

        text, keyboard = await PortfolioView()(
            portfolio=portfolio_info,
            user_id=message.from_user.id
        )

        await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        await state.clear()