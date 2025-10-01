from typing import Optional

from components.images.infrastructure.models.BasePicturesModel import BasePicturesModel
from components.images.infrastructure.models.PicturesModel import PicturesModel


class IPicturesRepository:

    async def add(self, picture: BasePicturesModel) -> int:
        raise NotImplementedError()

    async def get_by_id(self, picture_id: int) -> Optional[PicturesModel]:
        raise NotImplementedError()
