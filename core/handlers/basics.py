from aiogram.types import Message, InputFile
from tbconfig import HELP_COMMAND


async def help_command(message: Message):
    await message.answer(text=HELP_COMMAND)
    await message.delete()


async def description_command(message: Message):
    await message.answer(text='Здесь будет описание моей миссии ;)')
    await message.delete()


async def start_command(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.first_name}! Предлагаю поиграть.',
    )
    photo = InputFile(path_or_bytesio='./cards/animals/cat.jpg')
    await message.answer_photo(
        photo=photo,
        caption="Как это называется на английском?"
    )
    await message.delete()


async def echo(message: Message):
    await message.reply(text='Я Вас не понимаю. :(')
