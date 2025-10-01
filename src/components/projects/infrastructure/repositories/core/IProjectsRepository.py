from typing import List

from components.projects.infrastructure.models.BaseProjectsModel import BaseProjectsModel
from components.projects.infrastructure.models.ProjectWithPhotoModel import ProjectWithPhotoModel
from components.projects.infrastructure.models.ProjectsModel import ProjectsModel


class IProjectsRepository:

    async def get_all_by_portfolio_id(self, portfolio_id: int) -> List[ProjectsModel]:
        raise NotImplementedError()

    async def delete(self, id: int):
        raise NotImplementedError()

    async def add_photo(self, project_id: int, picture_id: int):
        raise NotImplementedError()

    async def add(self, project: BaseProjectsModel, portfolio_id: int) -> int:
        raise NotImplementedError()

    async def get_by_id(self, id: int) -> ProjectWithPhotoModel:
        raise NotImplementedError()