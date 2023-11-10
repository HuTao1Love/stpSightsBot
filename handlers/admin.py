from aiogram import types, F
from aiogram.fsm.context import FSMContext
from states.user import UserStates
from switchers import AdminSwitchers
from view import buttons_callback_data
from loader import dp
from view import messages
from database.models import *


@dp.callback_query(UserStates.MAIN_MENU, F.data == buttons_callback_data.CREATE_LOCATION_TYPE)
async def create_location_type_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserStates.CREATE_LOCATION_TYPE)
    await callback.message.edit_text(messages.CREATE_NEW_LOCATION_TYPE)
    await state.set_data({"message_id": callback.message.message_id, "chat_id": callback.message.chat.id})


@dp.message(UserStates.CREATE_LOCATION_TYPE)
async def create_location_type_end(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.bot.delete_message(chat_id=data['chat_id'], message_id=data['message_id'])
    await state.set_state(UserStates.END)
    location_type, created = LocationType.get_or_create(name=message.text)
    location_type.save()
    if not  created:
        await AdminSwitchers.ended_admin_action(message, state, formatted.LOCATION_TYPE_ALREADY_EXISTS_END.format(name=location_type.name))
    else:
        await AdminSwitchers.ended_admin_action(message, state, formatted.LOCATION_TYPE_CREATE_END.format(name=location_type.name))
