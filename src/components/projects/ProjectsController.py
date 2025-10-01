from aiogram import Router, F

from components.images.infrastructure.repositories.core.IPicturesRepository import IPicturesRepository
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from components.projects.handlers.AddPortfolioProjectHandler import AddPortfolioProjectHandler
from components.projects.handlers.DeleteProjectHandler import DeleteProjectHandler
from components.projects.handlers.InputImageProjectCallbackHandler import InputImageProjectCallbackHandler
from components.projects.handlers.InputImageProjectMessageHandler import InputImageProjectMessageHandler
from components.projects.handlers.InputNameProjectMessageHandler import InputNameProjectMessageHandler
from components.projects.handlers.InputTextProjectMessageHandler import InputTextProjectMessageHandler
from components.projects.handlers.SeePortfolioProjectsHandler import SeePortfolioProjectsHandler
from components.projects.handlers.SeeProjectHandler import SeeProjectHandler
from components.projects.infrastructure.repositories.core.IProjectsRepository import IProjectsRepository
from components.projects.states.ProjectStates import ProjectStates
from system.ioc.ioc import ioc


class ProjectsController:

    def __init__(self):
        self.router = Router()

    def register(self):
        see_portfolio_projects_handler = SeePortfolioProjectsHandler(
            projects_repository=ioc.get(IProjectsRepository),
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.callback_query.register(
            see_portfolio_projects_handler.__call__,
            F.data.startswith("see_projects_")
        )

        add_portfolio_project_handler = AddPortfolioProjectHandler()
        self.router.callback_query.register(
            add_portfolio_project_handler.__call__,
            F.data.startswith("add_project_")
        )

        input_name_project_message_handler = InputNameProjectMessageHandler()
        self.router.message.register(
            input_name_project_message_handler.__call__,
            ProjectStates.waiting_for_project_name
        )

        input_text_project_message_handler = InputTextProjectMessageHandler()
        self.router.message.register(
            input_text_project_message_handler.__call__,
            ProjectStates.waiting_for_project_description
        )

        input_image_project_message_handler = InputImageProjectMessageHandler(
            project_repository=ioc.get(IProjectsRepository),
            pictures_repository=ioc.get(IPicturesRepository),
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        input_image_project_callback_handler = InputImageProjectCallbackHandler(
            project_repository=ioc.get(IProjectsRepository),
            portfolio_repository=ioc.get(IPortfolioRepository)
        )
        self.router.message.register(
            input_image_project_message_handler.__call__,
            ProjectStates.waiting_for_project_pictures
        )
        self.router.callback_query.register(
            input_image_project_callback_handler.__call__,
            ProjectStates.waiting_for_project_pictures,
            F.data == "continue"
        )

        see_project_handler = SeeProjectHandler(
            project_repository=ioc.get(IProjectsRepository)
        )
        self.router.callback_query.register(
            see_project_handler.__call__,
            F.data.startswith("see_project_")
        )

        delete_project_handler = DeleteProjectHandler(
            project_repository=ioc.get(IProjectsRepository)
        )
        self.router.callback_query.register(
            delete_project_handler.__call__,
            F.data.startswith("remove_project_")
        )
