from aiogram import types
from config import dp,bot
from .messages import *
from Include.core.states import *
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
import time

@dp.callback_query_handler(text='userprofile_competence')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,competence_msg+"\n"+get_competence_info(callback_query.from_user.id),reply_markup=competence_btn)

@dp.callback_query_handler(text='go_back_competence')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                text=get_competence_info(callback_query.from_user.id),
                                message_id=callback_query.message.message_id,reply_markup=competence_btn)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("removecompetence"))
async def status_project(callback_query: types.CallbackQuery):
    competence = str(callback_query.data).split("_")[1]
    deletecompetences(callback_query.from_user.id,competence)

    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                text=competence_text_3+"\n"+get_competence_info(callback_query.from_user.id),
                                message_id=callback_query.message.message_id,reply_markup=competence_btn)


@dp.callback_query_handler(text='add_competence')
async def add_project(callback_query: types.CallbackQuery):

    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=competence_text_1+"\n"+get_competence_info(callback_query.from_user.id)
                                    ,reply_markup=get_competence_btn(callback_query.from_user.id))

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("addcompetence"))
async def add_project(callback_query: types.CallbackQuery):
    competence = str(callback_query.data).split("_")[1]
    addcompetences(callback_query.from_user.id,competence)
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text=competence_text_4+"\n"+competence_text_1+"\n"+get_competence_info(callback_query.from_user.id),
                                reply_markup=get_competence_btn(callback_query.from_user.id))


@dp.callback_query_handler(text='remove_competence')
async def id(callback_query: types.CallbackQuery):
    competence_data = getcompetences(callback_query.from_user.id)
    id = 0
    btns = []
    for i in competence_data:
        id += 1
        project_id = i["id"]
        tulist = ("Удалить компетенцию #"+str(id), "removecompetence_"+str(project_id))
        btns.append(tulist)
    tulist = ("Вернуться назад", "go_back_competence")
    btns.append(tulist)
    btns_new = tg_helper.create_inline_markup(*reversed(btns), row_width=2)
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text=competence_text_2 + "\n" + get_competence_info(callback_query.from_user.id),
                                reply_markup=btns_new)

def get_competence_btn(tgid):
    competences = get_hobby_or_competence('competence')
    competences_user = getcompetences(tgid)
    id = 0
    btns = []

    tips = []
    for user_competence in competences_user:
        hashtag = user_competence['hashtag']
        if not tips.__contains__(hashtag):
            tips.append(hashtag)

    for competence in competences:
        id += 1
        if not tips.__contains__(competence['tip']):
            tulist = ("#"+str(competence['tip']), "addcompetence_" + str(competence['tip']))
            btns.append(tulist)
    tulist = ("Вернуться назад", "go_back_competence")
    btns.append(tulist)
    btns_new = tg_helper.create_inline_markup(*btns)
    return btns_new