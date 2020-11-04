from aiogram import types
from config import dp,bot
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
from .messages import *




@dp.message_handler(lambda message: message.text and 'мои мероприятия' in message.text.lower())
async def base_main(message: types.Message):
    await message.reply("В разработке")