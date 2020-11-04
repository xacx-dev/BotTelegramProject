from aiogram import types
from config import dp,bot
from .messages import *


@dp.message_handler(lambda message: message.text and 'моё досье' in message.text.lower())
async def my_data(message: types.Message):
    photo_id = get_photo_id(message.from_user.id)
    data = main_data(message.from_user.id)
    if photo_id:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo_id, caption=user_profile_text + "\n\n" + data,
                             reply_markup=user_profile_btn)


@dp.callback_query_handler(text='back')
async def userprofile_project(callback_query: types.CallbackQuery):
    photo_id = get_photo_id(callback_query.from_user.id)
    data = main_data(callback_query.from_user.id)
    if photo_id:
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_id, caption=user_profile_text + "\n\n" + data,
                             reply_markup=user_profile_btn)

