from sqlalchemy import Column, BigInteger, String, Boolean

from system.connection_pool.metadata.impl.base import Base


class UserModelTable(Base):

    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True)
    is_admin = Column(Boolean, server_default="false")
    username = Column(String, nullable=True)