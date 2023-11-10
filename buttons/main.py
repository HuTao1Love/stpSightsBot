from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from view import buttons as button_view, buttons_callback_data as button_callback


def generate_inline_keyboard(values: list[list[InlineKeyboardButton] | InlineKeyboardButton]) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    for row in values:
        buttons_insert = [row] if isinstance(row, InlineKeyboardButton) else row
        keyboard.row(*buttons_insert)
    return keyboard.as_markup(resize_keyboards=True)


def generate_inline_keyboard_with_back(values: list[list[InlineKeyboardButton] | InlineKeyboardButton]) -> InlineKeyboardMarkup:
    return generate_inline_keyboard(values + [
        [
            InlineKeyboardButton(text=button_view.TO_MAIN_MENU, callback_data=button_callback.MAIN_MENU)
        ]
    ])
