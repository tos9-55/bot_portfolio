from typing import List

from sqlalchemy import select, insert, delete

from components.images.infrastructure.models.PicturesModelTable import PicturesModelTable
from components.projects.infrastructure.models.BaseProjectsModel import BaseProjectsModel
from components.projects.infrastructure.models.PortfolioProjectsModelTable import PortfolioProjectsModelTable
from components.projects.infrastructure.models.ProjectPicturesModelTable import ProjectPicturesModelTable
from components.projects.infrastructure.models.ProjectWithPhotoModel import ProjectWithPhotoModel
from components.projects.infrastructure.models.ProjectsModel import ProjectsModel
from components.projects.infrastructure.models.ProjectsModelTable import ProjectsModelTable
from components.projects.infrastructure.repositories.core.IProjectsRepository import IProjectsRepository
from system.connection_pool.factories.core.ISessionFactory import ISessionFactory


class ProjectsRepository(IProjectsRepository):

    def __init__(
        self,
        session_factory: ISessionFactory
    ):
        self.__session_factory = session_factory

    async def get_all_by_portfolio_id(self, portfolio_id: int) -> List[ProjectsModel]:
        query = (
            select(ProjectsModelTable)
            .join(PortfolioProjectsModelTable, ProjectsModelTable.id == PortfolioProjectsModelTable.project_id)
            .where(PortfolioProjectsModelTable.portfolio_id == portfolio_id)
        )
        async with self.__session_factory() as session:
            project_list: List[ProjectsModel] = await session.fetch_all(query)
        return [ProjectsModel(
            id=project.id,
            created_at=project.created_at,
            updated_at=project.updated_at,
            name=project.name,
            text=project.text,
            created_by=project.created_by,
        ) for project in project_list]

    async def delete(self, id: int):
        query = (
            delete(ProjectsModelTable)
            .where(ProjectsModelTable.id == id)
        )
        async with self.__session_factory() as session:
            await session.execute(query)

    async def add_photo(self, project_id: int, picture_id: int):
        query = (
            insert(ProjectPicturesModelTable)
            .values(
                picture_id=picture_id,
                project_id=project_id
            )
        )
        async with self.__session_factory() as session:
            await session.execute(query)

    async def add(self, project: BaseProjectsModel, portfolio_id: int):
        query = (
            insert(ProjectsModelTable)
            .values(
                name=project.name,
                text=project.text,
                created_by=project.created_by
            )
            .returning(ProjectsModelTable.id)
        )
        async with self.__session_factory() as session:
            project = await session.fetch_one(query)
            query = (
                insert(PortfolioProjectsModelTable)
                .values(
                    portfolio_id=portfolio_id,
                    project_id=project.id
                )
            )
            await session.execute(query)
        return project.id

    async def get_by_id(self, id: int) -> ProjectWithPhotoModel:
        query = (
           select(ProjectsModelTable)
           .where(ProjectsModelTable.id == id)
        )
        query_photo = (
            select(PicturesModelTable.file_id)
            .join(ProjectPicturesModelTable, ProjectPicturesModelTable.picture_id == PicturesModelTable.id)
            .where(ProjectPicturesModelTable.project_id == id)
        )
        async with self.__session_factory() as session:
            project = await session.fetch_one(query)
            photo_list = await session.fetch_all(query_photo)
        return ProjectWithPhotoModel(
            project=ProjectsModel(
                id=project.id,
                created_at=project.created_at,
                updated_at=project.updated_at,
                name=project.name,
                text=project.text,
                created_by=project.created_by,
            ),
            photo=[photo.file_id for photo in photo_list]
        )