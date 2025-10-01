from sqlalchemy import Column, Integer, ForeignKey

from system.connection_pool.metadata.impl.base import Base


class ProjectPicturesModelTable(Base):
    __tablename__ = "project_pictures_mapping"

    id = Column(Integer, primary_key=True, autoincrement=True)
    picture_id = Column(Integer, ForeignKey("pictures.id", ondelete="CASCADE"))
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"))