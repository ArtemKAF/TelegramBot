from aiogram import Bot, Dispatcher, executor, types
from tbconfig import TOKEN_API


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = '''
/help - список команд
/description - просмотреть описание бота
/start - начало работы с ботом
'''


@dp.message_handler(commands=['help'])
async def help_command(message: types.message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()

@dp.message_handler(commands=['description'])
async def help_command(message: types.message):
    await message.answer(text='Здесь будет описание моей миссии ;)')
    await message.delete()

@dp.message_handler(commands=['start'])
async def help_command(message: types.message):
    await message.answer(text=f'Здравствуйте, {message.text}! '
                               'Предлагаю Вам начать игру.')
    await message.delete()


@dp.message_handler()
async def echo(message: types.message):
    await message.reply(text='Я Вас не понимаю. :(')


if __name__ == '__main__':
    executor.start_polling(dp)