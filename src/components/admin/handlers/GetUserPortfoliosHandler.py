from aiogram.types import CallbackQuery

from components.admin.views.UserPortfoliosView import UserPortfoliosView
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository


class GetUserPortfoliosHandler:

    def __init__(
        self,
        user_repository: IUserRepository,
        portfolio_repository: IPortfolioRepository
    ):
        self.__user_repository = user_repository
        self.__portfolio_repository = portfolio_repository

    async def __call__(self, call: CallbackQuery):
        current_user = await self.__user_repository.get_by_id(user_id=call.from_user.id)
        if not current_user or not current_user.is_admin:
            await call.answer("Нет доступа", show_alert=True)
            return

        user_id = int(call.data.split("_")[-1])
        user_info = await self.__user_repository.get_by_id(user_id=user_id)
        if not user_info:
            await call.answer("Пользователь не найден", show_alert=True)
            return

        portfolios = await self.__portfolio_repository.get_all_by_user_id(user_id=user_id)
        text, keyboard = await UserPortfoliosView()(user=user_info, portfolios=portfolios)
        await call.answer()
        await call.message.edit_text(text=text, reply_markup=keyboard)
