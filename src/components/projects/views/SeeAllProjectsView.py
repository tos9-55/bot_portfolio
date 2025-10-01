from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from components.projects.infrastructure.models.ProjectsModel import ProjectsModel


class SeeAllProjectsView:

    async def __call__(self, project_list: List[ProjectsModel], portfolio_id: int, user_id: int, created_by_portfolio: int):
        text = (
            "Список всех проектов"
        )
        inline_keyboard = []

        for project in project_list:
            element = []
            element.append(InlineKeyboardButton(text=project.name, callback_data=f"see_project_{project.id}"))
            if project.created_by == user_id:
                element.append(InlineKeyboardButton(text="🗑 Удалить", callback_data=f"remove_project_{project.id}"))
            inline_keyboard.append(element)
        if created_by_portfolio == user_id:
            inline_keyboard.append([
                InlineKeyboardButton(text="🆕 Добавить проект", callback_data=f"add_project_{portfolio_id}")
            ])

        inline_keyboard.append([
            InlineKeyboardButton(text="🔙 Назад", callback_data=f"see_portfolio_{portfolio_id}")
        ])
        return text, InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
