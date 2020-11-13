from aiogram import types
from config import dp,bot
from .messages import *
from aiogram.dispatcher import FSMContext
from Include.core.states import Finder
from Include.core.handlers.UserProfile.messages import *

@dp.message_handler(lambda message: message.text and 'поиск пользователей' in message.text.lower())
async def finder(message: types.Message):
    finder_msg_withid = finder_msg + "\n\n" + "Ваш telegram_id - " + str(message.from_user.id)
    await bot.send_message(chat_id=message.from_user.id, text=finder_msg_withid, reply_markup=finder_btn)

@dp.callback_query_handler(lambda c: str(c.data).__eq__("finder_lastname"))
async def finder_lastname(callback_query: types.CallbackQuery):
    await Finder.WRITE_DATA.set()
    await bot.send_message(callback_query.from_user.id,find_lastname_txt)

@dp.callback_query_handler(lambda c: str(c.data).__eq__("finder_vk"))
async def finder_lastname(callback_query: types.CallbackQuery):
    await Finder.WRITE_DATA.set()
    await bot.send_message(callback_query.from_user.id,find_vk_text)

@dp.callback_query_handler(lambda c: str(c.data).__eq__("finder_fb"))
async def finder_lastname(callback_query: types.CallbackQuery):
    await Finder.WRITE_DATA.set()
    await bot.send_message(callback_query.from_user.id,find_fb_text)

@dp.callback_query_handler(lambda c: str(c.data).__eq__("finder_tg"))
async def finder_lastname(callback_query: types.CallbackQuery):
    await Finder.WRITE_DATA.set()
    await bot.send_message(callback_query.from_user.id,find_telegramid_text)

@dp.callback_query_handler(lambda c: str(c.data).__eq__("finder_hobby"))
async def finder_lastname(callback_query: types.CallbackQuery):
    #await Finder.WRITE_DATA.set()
    await bot.send_message(callback_query.from_user.id,find_hobbyes_text+"not work")

@dp.callback_query_handler(lambda c: str(c.data).__eq__("finder_competence"))
async def finder_lastname(callback_query: types.CallbackQuery):
    #await Finder.WRITE_DATA.set()
    await bot.send_message(callback_query.from_user.id,find_competences_text+"not work")



@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("findusereducation"))
async def findusereducation(callback_query: types.CallbackQuery):
    tgid = int(str(callback_query.data).split("_")[1])
    await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                             caption=study_msg_info+"\n"+get_study_info(tgid),reply_markup=back_btn(tgid))

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("finduserprojects"))
async def finduserprojects(callback_query: types.CallbackQuery):
    tgid = int(str(callback_query.data).split("_")[1])
    await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                             caption=project_msg_info+"\n"+get_project_info(tgid),reply_markup=back_btn(tgid))

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("finduserwork"))
async def finduserwork(callback_query: types.CallbackQuery):
    tgid = int(str(callback_query.data).split("_")[1])
    await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                             caption=work_msg_info+"\n"+get_works_info(tgid),reply_markup=back_btn(tgid))

def back_btn(tgid):
    btn = [("Назад","backtouserfind_"+str(tgid))]
    finish_btn = tg_helper.create_inline_markup(*btn, row_width=1)
    return finish_btn


@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("backtouserfind"))
async def backtouser(callback_query: types.CallbackQuery):
    tgid = int(str(callback_query.data).split("_")[1])
    photo_id = get_photo_id(tgid)
    data = main_data(tgid)
    if photo_id:
        await bot.edit_message_caption(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,
                                           caption=data,reply_markup=btns_users(tgid))




