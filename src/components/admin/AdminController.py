from aiogram import Router, F
from aiogram.filters import Command

from components.admin.handlers.AdminPanelHandler import AdminPanelHandler
from components.admin.handlers.GetAllUsersHandler import GetAllUsersHandler
from components.admin.handlers.GetUserProfileHandler import GetUserProfileHandler
from components.admin.handlers.GetUserPortfoliosHandler import GetUserPortfoliosHandler
from components.admin.handlers.ToggleUserAdminHandler import ToggleUserAdminHandler
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
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

        get_user_profile_handler = GetUserProfileHandler(
            user_repository=ioc.get(IUserRepository)
        )
        self.router.callback_query.register(
            get_user_profile_handler.__call__,
            F.data.startswith("admin_user_profile_")
        )

        get_user_portfolios_handler = GetUserPortfoliosHandler(
            user_repository=ioc.get(IUserRepository),
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.callback_query.register(
            get_user_portfolios_handler.__call__,
            F.data.startswith("admin_user_portfolios_")
        )

        toggle_user_admin_handler = ToggleUserAdminHandler(
            user_repository=ioc.get(IUserRepository)
        )
        self.router.callback_query.register(
            toggle_user_admin_handler.__call__,
            F.data.startswith("admin_user_toggle_admin_")
        )
