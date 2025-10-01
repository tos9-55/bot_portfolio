from aiogram import Router
from aiogram.filters import Command

from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.registration.handlers.StartCommandHandler import StartCommandHandler
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository
from system.ioc.ioc import ioc


class RegistrationController:

    def __init__(self):
        self.router = Router()

    def register(self):
        start_command_handler = StartCommandHandler(
            user_repository=ioc.get(IUserRepository),
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.message.register(start_command_handler.__call__, Command(commands=["start"]))
