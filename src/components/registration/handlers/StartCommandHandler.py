from aiogram.enums import ParseMode
from aiogram.filters import CommandObject
from aiogram.types import Message

from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.views.PortfolioView import PortfolioView
from components.registration.views.NewUserView import NewUserView
from components.registration.views.OldUserView import OldUserView
from components.user.infrastructure.models.UserModel import UserModel
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository


class StartCommandHandler:

    def __init__(
        self,
        user_repository: IUserRepository,
        portfolio_repository: IPortfolioRepository
    ):
        self.__user_repository = user_repository
        self.__portfolio_repository = portfolio_repository

    async def __call__(self, message: Message, command: CommandObject):
        user_info = await self.__user_repository.get_by_id(user_id=message.from_user.id)

        if command.args:
            portfolio_id = int(command.args.split("_")[-1])

            portfolio_info = await self.__portfolio_repository.get_by_id(id=portfolio_id)

            text, keyboard = await PortfolioView()(
                portfolio=portfolio_info,
                user_id=message.from_user.id
            )

            await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)

        if not user_info:
            await self.__user_repository.add(user=UserModel(
                user_id=message.from_user.id,
                username=message.from_user.username,
                is_admin=False
            ))
            if not command.args:
                text, keyboard = await NewUserView()()
                await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        else:
            if not command.args:
                text, keyboard = await OldUserView()()
                await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
