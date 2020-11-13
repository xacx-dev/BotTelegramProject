from aiogram import types
from config import dp,bot
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
from Include.core.handlers.UserProfile.messages import *
from .messages import *


@dp.callback_query_handler(text='tomain',state="*")
async def process_callback_authbtn(callback_query: types.CallbackQuery):
    photo_id = get_photo_id(callback_query.from_user.id)
    data = main_data(callback_query.from_user.id)
    if photo_id:
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_id, caption=user_profile_text + "\n\n" + data,
                             reply_markup=user_profile_btn)

@dp.message_handler(lambda message: message.text and 'база пользователей' in message.text.lower())
async def base_main(message: types.Message):
    groups_list = []
    groups = requestsApi.getgroups()
    for i in range(0, len(groups)):
        fond = groups[i]['fond']
        tulist = ("Фонд \"" + fond + "\" "+groups[i]['year'], "basefond_" + fond+"_"+groups[i]['year'])
        if tulist not in groups_list:
            groups_list.append(tulist)
    btns = tg_helper.create_inline_markup(*groups_list, row_width=1)
    await bot.send_message(message.from_user.id, select_fond, reply_markup=btns)


@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("basefond"))
async def city(callback_query: types.CallbackQuery):
    selected_fond = str(callback_query.data).split("_")[1]
    year_fond = str(callback_query.data).split("_")[2]
    groups = requestsApi.getgroups()
    gpid=''
    for i in range(0, len(groups)):
        fond = groups[i]['fond']
        if fond == selected_fond and year_fond == groups[i]['year']:
            gpid = groups[i]['group_id']
    urs = requestsApi.getusers_in_group(gpid)
    if urs:
        photo_id = get_photo_id(urs[0]['telegram_id'])
        data = main_data(urs[0]['telegram_id'])
        if photo_id:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_id, caption=data,
                                 reply_markup=bnts_users(gpid,0))
    else:
        await bot.send_message(callback_query.from_user.id,groups_empty)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("gonext"))
async def gonext(callback_query: types.CallbackQuery):
    gpid = str(callback_query.data).split("_")[1]
    idinbd = int(str(callback_query.data).split("_")[2])
    urs = requestsApi.getusers_in_group(gpid)
    if urs:
        photo_id = get_photo_id(urs[idinbd]['telegram_id'])
        data = main_data(urs[idinbd]['telegram_id'])
        if photo_id:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_id, caption=data,
                                 reply_markup=bnts_users(gpid,idinbd))
    else:
        await bot.send_message(callback_query.from_user.id,groups_empty)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("goback"))
async def goback(callback_query: types.CallbackQuery):
    gpid = str(callback_query.data).split("_")[1]
    idinbd = int(str(callback_query.data).split("_")[2])
    urs = requestsApi.getusers_in_group(gpid)
    if urs:
        photo_id = get_photo_id(urs[idinbd]['telegram_id'])
        data = main_data(urs[idinbd]['telegram_id'])
        if photo_id:
            await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_id, caption=data,
                                 reply_markup=bnts_users(gpid,idinbd))
    else:
        await bot.send_message(callback_query.from_user.id,groups_empty)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("baseusereducation"))
async def baseusereducation(callback_query: types.CallbackQuery):
    gpid = str(callback_query.data).split("_")[3]
    idinbd = int(str(callback_query.data).split("_")[2])
    tgid = int(str(callback_query.data).split("_")[1])
    await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                             caption=study_msg_info+"\n"+get_study_info(tgid),reply_markup=back_btn(gpid,idinbd,tgid))

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("baseuserprojects"))
async def baseusereducation(callback_query: types.CallbackQuery):
    gpid = str(callback_query.data).split("_")[3]
    idinbd = int(str(callback_query.data).split("_")[2])
    tgid = int(str(callback_query.data).split("_")[1])
    await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                             caption=project_msg_info+"\n"+get_project_info(tgid),reply_markup=back_btn(gpid,idinbd,tgid))

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("baseuserwork"))
async def baseusereducation(callback_query: types.CallbackQuery):
    gpid = str(callback_query.data).split("_")[3]
    idinbd = int(str(callback_query.data).split("_")[2])
    tgid = int(str(callback_query.data).split("_")[1])
    await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                             caption=work_msg_info+"\n"+get_works_info(tgid),reply_markup=back_btn(gpid,idinbd,tgid))


def back_btn(gpid,id,tgid):
    btn = []
    btn.append(("Назад","backtouser_"+str(tgid)+"_"+str(id)+"_"+str(gpid)))
    finish_btn = tg_helper.create_inline_markup(*btn, row_width=1)
    return finish_btn

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("backtouser"))
async def backtouser(callback_query: types.CallbackQuery):
    gpid = str(callback_query.data).split("_")[3]
    id = int(str(callback_query.data).split("_")[2])
    tgid = int(str(callback_query.data).split("_")[1])
    urs = requestsApi.getusers_in_group(gpid)
    if urs:
        photo_id = get_photo_id(tgid)
        data = main_data(tgid)
        if photo_id:
            await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                                           caption=data,reply_markup=bnts_users(gpid,id))
    else:
        await bot.send_message(callback_query.from_user.id,groups_empty)


def bnts_users(gpid,id):
    users = requestsApi.getusers_in_group(gpid)
    btns = []
    btns.append(("Образование", "baseusereducation_" + str(users[id]['telegram_id'])+"_"+str(id)+"_"+str(gpid)))
    btns.append(("Проекты", "baseuserprojects_" + str(users[id]['telegram_id'])+"_"+str(id)+"_"+str(gpid)))
    btns.append(("Работа", "baseuserwork_" + str(users[id]['telegram_id'])+"_"+str(id)+"_"+str(gpid)))
    if len(users) == 1:
        btns.append(("На главную", "tomain"))
    elif len(users)>1 and id == 0:
        btns.append(("Вперед", "gonext_"+str(gpid)+"_"+str(id+1)))
        btns.append(("На главную", "tomain"))
    elif len(users) != (id+1):
        btns.append(("Вперед", "gonext_"+str(gpid)+"_"+str(id+1)))
        btns.append(("Назад", "goback_"+str(gpid)+"_"+str(id-1)))
        btns.append(("На главную", "tomain"))
    elif len(users) == (id+1):
        btns.append(("Назад", "goback_" + str(gpid) + "_" + str(id - 1)))
        btns.append(("На главную", "tomain"))
    finish_btns = tg_helper.create_inline_markup(*btns, row_width=2)
    return finish_btns
