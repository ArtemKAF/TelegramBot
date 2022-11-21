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
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()


@dp.message_handler(commands=['description'])
async def help_command(message: types.Message):
    await message.answer(text='Здесь будет описание моей миссии ;)')
    await message.delete()


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Привет, {message.from_user.first_name}! Предлагаю поиграть.',
        parse_mode='HTML',
    )
    await bot.send_photo(
        chat_id=message.chat.id,
        photo='https://kids-flashcards.com/images/ru/1/large/picture-flashcard/%D0%BA%D0%BE%D1%82.jpg',
        caption='Как это называется на английском?',
    )
    await message.delete()


@dp.message_handler()
async def echo(message: types.message):
    await message.reply(text='Я Вас не понимаю. :(')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
