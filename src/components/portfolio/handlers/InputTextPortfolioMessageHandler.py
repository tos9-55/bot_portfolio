from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from components.portfolio.infrastructure.models.BasePortfolioModel import BasePortfolioModel
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.states.CreatePortfolioStates import CreatePortfolioStates
from components.portfolio.views.AllPortfolioView import AllPortfolioView
from components.portfolio.views.InputTextView import InputTextView


class InputTextPortfolioMessageHandler:

    def __init__(
        self,
        portfolio_repository: IPortfolioRepository
    ):
        self.__portfolio_repository = portfolio_repository

    async def __call__(self, message: Message, state: FSMContext):
        portfolio_text = message.text.strip()
        if not portfolio_text:
            await message.answer("Пожалуйста, введите корректное описание портфолио.")
            return
        user_data = await state.get_data()

        await self.__portfolio_repository.add(portfolio=BasePortfolioModel(
            name=user_data.get('portfolio_name'),
            text=portfolio_text,
            created_by= message.from_user.id,
        ))
        await message.answer("🎉 Ваше портфолио успешно создано! Вы можете просмотреть его в разделе **Мое портфолио**.", parse_mode=ParseMode.MARKDOWN)
        await state.clear()

        portfolio_list = await self.__portfolio_repository.get_all_by_user_id(
            user_id=message.from_user.id
        )
        text, keyboard = await AllPortfolioView()(
            portfolio_list=portfolio_list
        )
        await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)