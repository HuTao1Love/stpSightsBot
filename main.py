from loader import bot
import asyncio
from handlers import *


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("START")
    asyncio.run(main())
