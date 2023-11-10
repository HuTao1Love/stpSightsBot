from config import TOKEN
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher


bot = Bot(
    token=TOKEN,
    parse_mode=ParseMode.MARKDOWN,
    disable_web_page_preview=True,
)
dp = Dispatcher()
