import os
from aiogram import Bot, Dispatcher, executor, types
from tbconfig import TOKEN_API, HELP_COMMAND


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


file_list = os.listdir('./cards')
print(file_list)


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
    photo = types.InputFile(path_or_bytesio='./cards/animals/cat.jpg')
    await bot.send_photo(message.chat.id, photo=photo, caption="Как это называется на английском?")
    await message.delete()


@dp.message_handler()
async def echo(message: types.message):
    await message.reply(text='Я Вас не понимаю. :(')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
