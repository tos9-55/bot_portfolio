from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery, InputMediaPhoto

from components.projects.infrastructure.repositories.core.IProjectsRepository import IProjectsRepository
from components.projects.views.SeeProjectView import SeeProjectView


class SeeProjectHandler:

    def __init__(
        self,
        project_repository: IProjectsRepository
    ):
        self.__project_repository = project_repository

    async def __call__(self, call: CallbackQuery):
        project_id = int(call.data.split("_")[-1])

        project_info = await self.__project_repository.get_by_id(id=project_id)

        text, keyboard = await SeeProjectView()(project=project_info.project)
        media = []
        for idx, file_id in enumerate(project_info.photo):
            if idx == 0:
                media.append(InputMediaPhoto(media=file_id, caption=text, parse_mode=ParseMode.MARKDOWN))
            else:
                media.append(InputMediaPhoto(media=file_id))
        await call.message.delete()
        if media:
            await call.message.answer_media_group(media=media)
        else:
            await call.message.answer(text=text, parse_mode=ParseMode.MARKDOWN)
        await call.message.answer(text=call.message.text, reply_markup=call.message.reply_markup, parse_mode=ParseMode.MARKDOWN)

