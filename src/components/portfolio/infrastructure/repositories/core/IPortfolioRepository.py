from typing import Optional, List

from components.portfolio.infrastructure.models.BasePortfolioModel import BasePortfolioModel
from components.portfolio.infrastructure.models.PortfolioModel import PortfolioModel


class IPortfolioRepository:

    async def get_by_id(self, id: int) -> Optional[PortfolioModel]:
        raise NotImplementedError()

    async def add(self, portfolio: BasePortfolioModel):
        raise NotImplementedError()

    async def get_all_by_user_id(self, user_id: int, offset: int = 0) -> List[PortfolioModel]:
        raise NotImplementedError()

    async def delete(self, portfolio_id: int):
        raise NotImplementedError()

    async def edit(self):
        raise NotImplementedError()