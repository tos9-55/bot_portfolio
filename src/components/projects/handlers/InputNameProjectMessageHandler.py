from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from components.projects.states.ProjectStates import ProjectStates
from components.projects.views.InputTextProjectView import InputTextProjectView


class InputNameProjectMessageHandler:

    async def __call__(self, message: Message, state: FSMContext):

        project_name = message.text.strip()
        if not project_name:
            await message.answer("❗ Пожалуйста, введите корректное название проекта.")
            return
        await state.update_data(project_name=project_name)

        text, keyboard = await InputTextProjectView()()

        await state.set_state(ProjectStates.waiting_for_project_description)
        await message.answer(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
