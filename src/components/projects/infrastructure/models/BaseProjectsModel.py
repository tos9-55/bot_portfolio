from pydantic import BaseModel


class BaseProjectsModel(BaseModel):
    name: str
    text: str
    created_by: int