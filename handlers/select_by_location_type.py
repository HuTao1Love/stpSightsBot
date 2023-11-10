from aiogram import types, F
from aiogram.fsm.context import FSMContext
from states.user import UserStates
from view import buttons_callback_data
from loader import dp
from switchers import UserSwitchers
from database.models import *


@dp.callback_query(UserStates.MAIN_MENU, F.data == buttons_callback_data.MAIN_MENU_START_SELECTING_BY_LOCATION_TYPE)
async def select_location_type(callback: types.CallbackQuery, state: FSMContext):
    await UserSwitchers.select_location_type(callback.message, state)


@dp.callback_query(UserStates.SELECT_LOCATION_TYPE, F.data.isdigit())
async def select_location_type(callback: types.CallbackQuery, state: FSMContext):
    await UserSwitchers.select_location(callback.message, state, int(callback.data))


@dp.callback_query(UserStates.SELECT_LOCATION, F.data.isdigit())
async def select_location(callback: types.CallbackQuery, state: FSMContext):
    await UserSwitchers.current_location(callback.message, state, int(callback.data))


@dp.callback_query(UserStates.LOCATION, F.data == buttons_callback_data.QUEST_WITH_LOCATION)
async def quest_in_location(callback: types.CallbackQuery, state: FSMContext):
    await UserSwitchers.quest_in_location(callback.message, state)
