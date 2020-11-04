from aiogram import types
from config import dp,bot,req_url
from aiogram.dispatcher import FSMContext
from Include.core.states import Registration, UserProfileEdit
from Include.core.helpers import requestsApi
from .CheckRegData import *
from .messages import *
import time
import re

@dp.callback_query_handler(text='yes_reg',state="*")
async def process_callback_authbtn(callback_query: types.CallbackQuery):
    #await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Введите пароль")
    await Registration.REG_PASS.set()




@dp.message_handler(lambda message: message.text, state=Registration.REG_LASTNAME,content_types=types.ContentTypes.TEXT)
async def last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        requestsApi.update(message.from_user.id,"last_name",message.text)
        await state_reg(message.from_user.id,data)



@dp.message_handler(state=Registration.REG_FIRSTNAME, content_types=types.ContentTypes.TEXT)
async def first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        requestsApi.update(message.from_user.id, "first_name", message.text)
        await state_reg(message.from_user.id, data)

@dp.message_handler(state=Registration.REG_DAYMONTHENTER, content_types=types.ContentTypes.TEXT)
async def daymonthenter(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
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

@dp.message_handler(state=Registration.REG_EMAIL, content_types=types.ContentTypes.TEXT)
async def email_check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, message.text)):
            requestsApi.update(message.from_user.id, "email", message.text)
            await state_reg(message.from_user.id, data)
        else:
            await bot.send_message(message.from_user.id, email_error)

@dp.message_handler(state=Registration.REG_VK, content_types=types.ContentTypes.TEXT)
async def vk(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if (requestsApi.check_vk_url(message.text)):
            requestsApi.update(message.from_user.id, "vk", message.text)
            await state_reg(message.from_user.id, data)
        elif message.text != "нет":
            requestsApi.update(message.from_user.id, "нет", message.text)
            await state_reg(message.from_user.id, data)
        else:
            await bot.send_message(message.from_user.id, vk_error)

@dp.message_handler(state=Registration.REG_FB, content_types=types.ContentTypes.TEXT)
async def fb(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        message.text = str(message.text).lower()
        if message.text == "нет":
            requestsApi.update(message.from_user.id, "fb", message.text)
            await state_reg(message.from_user.id, data)
        else:

            if str(message.text).__contains__("facebook.com/") and str(message.text).split("facebook.com/")[1]:
                requestsApi.update(message.from_user.id, "fb", message.text)
                await state_reg(message.from_user.id, data)
            else:
                await bot.send_message(message.from_user.id, fb_error)

@dp.message_handler(state=Registration.REG_TEL, content_types=types.ContentTypes.TEXT)
async def telephone_check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        pattern = re.compile("^[\dA-Z]{1}-[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
        if(pattern.match(message.text)):
            requestsApi.update(message.from_user.id, "telnum", message.text)
            await state_reg(message.from_user.id, data)
        else:
            await bot.send_message(message.from_user.id, telnum_error)

@dp.message_handler(state=Registration.REG_BITRH, content_types=types.ContentTypes.TEXT)
async def birthday_check(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            day = str(message.text).split("-")[0]
            month = str(message.text).split("-")[1]
            year = str(message.text).split("-")[2]
            date = year+"-"+month+"-"+day
            valid_date = time.strptime(date, '%Y-%m-%d')
            requestsApi.update(message.from_user.id,"birthday",date)
            await state_reg(message.from_user.id, data)
        except ValueError:
            await bot.send_message(message.from_user.id, date_error)


@dp.message_handler(state=Registration.REG_PHOTO, content_types=['photo'])
async def reg_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        photo_id = message.photo[1].file_id
        file = await bot.get_file(photo_id)
        file_path = file.file_path
        await bot.download_file(file_path, "./core/media/photo/"+str(message.from_user.id)+"__"+str(photo_id)+".png")
        await state.finish()
        await bot.send_message(message.from_user.id,finish_txt,reply_markup=MAIN_KB)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("fond"),state=Registration.REG_GROUP)
async def group(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        fond = str(callback_query.data).split("_")[1]
        requestsApi.update(callback_query.from_user.id, "group", fond)
        await state_reg(callback_query.from_user.id, data)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("fondcity"),state=Registration.REG_CITY)
async def city(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        fond = str(callback_query.data).split("_")[1]
        requestsApi.update(callback_query.from_user.id, "city", fond)
        await state_reg(callback_query.from_user.id, data)

@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("fondyear"),state=Registration.REG_YEARENTER)
async def year(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        year = str(callback_query.data).split("_")[1]
        data['year'] = year
        await bot.send_message(callback_query.from_user.id, date_example)
        await Registration.next()

