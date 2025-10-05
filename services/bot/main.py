import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from databases import Database
from dotenv import load_dotenv

from components.admin.AdminController import AdminController
from components.images.infrastructure.repositories.core.IPicturesRepository import IPicturesRepository
from components.images.infrastructure.repositories.impl.PicturesRepository import PicturesRepository
from components.portfolio.PortfolioController import PortfolioController
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.portfolio.infrastructure.repositories.impl.PortfolioRepository import PortfolioRepository
from components.projects.ProjectsController import ProjectsController
from components.projects.infrastructure.repositories.core.IProjectsRepository import IProjectsRepository
from components.projects.infrastructure.repositories.impl.ProjectsRepository import ProjectsRepository
from components.registration.RegistrationController import RegistrationController
from components.registration.handlers.StartCommandHandler import StartCommandHandler
from components.user.infrastructure.repositories.core.IUserRepository import IUserRepository
from components.user.infrastructure.repositories.impl.UserRepository import UserRepository
from system.connection_pool.factories.core.ISessionFactory import ISessionFactory
from system.connection_pool.factories.impl.SessionFactory import SessionFactory
from system.ioc.ioc import ioc


async def main():
    load_dotenv()

    database = Database(
        f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASS')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DATABASE')}",
        min_size=1,
        max_size=10
    )
    session_factory = SessionFactory(
        database=database
    )

    ioc.set(ISessionFactory, session_factory)
    ioc.set(IUserRepository, UserRepository(
        session_factory=session_factory
    ))
    ioc.set(IPortfolioRepository, PortfolioRepository(
        session_factory=session_factory
    ))
    ioc.set(IProjectsRepository, ProjectsRepository(
        session_factory=session_factory
    ))
    ioc.set(IPicturesRepository, PicturesRepository(
        session_factory=session_factory
    ))
    await database.connect()

    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    portfolio_controller = PortfolioController()
    registration_controller = RegistrationController()
    projects_controller = ProjectsController()
    admin_controller = AdminController()

    portfolio_controller.register()
    registration_controller.register()
    projects_controller.register()
    admin_controller.register()

    dp.include_router(router=portfolio_controller.router)
    dp.include_router(router=registration_controller.router)
    dp.include_router(router=projects_controller.router)
    dp.include_router(router=admin_controller.router)

    try:
        print("Бот запущен...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await database.disconnect()

if __name__ == '__main__':
    asyncio.run(main())