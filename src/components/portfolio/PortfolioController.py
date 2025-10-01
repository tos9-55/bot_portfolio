from aiogram import Router
from aiogram import F
from aiogram.filters import Command

from components.portfolio.handlers.DeletePortfolioCallbackHandler import DeletePortfolioCallbackHandler
from components.portfolio.handlers.InputNamePortfolioCallbackHandler import InputNamePortfolioCallbackHandler
from components.portfolio.handlers.InputNamePortfolioMessageHandler import InputNamePortfolioMessageHandler
from components.portfolio.handlers.InputTextPortfolioCallbackHandler import InputTextPortfolioCallbackHandler
from components.portfolio.handlers.InputTextPortfolioMessageHandler import InputTextPortfolioMessageHandler
from components.portfolio.handlers.SeeAllPortfolioCallbackHandler import SeeAllPortfolioCallbackHandler
from components.portfolio.handlers.SeeAllPortfolioMessageHandler import SeeAllPortfolioMessageHandler
from components.portfolio.handlers.SeePortfolioCallbackHandler import SeePortfolioCallbackHandler
from components.portfolio.handlers.SharePortfolioCallbackHander import SharePortfolioCallbackHandler
from components.portfolio.handlers.StartCreatePortfolioHandler import StartCreatePortfolioHandler
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.states.CreatePortfolioStates import CreatePortfolioStates
from system.ioc.ioc import ioc


class PortfolioController:

    def __init__(self):
        self.router = Router()

    def register(self):
        start_create_portfolio_handler = StartCreatePortfolioHandler()
        self.router.callback_query.register(start_create_portfolio_handler.__call__, F.data == "create_portfolio")

        input_name_portfolio_message_handler = InputNamePortfolioMessageHandler()
        input_name_portfolio_callback_handler = InputNamePortfolioCallbackHandler(
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.message.register(
            input_name_portfolio_message_handler.__call__,
            CreatePortfolioStates.waiting_for_name
        )
        self.router.callback_query.register(
            input_name_portfolio_callback_handler.__call__,
            CreatePortfolioStates.waiting_for_name,
            F.data == "cancel_portfolio_input_name"
        )

        input_text_portfolio_message_handler = InputTextPortfolioMessageHandler(
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        input_text_portfolio_callback_handler = InputTextPortfolioCallbackHandler()
        self.router.message.register(
            input_text_portfolio_message_handler.__call__,
            CreatePortfolioStates.waiting_for_text
        )
        self.router.callback_query.register(
            input_text_portfolio_callback_handler.__call__,
            CreatePortfolioStates.waiting_for_text,
            F.data == "cancel_portfolio_input_text"
        )

        see_all_portfolio_callback_handler = SeeAllPortfolioCallbackHandler(
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.callback_query.register(
            see_all_portfolio_callback_handler.__call__,
            F.data == "see_all_portfolio"
        )

        see_all_portfolio_message_handler = SeeAllPortfolioMessageHandler(
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.message.register(
            see_all_portfolio_message_handler.__call__,
            Command('my_portfolios')
        )

        see_portfolio_callback_handler = SeePortfolioCallbackHandler(
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.callback_query.register(
            see_portfolio_callback_handler.__call__,
            F.data.startswith("see_portfolio_")
        )

        delete_portfolio_callback_handler = DeletePortfolioCallbackHandler(
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.callback_query.register(
            delete_portfolio_callback_handler.__call__,
            F.data.startswith("remove_portfolio_")
        )

        share_portfolio_callback_handler = SharePortfolioCallbackHandler()
        self.router.callback_query.register(
            share_portfolio_callback_handler.__call__,
            F.data.startswith("share_portfolio_")
        )
