from aiogram import types
from config import dp,bot,req_url
from Include.core.helpers import requestsApi
from Include.core.helpers.Utils import *
from .messages import *
from Include.core.handlers.UserProfile.messages import *



@dp.message_handler()
async def process_chat_command(message: types.Message):
    message.text = str(message.text).lower()
    print(message.text)

    if message.text == "чаты":
        with open('./news-1.jpg', 'rb') as photo:
            print(photo)
            await bot.send_photo(chat_id=message.from_user.id, photo=photo,caption=chats_msg,reply_markup=chats2)
    elif message.text == "база пользователей":
        message.reply("В разработке")
    elif message.text == "поиск пользователей":
        finder_msg_withid = finder_msg +"\n\n"+"Ваш telegram_id - "+str(message.from_user.id)
        await bot.send_message(chat_id=message.from_user.id, text=finder_msg_withid,reply_markup=finder_btn)
    elif message.text == "моё досье":
        photo_id = get_photo_id(message.from_user.id)
        data = main_data(message.from_user.id)
        if photo_id:
            await bot.send_photo(chat_id=message.from_user.id, photo=photo_id,caption=user_profile_text+"\n\n"+data,reply_markup=user_profile_btn)

    elif message.text == "мои мероприятия":
        message.reply("В разработке")


