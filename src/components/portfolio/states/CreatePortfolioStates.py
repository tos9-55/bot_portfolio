from aiogram.fsm.state import State, StatesGroup


class CreatePortfolioStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_text = State()
