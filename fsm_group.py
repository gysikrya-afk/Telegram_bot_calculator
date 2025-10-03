from aiogram.fsm.state import State,StatesGroup

class Calculator(StatesGroup):
    operations = State()
