from datetime import datetime

from components.images.infrastructure.models.BasePicturesModel import BasePicturesModel


class PicturesModel(BasePicturesModel):
    id: int
    created_at: datetime
    updated_at: datetime