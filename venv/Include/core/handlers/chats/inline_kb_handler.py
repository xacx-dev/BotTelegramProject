from aiogram import types
from config import dp,bot
from .messages import *
from .chats import *


@dp.message_handler(lambda message: message.text and 'чаты' in message.text.lower())
async def chats(message: types.Message):
    with open('./news-1.jpg', 'rb') as photo:
        await bot.send_photo(chat_id=message.from_user.id, photo=photo,caption=chats_msg,reply_markup=chats2)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("chat"))
async def process_callback_authbtn(callback_query: types.CallbackQuery):
    chats_id = str(callback_query.data).split("_")
    kb = None
    try:
        kb = all_chats[int(chats_id[1])-1]
    except:
        pass
    text = all_chats_msg[int(chats_id[1]) - 1]
    await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id, caption=text,reply_markup=kb)

