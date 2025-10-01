from datetime import datetime

from components.projects.infrastructure.models.BaseProjectsModel import BaseProjectsModel


class ProjectsModel(BaseProjectsModel):
    id: int
    created_at: datetime
    updated_at: datetime