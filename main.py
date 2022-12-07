import asyncio
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import Command
from core.handlers.basics import *
from tbconfig import TOKEN_API


async def main():
    bot = Bot(TOKEN_API)
    dp = Dispatcher(bot)
    dp.message_handlers.register(help_command, Command(commands=['help']))
    dp.message_handlers.register(description_command, Command(commands=['description']))
    dp.message_handlers.register(start_command, Command(commands=['start']))
    dp.message_handlers.register(echo)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
