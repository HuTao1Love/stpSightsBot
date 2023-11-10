from aiogram import types
from aiogram.fsm.context import FSMContext
from states.user import UserStates
from view import buttons, messages
from buttons.main_menu import *


async def main_menu(message: types.Message, state: FSMContext, user_id):
    await state.set_state(UserStates.MAIN_MENU)
    await message.answer(messages.IN_MAIN_MENU, reply_markup=generate_main_menu(user_id))


async def select_location_type(message: types.Message, state: FSMContext):
    print("Select location type")
    await state.set_state(UserStates.SELECT_LOCATION_TYPE)
    await message.edit_text(messages.IN_SELECT_LOCATION_TYPE, reply_markup=generate_location_type())


async def select_location(message: types.Message, state: FSMContext, location_type_id: int):
    print("Select location")
    await state.set_state(UserStates.SELECT_LOCATION)
    await message.edit_text(
        messages.IN_SELECT_LOCATION.format(location_type_name=LocationType.get(LocationType.id == location_type_id).name),
        reply_markup=generate_location_select(location_type_id)
    )


async def current_location(message: types.Message, state: FSMContext, location_id: int):
    print("Current location")
    location = Location.select().where(Location.id == location_id).get()
    await state.set_state(UserStates.LOCATION)
    await state.set_data({"location": location_id})
    await message.delete()
    await message.answer_photo(location.photo, caption=location.get_text(), reply_markup=generate_location(location.id))


async def quest_in_location(message: types.Message, state: FSMContext):
    print("Quest with location")
    location = Location.get(Location.id == (await state.get_data())["location"])
    await message.delete()
    await message.answer(f"TODO\nЗдесь потом будут квесты с локацией {location.name}", reply_markup=generate_inline_keyboard_with_back([]))
