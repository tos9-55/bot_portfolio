from typing import List

from pydantic import BaseModel

from components.projects.infrastructure.models.ProjectsModel import ProjectsModel


class ProjectWithPhotoModel(BaseModel):
    project: ProjectsModel
    photo: List[str]