from aiogram.fsm.state import State, StatesGroup

class ProjectStates(StatesGroup):
    waiting_for_project_name = State()
    waiting_for_project_description = State()
    waiting_for_project_pictures = State()