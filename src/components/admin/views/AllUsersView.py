from typing import List

from components.user.infrastructure.models.UserModel import UserModel


class AllUsersView:

    async def __call__(self, users: List[UserModel]):
        text = (
            "Список пользователей:\n\n"
        )
        for user in users:
            text += f"ID: {user.user_id}, Username: @{user.username}, Admin: {'Да' if user.is_admin else 'Нет'}\n"
        return text
