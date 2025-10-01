from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, DateTime, func

from system.connection_pool.metadata.impl.base import Base


class PicturesModelTable(Base):
    __tablename__ = "pictures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(String, nullable=False)
    created_by = Column(BigInteger, ForeignKey("users.user_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())