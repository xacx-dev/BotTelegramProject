from aiogram import types
from config import dp,bot,req_url
from aiogram.dispatcher import FSMContext
from Include.core.states import Registration
from .messages import *
from Include.core.helpers import requestsApi
from .CheckRegData import *

@dp.message_handler(state=Registration.REG_PASS, content_types=types.ContentTypes.TEXT)
async def auth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        check_user_bd =requestsApi.check_pass(message.text,message.from_user.id)
        print(check_user_bd)
        if not (check_user_bd['token'] and check_user_bd['id']):
            auth_req = requestsApi.gettoken(message.from_user.id)
            if not (auth_req['token'] and auth_req['id']):
                await bot.send_message(message.from_user.id, bad_password)
        else:
            if await state_reg(message.from_user.id, data):
                print('good')

