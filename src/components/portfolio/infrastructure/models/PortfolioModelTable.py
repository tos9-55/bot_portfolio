from sqlalchemy import Column, Integer, BigInteger, ForeignKey, DateTime, func, String, Text

from system.connection_pool.metadata.impl.base import Base


class PortfolioModelTable(Base):

    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    created_by = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())