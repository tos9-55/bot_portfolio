from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from components.projects.states.ProjectStates import ProjectStates
from components.projects.views.InputPicturesProjectView import InputPicturesProjectView


class InputTextProjectMessageHandler:

    async def __call__(self, message: Message, state: FSMContext):
        text, keyboard = await InputPicturesProjectView()()

        project_description = message.text.strip()
        if not project_description:
            await message.answer("❗ Пожалуйста, введите корректное описание проекта.")
            return
        await state.update_data(project_description=project_description)
        await state.set_state(ProjectStates.waiting_for_project_pictures)
        await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
