from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    # DEFAULT
    MAIN_MENU = State()
    SELECT_LOCATION_TYPE = State()
    SELECT_LOCATION = State()
    LOCATION = State()

    # ADMIN
    CREATE_LOCATION_TYPE = State()
    CREATE_LOCATION = State()
    END = State()
