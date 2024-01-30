import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InputFile
from aiogram.utils.markdown import hbold
from ikb import ikb

from config import TOKEN

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer_photo(photo=types.FSInputFile(path='image/test.jpg'),
                               caption=f"Привіт, {hbold(message.from_user.full_name)}!\n"
                                       f"Я Jarkey, допоможу виготовити дублікати ключів",
                               reply_markup=ikb)



# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


async def main() -> None:
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
