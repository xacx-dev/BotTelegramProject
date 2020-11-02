from aiogram import types
from config import dp,bot
from aiogram.dispatcher import FSMContext
from Include.core.states import UserProfileEdit
from Include.core.helpers import telegram as tg_helper
from Include.core.helpers.Utils import *
from .messages import *
from Include.core.handlers.registration.messages import *
import re

@dp.callback_query_handler(text='userprofile_edit',state="*")
async def process_callback_authbtn(callback_query: types.CallbackQuery):
    await UserProfileEdit.EDIT_LASTNAME.set()
    await bot.send_message(callback_query.from_user.id, last_name_txt+edit_addon)


@dp.message_handler(lambda message: message.text, state=UserProfileEdit.EDIT_LASTNAME,content_types=types.ContentTypes.TEXT)
async def last_name(message: types.Message, state: FSMContext):
    if not message.text == "0":
        requestsApi.update(message.from_user.id,"last_name",message.text)
    await bot.send_message(message.from_user.id, first_name_txt +edit_addon)
    await UserProfileEdit.next()

@dp.message_handler(lambda message: message.text, state=UserProfileEdit.EDIT_FIRSTNAME,content_types=types.ContentTypes.TEXT)
async def first_name(message: types.Message, state: FSMContext):
    if not message.text == "0":
        requestsApi.update(message.from_user.id,"first_name",message.text)

    groups_list = []
    groups = requestsApi.getgroups()
    for i in range(1, len(groups)):
        fond = groups[i]['fond']
        tulist = ("Участник проекта \"" + fond + "\"", "fond_" + fond)
        if tulist not in groups_list:
            groups_list.append(tulist)
    groups_list.append(("Наставник", "fond_mentor"))
    groups_list.append(("Сооснователь Фонда", "fond_cofounder"))
    groups_list.append(("Команда Фонда", "fond_team"))
    btns = tg_helper.create_inline_markup(*groups_list, row_width=1)
    await bot.send_message(message.from_user.id, group_text+edit_addon, reply_markup=btns)
    await UserProfileEdit.next()

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("fond"),state=UserProfileEdit.EDIT_GROUP)
async def group(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        fond = str(callback_query.data).split("_")[1]
        requestsApi.update(callback_query.from_user.id, "group", fond)
        await bot.send_message(callback_query.from_user.id, city_where + edit_addon,reply_markup=await get_btns_param(callback_query.from_user.id,'city'))
        await UserProfileEdit.next()

@dp.message_handler(lambda message: message.text, state=UserProfileEdit.EDIT_GROUP,content_types=types.ContentTypes.TEXT)
async def group(message: types.Message, state: FSMContext):
    if message.text == "0":
        await bot.send_message(message.from_user.id, city_where +edit_addon,reply_markup=await get_btns_param(message.from_user.id,'city'))
        await UserProfileEdit.next()


@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("fondcity"),state=UserProfileEdit.EDIT_CITY)
async def city(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        fond = str(callback_query.data).split("_")[1]
        requestsApi.update(callback_query.from_user.id, "city", fond)
        await bot.send_message(callback_query.from_user.id, year_join + edit_addon, reply_markup=await get_btns_param(callback_query.from_user.id,'year'))
        await UserProfileEdit.next()


@dp.message_handler(lambda message: message.text, state=UserProfileEdit.EDIT_CITY,
                    content_types=types.ContentTypes.TEXT)
async def city(message: types.Message, state: FSMContext):
    if message.text == "0":
        await bot.send_message(message.from_user.id, year_join + edit_addon,reply_markup=await get_btns_param(message.from_user.id,'year'))
        await UserProfileEdit.next()


@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("fondyear"),state=UserProfileEdit.EDIT_YEARENTER)
async def year(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        year = str(callback_query.data).split("_")[1]
        data['year'] = year
        await bot.send_message(callback_query.from_user.id, date_example+edit_addon)
        await UserProfileEdit.EDIT_DAYMONTHENTER.set()


@dp.message_handler(state=UserProfileEdit.EDIT_DAYMONTHENTER, content_types=types.ContentTypes.TEXT)
async def daymonthenter(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "0":
            userData = requestsApi.getUserData(message.from_user.id)['startdate']
            month = str(userData).split("-")[1]
            day = str(userData).split("-")[2]
            year = str(data['year'])
            date = year + "-" + month + "-" + day
            requestsApi.update(message.from_user.id, "startdate", date)
            await bot.send_message(message.from_user.id, email_text + edit_addon)
            await UserProfileEdit.EDIT_EMAIL.set()
            return
        try:
            day = str(message.text).split("-")[0]
            month = str(message.text).split("-")[1]
            year = str(data['year'])
            date = year+"-"+month+"-"+day
            valid_date = time.strptime(date, '%Y-%m-%d')
            requestsApi.update(message.from_user.id,"startdate",date)
            await state_reg(message.from_user.id, data)
        except ValueError:
            await bot.send_message(message.from_user.id, date_error)

@dp.message_handler(lambda message: message.text, state=UserProfileEdit.EDIT_YEARENTER,
                    content_types=types.ContentTypes.TEXT)
async def year(message: types.Message, state: FSMContext):
    if message.text == "0":
        await bot.send_message(message.from_user.id, email_text + edit_addon)
        await UserProfileEdit.EDIT_EMAIL.set()

@dp.message_handler(state=UserProfileEdit.EDIT_EMAIL, content_types=types.ContentTypes.TEXT)
async def email_check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "0":
            await bot.send_message(message.from_user.id, vk_text + edit_addon)
            await UserProfileEdit.next()
            return
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, message.text)):
            requestsApi.update(message.from_user.id, "email", message.text)
            await bot.send_message(message.from_user.id, vk_text + edit_addon)
            await UserProfileEdit.next()
        else:
            await bot.send_message(message.from_user.id, email_error)

