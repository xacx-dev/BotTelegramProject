from aiogram import types
from config import dp,bot
from .messages import *
from Include.core.states import *
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
import time

@dp.callback_query_handler(text='userprofile_hobby')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,hobby_msg+"\n"+get_hobby_info(callback_query.from_user.id),reply_markup=hobby_btn)

@dp.callback_query_handler(text='go_back_hobby')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                text=get_hobby_info(callback_query.from_user.id),
                                message_id=callback_query.message.message_id,reply_markup=hobby_btn)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("removehobby"))
async def status_project(callback_query: types.CallbackQuery):
    hobby = str(callback_query.data).split("_")[1]
    deletehobby(callback_query.from_user.id,hobby)

    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                text=hobby_text_3+"\n"+get_hobby_info(callback_query.from_user.id),
                                message_id=callback_query.message.message_id,reply_markup=hobby_btn)


@dp.callback_query_handler(text='add_hobby')
async def add_project(callback_query: types.CallbackQuery):

    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=hobby_text_1+"\n"+get_hobby_info(callback_query.from_user.id)
                                    ,reply_markup=get_hobbyes_btn(callback_query.from_user.id))

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("addhobby"))
async def add_project(callback_query: types.CallbackQuery):
    hobby = str(callback_query.data).split("_")[1]
    addhobby(callback_query.from_user.id,hobby)
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text=hobby_text_4+"\n"+hobby_text_1+"\n"+get_hobby_info(callback_query.from_user.id),
                                reply_markup=get_hobbyes_btn(callback_query.from_user.id))


@dp.callback_query_handler(text='remove_hobby')
async def id(callback_query: types.CallbackQuery):
    hobby_data = gethobby(callback_query.from_user.id)
    id = 0
    btns = []
    for i in hobby_data:
        id += 1
        project_id = i["id"]
        tulist = ("Удалить интерес #"+str(id), "removehobby_"+str(project_id))
        btns.append(tulist)
    tulist = ("Вернуться назад", "go_back_hobby")
    btns.append(tulist)
    btns_new = tg_helper.create_inline_markup(*reversed(btns), row_width=2)
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text=hobby_text_2 + "\n" + get_hobby_info(callback_query.from_user.id),
                                reply_markup=btns_new)

def get_hobbyes_btn(tgid):
    hobbyes = get_hobby_or_competence('hobby')
    hobby_user = gethobby(tgid)
    id = 0
    btns = []

    tips = []
    for user_hobby in hobby_user:
        hashtag = user_hobby['hashtag']
        if not tips.__contains__(hashtag):
            tips.append(hashtag)

    for hobby in hobbyes:
        id += 1
        if not tips.__contains__(hobby['tip']):
            tulist = ("#"+str(hobby['tip']), "addhobby_" + str(hobby['tip']))
            btns.append(tulist)
    tulist = ("Вернуться назад", "go_back_hobby")
    btns.append(tulist)
    btns_new = tg_helper.create_inline_markup(*btns)
    return btns_new