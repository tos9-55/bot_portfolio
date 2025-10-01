from typing import Optional, List

from sqlalchemy import select, insert, delete

from components.portfolio.infrastructure.models.BasePortfolioModel import BasePortfolioModel
from components.portfolio.infrastructure.models.PortfolioModel import PortfolioModel
from components.portfolio.infrastructure.models.PortfolioModelTable import PortfolioModelTable
from components.portfolio.infrastructure.repositories.core.IPortfolioRepository import IPortfolioRepository
from system.connection_pool.factories.core.ISessionFactory import ISessionFactory


class PortfolioRepository(IPortfolioRepository):

    def __init__(
        self,
        session_factory: ISessionFactory
    ):
        self.__session_factory = session_factory

    async def get_by_id(self, id: int) -> Optional[PortfolioModel]:
        query = (
            select(PortfolioModelTable)
            .where(PortfolioModelTable.id == id)
        )
        async with self.__session_factory() as session:
            portfolio_info: PortfolioModelTable = await session.fetch_one(query)
        return None if not portfolio_info else PortfolioModel(
            id=portfolio_info.id,
            name=portfolio_info.name,
            text=portfolio_info.text,
            created_by=portfolio_info.created_by,
            created_at=portfolio_info.created_at,
            updated_at=portfolio_info.updated_at,
        )

    async def add(self, portfolio: BasePortfolioModel):
        query = (
            insert(PortfolioModelTable)
            .values(portfolio.model_dump())
        )
        async with self.__session_factory() as session:
            await session.execute(query)

    async def get_all_by_user_id(self, user_id: int, offset: int = 0) -> List[PortfolioModel]:
        query = (
            select(PortfolioModelTable)
            .where(PortfolioModelTable.created_by == user_id)
            .limit(5)
            .offset(offset)
        )
        async with self.__session_factory() as session:
            portfolio_list: List[PortfolioModelTable] = await session.fetch_all(query)

        return [PortfolioModel(
            id=portfolio.id,
            created_at=portfolio.created_at,
            updated_at=portfolio.updated_at,
            name=portfolio.name,
            text=portfolio.text,
            created_by=portfolio.created_by,
        ) for portfolio in portfolio_list]

    async def delete(self, portfolio_id: int):
        query = (
            delete(PortfolioModelTable)
            .where(PortfolioModelTable.id == portfolio_id)
        )
        async with self.__session_factory() as session:
            await session.execute(query)

    async def edit(self):
        raise NotImplementedError()