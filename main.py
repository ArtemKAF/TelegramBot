from aiogram import Bot, Dispatcher, executor, types
import requests as requests
from tbconfig import TOKEN_API


URL = 'https://api.telegram.org/bot'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = '''
/help - список команд
/description - просмотреть описание бота
/start - начало работы с ботом
'''


def send_photo_file(chat_id, img):
    files = {'photo': open(img, 'rb')}
    requests.post(f'{URL}{TOKEN_API}/sendPhoto?chat_id={chat_id}', files=files)


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text='Здесь будет описание моей миссии ;)')
    await message.delete()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Привет, {message.from_user.first_name}! Предлагаю поиграть.',
    )
    send_photo_file(message.chat.id, './cards/animals/cat.jpg')
    await bot.send_message(
        message.chat.id,
        text='Как это называется на английском?'
    )
    await message.delete()


@dp.message_handler()
async def echo(message: types.message):
    await message.reply(text='Я Вас не понимаю. :(')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
