from aiogram import types
from config import dp,bot
from .messages import *
from aiogram.dispatcher import FSMContext
from Include.core.states import Finder

@dp.callback_query_handler(lambda c: str(c.data).__eq__("finder_lastname"))
async def finder_lastname(callback_query: types.CallbackQuery):
    await Finder.WriteData.set()
    await bot.send_message(callback_query.from_user.id,find_lastname_txt)


@dp.message_handler(lambda message: message.text, state=Finder.WRITE_DATA, content_types=types.ContentTypes.TEXT)
async def last_name_finder(message: types.Message, state: FSMContext):
    print("")

