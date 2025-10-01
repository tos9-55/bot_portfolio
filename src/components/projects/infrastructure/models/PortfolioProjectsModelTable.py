from sqlalchemy import Column, Integer, ForeignKey

from system.connection_pool.metadata.impl.base import Base


class PortfolioProjectsModelTable(Base):
    __tablename__ = "portfolio_projects_mapping"

    id = Column(Integer, primary_key=True, autoincrement=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id", ondelete="CASCADE"))
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"))