@dp.message_handler(state=UserProfileEdit.EDIT_VK, content_types=types.ContentTypes.TEXT)
async def vk(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "0":
            await bot.send_message(message.from_user.id, fb_text + edit_addon)
            await UserProfileEdit.next()
            return
        if str(message.text).lower()  == "нет":
            requestsApi.update(message.from_user.id, "vk", message.text)
            await bot.send_message(message.from_user.id, fb_text + edit_addon)
            await UserProfileEdit.next()
        elif (requestsApi.check_vk_url(message.text)) and str(message.text).__contains__("/"):
            requestsApi.update(message.from_user.id, "vk", message.text)
            await bot.send_message(message.from_user.id, fb_text + edit_addon)
            await UserProfileEdit.next()
        else:
            await bot.send_message(message.from_user.id, vk_error)

@dp.message_handler(state=UserProfileEdit.EDIT_FB, content_types=types.ContentTypes.TEXT)
async def fb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "0":
            await bot.send_message(message.from_user.id, telnum_text + edit_addon)
            await UserProfileEdit.next()
            return
        if str(message.text).lower()  == "нет":
            requestsApi.update(message.from_user.id, "fb", message.text)
            await bot.send_message(message.from_user.id, telnum_text + edit_addon)
            await UserProfileEdit.next()
        elif (requestsApi.check_vk_url(message.text)) and str(message.text).__contains__("/"):
            requestsApi.update(message.from_user.id, "fb", message.text)
            await bot.send_message(message.from_user.id, telnum_text + edit_addon)
            await UserProfileEdit.next()
        else:
            await bot.send_message(message.from_user.id, vk_error)


@dp.message_handler(state=UserProfileEdit.EDIT_TEL, content_types=types.ContentTypes.TEXT)
async def telephone_check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "0":
            await bot.send_message(message.from_user.id, birthday_text + edit_addon)
            await UserProfileEdit.next()
            return
        pattern = re.compile("^[\dA-Z]{1}-[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
        if(pattern.match(message.text)):
            requestsApi.update(message.from_user.id, "telnum", message.text)
            await bot.send_message(message.from_user.id, birthday_text + edit_addon)
            await UserProfileEdit.next()
        else:
            await bot.send_message(message.from_user.id, telnum_error)

@dp.message_handler(state=UserProfileEdit.EDIT_BITRH, content_types=types.ContentTypes.TEXT)
async def birthday_check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "0":
            await bot.send_message(message.from_user.id, photo_text + edit_addon)
            await UserProfileEdit.next()
            return
        try:
            day = str(message.text).split("-")[0]
            month = str(message.text).split("-")[1]
            year = str(message.text).split("-")[2]
            date = year+"-"+month+"-"+day
            valid_date = time.strptime(date, '%Y-%m-%d')
            requestsApi.update(message.from_user.id,"birthday",date)
            await bot.send_message(message.from_user.id, photo_text + edit_addon)
            await UserProfileEdit.next()
        except ValueError:
            await bot.send_message(message.from_user.id, date_error)

@dp.message_handler(state=UserProfileEdit.EDIT_PHOTO, content_types=['photo'])
async def reg_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        remove_old_photo(message.from_user.id)
        photo_id = message.photo[1].file_id
        file = await bot.get_file(photo_id)
        file_path = file.file_path
        await bot.download_file(file_path, "./core/media/photo/"+str(message.from_user.id)+"__"+str(photo_id)+".png")
        await state.finish()
        await bot.send_message(message.from_user.id,edit_finish,reply_markup=MAIN_KB)

@dp.message_handler(lambda message: message.text, state=UserProfileEdit.EDIT_PHOTO,
                    content_types=types.ContentTypes.TEXT)
async def year(message: types.Message, state: FSMContext):
    if message.text == "0":
        await state.finish()
        await bot.send_message(message.from_user.id, edit_finish, reply_markup=MAIN_KB)

async def get_btns_param(tgid,param):
    userData = requestsApi.getUserData(tgid)
    curgroup = userData['group']
    data_list = []

    groups = requestsApi.getgroups()
    for i in range(1, len(groups)):
        if curgroup == groups[i]['fond'] or curgroup == "mentor" or curgroup == "cofounder" or curgroup == "team":
            parametr = groups[i][param]
            tulist = (parametr, "fond"+param+"_" + parametr)
            if tulist not in data_list:
                data_list.append(tulist)
    btns = tg_helper.create_inline_markup(*reversed(data_list), row_width=2)
    return btns


