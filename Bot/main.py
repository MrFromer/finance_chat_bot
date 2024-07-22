import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN_API
from app.handlers import router


dp = Dispatcher()
bot = Bot(token=TOKEN_API, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

async def startup(_):
    #await db_start() #подключение в бд
    print('Бот был успешно запущен')


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True, on_startup=startup)

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')


# from aiogram import Bot, Dispatcher, executor, types
# from Bot.config import TOKEN_API

# bot = Bot(TOKEN_API)
# dp  = Dispatcher(bot)

# async def startup(_):
#     #await db_start() #подключение в бд
#     print('Бот был успешно запущен')

# if __name__ == '__main__':
#     executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=startup)