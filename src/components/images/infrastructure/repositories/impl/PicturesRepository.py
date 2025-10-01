from typing import Optional

from sqlalchemy import insert

from components.images.infrastructure.models.BasePicturesModel import BasePicturesModel
from components.images.infrastructure.models.PicturesModel import PicturesModel
from components.images.infrastructure.models.PicturesModelTable import PicturesModelTable
from components.images.infrastructure.repositories.core.IPicturesRepository import IPicturesRepository
from system.connection_pool.factories.core.ISessionFactory import ISessionFactory


class PicturesRepository(IPicturesRepository):

    def __init__(
        self,
        session_factory: ISessionFactory
    ):
        self.__session_factory = session_factory

    async def add(self, picture: BasePicturesModel):
        query = (
            insert(PicturesModelTable)
            .values(picture.model_dump())
            .returning(PicturesModelTable.id)
        )
        async with self.__session_factory() as session:
            picture = await session.fetch_one(query)

        return picture.id

    async def get_by_id(self, picture_id: int) -> Optional[PicturesModel]:
        raise NotImplementedError()
