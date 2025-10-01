from typing import Optional

from pydantic import BaseModel


class UserModel(BaseModel):

    user_id: int
    is_admin: bool
    username: Optional[str]