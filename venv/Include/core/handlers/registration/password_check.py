from aiogram import types
from config import dp,bot,req_url
from aiogram.dispatcher import FSMContext
from Include.core.states import Registration
from Include.models import tokens
import requests

@dp.message_handler(state=Registration.REG_PASS, content_types=types.ContentTypes.TEXT)
async def food_step_2(message: types.Message, state: FSMContext):  # обратите внимание, есть второй аргумент
    async with state.proxy() as data:
        user_pass = message.text
        json_data = requests.post(
            req_url + "/check_password?password=" + str(user_pass) + "&telid=" + str(message.from_user.id)).json()
        id = json_data['id']
        token = json_data['token']
        new_token = {
            "idinmain": id,
            "telegramid": message.from_user.id,
            "token": token
        }
        await tokens.create(**new_token)