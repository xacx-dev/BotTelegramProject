from aiogram import types
from config import dp,bot
from .messages import *
from Include.core.states import *
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
import time

@dp.callback_query_handler(text='userprofile_work')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,work_msg+"\n"+get_works_info(callback_query.from_user.id),reply_markup=works_btn)

@dp.callback_query_handler(text='go_back_work')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,reply_markup=works_btn)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("removework"))
async def status_project(callback_query: types.CallbackQuery):
    workid = str(callback_query.data).split("_")[1]
    deletework(callback_query.from_user.id,workid)

    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,text=work_deleted+"\n"+get_works_info(callback_query.from_user.id), reply_markup=works_btn)


@dp.callback_query_handler(text='remove_work')
async def id(callback_query: types.CallbackQuery):
    works_data = getworks(callback_query.from_user.id)
    id = 0
    btns = []
    for i in works_data:
        id += 1
        project_id = i["id"]
        tulist = ("Удалить работу #"+str(id), "removework_"+str(project_id))
        btns.append(tulist)
    tulist = ("Вернуться назад", "go_back_work")
    btns.append(tulist)
    btns_new = tg_helper.create_inline_markup(*reversed(btns), row_width=2)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,reply_markup=btns_new)

@dp.callback_query_handler(text='add_work')
async def add_project(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,work_text_1,reply_markup=None)
    await AddWork.Organization.set()

@dp.message_handler(lambda message: message.text, state=AddWork.Organization,content_types=types.ContentTypes.TEXT)
async def group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name']=message.text
        await bot.send_message(message.from_user.id, work_text_2)
        await AddWork.next()

@dp.message_handler(lambda message: message.text, state=AddWork.Status,content_types=types.ContentTypes.TEXT)
async def group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['status']=message.text
        await bot.send_message(message.from_user.id, work_text_3,reply_markup=state_work_btn)
        await AddWork.next()

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("workstatus"),state=AddWork.inWork)
async def status_project(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        status = str(callback_query.data).split("_")[1]
        if status == "finished":
            data['statuswork'] = 0
        elif status == "inprogress":
            data['statuswork'] = 1
        await bot.send_message(callback_query.from_user.id, work_text_4, reply_markup=None)
        await AddWork.next()

@dp.message_handler(lambda message: message.text, state=AddWork.dateStart,content_types=types.ContentTypes.TEXT)
async def startdate_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            splited = str(message.text).split("-")
            day = splited[2]
            month = splited[1]
            year = splited[0]
            date = year + "-" + month + "-" + day
            valid_date = time.strptime(date, '%Y-%m-%d')
            data['startdata'] = date
            if data['statuswork']:
                data['enddata'] = "1970-01-01"
                create_work_send(data,message)
                await state.finish()

            else:
                await bot.send_message(message.from_user.id, project_text_6)
                await AddWork.next()

        except (ValueError, IndexError):
            await bot.send_message(message.from_user.id, date_error)
            pass



def create_work_send(data,message):
    send_data = {
        "name": data['name'],
        "position": data['status'],
        "status": data['statuswork'],
        "startdate": data['startdata'],
        "enddate": data['enddata'],
        "telegram_id": message.from_user.id
    }
    creatework(message.from_user.id,send_data)