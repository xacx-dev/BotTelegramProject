from aiogram import types
from config import dp,bot
from .messages import *
from Include.core.states import Registration

@dp.callback_query_handler(text='yes_reg',state="*")
async def process_callback_authbtn(callback_query: types.CallbackQuery):
    #await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Введите пароль")
    await Registration.REG_PASS.set()

