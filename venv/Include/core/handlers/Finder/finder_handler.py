from aiogram import types
from config import dp,bot
from .messages import *
from aiogram.dispatcher import FSMContext
from Include.core.states import Finder


@dp.message_handler(lambda message: message.text and 'поиск пользователей' in message.text.lower())
async def finder(message: types.Message):
    finder_msg_withid = finder_msg + "\n\n" + "Ваш telegram_id - " + str(message.from_user.id)
    await bot.send_message(chat_id=message.from_user.id, text=finder_msg_withid, reply_markup=finder_btn)


@dp.callback_query_handler(lambda c: str(c.data).__eq__("finder_lastname"))
async def finder_lastname(callback_query: types.CallbackQuery):
    await Finder.WriteData.set()
    await bot.send_message(callback_query.from_user.id,find_lastname_txt)


@dp.message_handler(lambda message: message.text, state=Finder.WRITE_DATA, content_types=types.ContentTypes.TEXT)
async def last_name_finder(message: types.Message, state: FSMContext):
    print("")

