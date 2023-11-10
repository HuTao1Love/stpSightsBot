from aiogram.types import InlineKeyboardButton
from view import buttons as button_view
from view import buttons_callback_data as button_callback
from buttons.main import generate_inline_keyboard, generate_inline_keyboard_with_back
from database.models import *


def generate_main_menu(user_id: int):
    buttons = [
        InlineKeyboardButton(text=button_view.MAIN_MENU_START_SELECTING_BY_LOCATION_TYPE, callback_data=button_callback.MAIN_MENU_START_SELECTING_BY_LOCATION_TYPE)
    ]
    user = User.get(User.id == user_id)
    if user.is_admin:
        buttons.append([
            InlineKeyboardButton(text=button_view.CREATE_LOCATION_TYPE, callback_data=button_callback.CREATE_LOCATION_TYPE),
            InlineKeyboardButton(text=button_view.CREATE_LOCATION, callback_data=button_callback.CREATE_LOCATION)
        ])

    return generate_inline_keyboard(buttons)


def generate_location_type():
    location_types: list[LocationType] = LocationType.select()

    return generate_inline_keyboard_with_back(
        [InlineKeyboardButton(text=i.name, callback_data=str(i.id)) for i in location_types]
    )


def generate_location_select(location_type_id: int):
    return generate_inline_keyboard_with_back(
        [InlineKeyboardButton(text=i.name, callback_data=str(i.id))
         for i in Location.select().where(Location.type == location_type_id)]
    )


def generate_location(location_id: int):
    location: Location = Location.get(Location.id == location_id)
    return generate_inline_keyboard_with_back([
        [
            InlineKeyboardButton(text=button_view.OPEN_URL_YANDEX, url=location.url_yandex()),
            InlineKeyboardButton(text=button_view.OPEN_URL_GOOGLE, url=location.url_google())
        ],
        InlineKeyboardButton(text=button_view.QUEST_WITH_CURRENT_LOCATION, callback_data=button_callback.QUEST_WITH_LOCATION)
    ])
