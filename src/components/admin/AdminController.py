from aiogram import Router, F
from aiogram.filters import Command

from components.admin.handlers.AdminPanelHandler import AdminPanelHandler
from components.admin.handlers.GetAllUsersHandler import GetAllUsersHandler
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository
from system.ioc.ioc import ioc


class AdminController:

    def __init__(self):
        self.router = Router()

    def register(self):
        admin_panel_handler = AdminPanelHandler(
            user_repository=ioc.get(IUserRepository)
        )
        self.router.message.register(admin_panel_handler.__call__, Command('admin'))

        get_all_users_handler = GetAllUsersHandler(
            user_repository=ioc.get(IUserRepository)
        )
        self.router.callback_query.register(get_all_users_handler.__call__, F.data == "all_users")