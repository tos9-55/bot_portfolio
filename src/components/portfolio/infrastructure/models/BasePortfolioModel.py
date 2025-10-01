from pydantic import BaseModel


class BasePortfolioModel(BaseModel):
    name: str
    text: str
    created_by: int