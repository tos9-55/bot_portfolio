from datetime import datetime

from components.portfolio.infrastructure.models.BasePortfolioModel import BasePortfolioModel


class PortfolioModel(BasePortfolioModel):
    id: int
    created_at: datetime
    updated_at: datetime