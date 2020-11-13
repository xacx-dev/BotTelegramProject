from aiogram import types
from config import dp,bot
from .messages import *
from aiogram.dispatcher import FSMContext
from Include.core.states import Finder
from Include.core.helpers import requestsApi
from Include.core.handlers.UserProfile.messages import *

@dp.callback_query_handler(text='tomainfind',state="*")
async def process_callback_authbtn(callback_query: types.CallbackQuery):
    finder_msg_withid = finder_msg + "\n\n" + "Ваш telegram_id - " + str(callback_query.from_user.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=finder_msg_withid, reply_markup=finder_btn)

@dp.message_handler(lambda message: message.text, state=Finder.WRITE_DATA, content_types=types.ContentTypes.TEXT)
async def last_name_finder(message: types.Message, state: FSMContext):
    message.text = str(message.text).lower().title()
    if message.text == "Нет":
        await bot.send_message(chat_id=message.from_user.id, text=find_cancled+"\n\n"+ "Ваш telegram_id - " + str(message.from_user.id), reply_markup=finder_btn)
        await state.finish()
        return
    try:
        data = requestsApi.find_user_lastname(message.text)
        if data:
            photo_id = get_photo_id(data[0]['telegram_id'])
            data_text = main_data(data[0]['telegram_id'])

            if photo_id:
                await bot.send_photo(chat_id=message.from_user.id, photo=photo_id, caption=user_profile_text + "\n\n" + data_text,
                                     reply_markup=btns_users(data[0]['telegram_id']))
                await state.finish()
        else:
            await bot.send_message(chat_id=message.from_user.id,text=user_not_found,reply_markup=finder_btn)
            await state.finish()
    except TypeError:
        await bot.send_message(message.from_user.id,other_err)



