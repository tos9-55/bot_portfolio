from sqlalchemy import Column, Integer, String, Text, BigInteger, ForeignKey, DateTime, func

from system.connection_pool.metadata.impl.base import Base


class ProjectsModelTable(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    text = Column(Text, nullable=True)
    created_by = Column(BigInteger, ForeignKey("users.user_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())