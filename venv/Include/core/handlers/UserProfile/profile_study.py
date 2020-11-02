from aiogram import types
from config import dp,bot
from .messages import *
from Include.core.states import *
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
import time

@dp.callback_query_handler(text='userprofile_study')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,study_msg+"\n"+get_study_info(callback_query.from_user.id),reply_markup=study_btn)

@dp.callback_query_handler(text='go_back_study')
async def userprofile_project(callback_query: types.CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,reply_markup=study_btn)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("removestudy"))
async def status_project(callback_query: types.CallbackQuery):
    studyid = str(callback_query.data).split("_")[1]
    deletestudy(callback_query.from_user.id,studyid)

    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,text=study_deleted+"\n"+get_study_info(callback_query.from_user.id), reply_markup=study_btn)

@dp.callback_query_handler(text='remove_study')
async def id(callback_query: types.CallbackQuery):
    study_data = getstudy(callback_query.from_user.id)
    id = 0
    btns = []
    for i in study_data:
        id += 1
        project_id = i["id"]
        tulist = ("Удалить учебу #"+str(id), "removestudy_"+str(project_id))
        btns.append(tulist)
    tulist = ("Вернуться назад", "go_back_study")
    btns.append(tulist)
    btns_new = tg_helper.create_inline_markup(*reversed(btns), row_width=2)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,message_id=callback_query.message.message_id,reply_markup=btns_new)



@dp.callback_query_handler(text='add_study')
async def add_project(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id,study_text_1,reply_markup=type_study_btn)
    await AddStudy.TypeStudy.set()

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("typestudy"),state=AddStudy.TypeStudy)
async def status_project(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        typestudy = str(callback_query.data).split("_")[1]
        data['type'] = typestudy
        await bot.send_message(callback_query.from_user.id, study_text_2, reply_markup=None)
        await AddStudy.next()

@dp.message_handler(lambda message: message.text, state=AddStudy.Location,content_types=types.ContentTypes.TEXT)
async def group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['location']=message.text
        await bot.send_message(message.from_user.id, study_text_3,reply_markup=state_study_btn)
        await AddStudy.next()

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("studystatus"),state=AddStudy.progress)
async def status_project(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        status = str(callback_query.data).split("_")[1]
        if status == "inprogress":
            data['statusstady'] = 0
            data['progress_stage'] = 0
            if data['type'] == "sch":
                await bot.send_message(callback_query.from_user.id, study_text_4)
                await AddStudy.progress_stage.set()
            else:
                await bot.send_message(callback_query.from_user.id, study_text_5)
                await AddStudy.progress_stage.set()
        elif status == "finished":
            data['statusstady'] = 1
            if data['type'] == "sch":
                await bot.send_message(callback_query.from_user.id, study_text_4)
                await AddStudy.progress_stage.set()
            else:
                await bot.send_message(callback_query.from_user.id, study_text_6)
                await AddStudy.Specialty.set()



@dp.message_handler(lambda message: str(message.text).isdigit(), state=AddStudy.progress_stage,content_types=types.ContentTypes.TEXT)
async def group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        stage = int(message.text)
        data['progress_stage'] = stage
        if data['type'] == "sch":
            if stage > 7 and stage < 12:
                data['speciality'] = ""
                await state.finish()
                create_study_send(data,message)
                await bot.send_message(message.from_user.id, study_added+"\n"+get_study_info(message.from_user.id),reply_markup=study_btn)
            else:
                await bot.send_message(message.from_user.id,study_error_sch)
        else:
            if stage > 0 and stage < 8:
                await bot.send_message(message.from_user.id, study_text_6,reply_markup=None)
                await AddStudy.Specialty.set()
            else:
                await bot.send_message(message.from_user.id,study_error_vuz)

@dp.message_handler(lambda message: message.text, state=AddStudy.Specialty,content_types=types.ContentTypes.TEXT)
async def group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['speciality']=message.text
        await state.finish()
        create_study_send(data, message)
        await bot.send_message(message.from_user.id, study_added + "\n" + get_study_info(message.from_user.id),
                               reply_markup=study_btn)


def create_study_send(data,message):
    send_data = {
        "type": data['type'],
        "name": data['location'],
        "status": data['statusstady'],
        "step": data['progress_stage'],
        "speciality": data['speciality'],
        "telegram_id": message.from_user.id
    }
    createstudy(message.from_user.id,send_data)