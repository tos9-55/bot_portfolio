from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from components.projects.states.ProjectStates import ProjectStates
from components.projects.views.InputNameProjectView import InputNameProjectView


class AddPortfolioProjectHandler:

    async def __call__(self, call: CallbackQuery, state: FSMContext):
        portfolio_id = int(call.data.split("_")[-1])

        text, keyboard = await InputNameProjectView()()
        await state.set_state(ProjectStates.waiting_for_project_name)
        await state.update_data(portfolio_id=portfolio_id)

        await call.message.edit_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
