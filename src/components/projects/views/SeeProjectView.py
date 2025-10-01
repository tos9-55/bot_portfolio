from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from components.projects.infrastructure.models.ProjectsModel import ProjectsModel


class SeeProjectView:

    async def __call__(self, project: ProjectsModel):
        text = (
            f"📂 **Название проекта:** {project.name}\n\n"
            f"📝 **Описание:**\n{project.text}\n\n"
            f"📅 **Дата создания:** {project.created_at.strftime('%d/%m/%Y, %H:%M')}\n"
            f"🔄 **Дата обновления:** {project.updated_at.strftime('%d/%m/%Y, %H:%M')}\n\n"
        )
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Назад", callback_data="cancel")
                ]
            ]
        )
        return text, keyboard
