from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from components.projects.infrastructure.repositories.core.IProjectsRepository import IProjectsRepository

class DeleteProjectHandler:

    def __init__(
        self,
        project_repository: IProjectsRepository
    ):
        self.__project_repository = project_repository

    async def __call__(self, call: CallbackQuery, state: FSMContext):
        project_id = int(call.data.split("_")[-1])

        await self.__project_repository.delete(id=project_id)

        await call.message.answer(text="Проект успешно удалён")

        for index, keyboard in enumerate(reversed(call.message.reply_markup.inline_keyboard), 1):
            if str(project_id) in keyboard[0].callback_data:
                call.message.reply_markup.inline_keyboard.pop(len(call.message.reply_markup.inline_keyboard) - index)

        await call.message.delete()
        await call.message.answer(text=call.message.text, reply_markup=call.message.reply_markup, parse_mode=ParseMode.MARKDOWN)
