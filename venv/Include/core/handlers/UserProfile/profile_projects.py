from aiogram import types
from config import dp,bot
from .messages import *
from Include.core.states import *
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
import time

@dp.callback_query_handler(text='userprofile_project')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,project_msg+"\n"+get_project_info(callback_query.from_user.id),reply_markup=projects_btn)

@dp.callback_query_handler(text='go_back_projects')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,reply_markup=projects_btn)


@dp.callback_query_handler(text='remove_project')
async def id(callback_query: types.CallbackQuery):
    projects_data = getprojects(callback_query.from_user.id)
    id = 0
    btns = []
    for i in projects_data:
        id += 1
        project_id = i["id"]
        tulist = ("Удалить проект #"+str(id), "removeprojct_"+str(project_id))
        btns.append(tulist)
    tulist = ("Вернуться назад", "go_back_projects")
    btns.append(tulist)
    btns_new = tg_helper.create_inline_markup(*reversed(btns), row_width=2)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,reply_markup=btns_new)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("removeprojct"))
async def status_project(callback_query: types.CallbackQuery):
    projectid = str(callback_query.data).split("_")[1]
    deleteproject(callback_query.from_user.id,projectid)

    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,text=project_deleted+"\n"+get_project_info(callback_query.from_user.id), reply_markup=projects_btn)


@dp.callback_query_handler(text='add_project')
async def add_project(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,project_text_1,reply_markup=None)
    await AddProject.Name.set()


@dp.message_handler(lambda message: message.text, state=AddProject.Name,content_types=types.ContentTypes.TEXT)
async def name_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await bot.send_message(message.from_user.id, project_text_2)
        await AddProject.next()

@dp.message_handler(lambda message: message.text, state=AddProject.Info,content_types=types.ContentTypes.TEXT)
async def info_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['info'] = message.text
        await bot.send_message(message.from_user.id, project_text_3, reply_markup=state_project_btn)
        await AddProject.next()

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("projectstatus"),state=AddProject.Status)
async def status_project(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        status = str(callback_query.data).split("_")[1]
        if status == "finished":
            data['status'] = 1
        elif status == "inprogress":
            data['status'] = 0
        await bot.send_message(callback_query.from_user.id, project_text_4, reply_markup=None)
        await AddProject.next()

@dp.message_handler(lambda message: message.text, state=AddProject.datestart,content_types=types.ContentTypes.TEXT)
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
            await bot.send_message(message.from_user.id, project_text_5)
            await AddProject.next()
        except (ValueError, IndexError):
            await bot.send_message(message.from_user.id, date_error)
            pass


@dp.message_handler(lambda message: message.text, state=AddProject.datefinish,content_types=types.ContentTypes.TEXT)
async def finishdate_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            splited = str(message.text).split("-")
            day = splited[2]
            month = splited[1]
            year = splited[0]
            date = year + "-" + month + "-" + day
            valid_date = time.strptime(date, '%Y-%m-%d')
            data['enddata'] = date
            await bot.send_message(message.from_user.id, project_text_6, reply_markup=grant_project_btn)
            await AddProject.next()
        except (ValueError, IndexError):
            await bot.send_message(message.from_user.id, date_error)
            pass


@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("projectgrant"),state=AddProject.hasGrant)
async def status_project(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        hasgrant = str(callback_query.data).split("_")[1]

        if(hasgrant == "yes"):
            data['hasGrant'] = 1
            await AddProject.ifhasGrant.set()
            await bot.send_message(callback_query.from_user.id, project_text_7, reply_markup=None)
        elif hasgrant=="no":
            data['hasGrant'] = 0
            data['grantinfo'] = ""
            await AddProject.statusInvestetion.set()
            await bot.send_message(callback_query.from_user.id, project_text_8, reply_markup=invest_btn)


@dp.message_handler(lambda message: message.text, state=AddProject.ifhasGrant,content_types=types.ContentTypes.TEXT)
async def finishdate_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['grantinfo'] = message.text
        await AddProject.statusInvestetion.set()
        await bot.send_message(callback_query.from_user.id, project_text_8, reply_markup=invest_btn)


@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("projectinvestition"),state=AddProject.statusInvestetion)
async def status_project(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        hasinvestitions = str(callback_query.data).split("_")[1]

        if(hasinvestitions == "yes"):
            data['investitions'] = 1
            await AddProject.InvestetionInfo.set()
            await bot.send_message(callback_query.from_user.id, project_text_9, reply_markup=None)
        elif hasinvestitions=="no":
            data['investitions'] = 0
            data['investitionsinfo'] = 0
            create_project_send(data, callback_query)
            await bot.send_message(callback_query.from_user.id, project_text_10+"\n"+project_msg+"\n"+get_project_info(callback_query.from_user.id), reply_markup=projects_btn)


@dp.message_handler(lambda message: str(message.text).isdigit(), state=AddProject.InvestetionInfo,content_types=types.ContentTypes.TEXT)
async def finishdate_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['investitionsinfo'] = message.text
        create_project_send(data,message)
        await bot.send_message(message.from_user.id, project_text_10+"\n"+project_msg+"\n"+get_project_info(message.from_user.id), reply_markup=projects_btn)


def create_project_send(data,message):
    send_data = {
        "name": data['name'],
        "description": data['info'],
        "status": data['status'],
        "startdate": data['startdata'],
        "enddate": data['enddata'],
        "is_investment_status_accept": data['hasGrant'],
        "investor": data['grantinfo'],
        "is_invest_need": data['investitions'],
        "investneedsum": data['investitionsinfo'],
        "telegram_id": message.from_user.id
    }
    createproject(message.from_user.id,send_data)