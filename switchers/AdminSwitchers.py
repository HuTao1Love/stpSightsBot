from aiogram import types
from aiogram.fsm.context import FSMContext
from states.user import UserStates
from view import buttons, messages
from buttons.main_menu import *


async def ended_admin_action(message: types.Message, state: FSMContext, text):
    await message.delete()
    await state.set_state(UserStates.END)
    await message.answer(text, reply_markup=generate_inline_keyboard_with_back([]))
