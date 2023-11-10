from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database import User
from loader import dp
from switchers import UserSwitchers
from view import buttons_callback_data


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    user, created = User.get_or_create(id=message.from_user.id)
    user.save()
    await message.delete()
    await UserSwitchers.main_menu(message, state, user.id)


@dp.message(Command("admin"))
async def set_admin(message: types.Message, state: FSMContext):
    user = User.get(User.id == message.from_user.id)
    user.is_admin = not user.is_admin
    user.save()
    await message.answer("Done")


@dp.callback_query(F.data == buttons_callback_data.MAIN_MENU)
async def to_main_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await UserSwitchers.main_menu(callback.message, state, callback.from_user.id)
