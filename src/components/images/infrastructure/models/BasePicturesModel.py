from pydantic import BaseModel


class BasePicturesModel(BaseModel):
    file_id: str
    created_by: int