from aiogram import types
from config import dp,bot,req_url
from aiogram.dispatcher import FSMContext
from .messages import *
from Include.core.helpers import requestsApi
from .CheckRegData import *

@dp.message_handler(state=Registration.REG_PASS, content_types=types.ContentTypes.TEXT)
async def auth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        auth_req = requestsApi.gettoken(message.from_user.id)
        if str(auth_req).__contains__("Object does not exist"):
            check_pass = requestsApi.check_pass(message.text,message.from_user.id)
            if check_pass['token'] == "incorrect password":
                await bot.send_message(message.from_user.id, bad_password)
            else:
                if (await state_reg(message.from_user.id, data)):
                    await state.finish()
        else:
            check_pass = requestsApi.check_pass(message.text, message.from_user.id)
            if check_pass['token'] == "incorrect password":
                await bot.send_message(message.from_user.id, bad_password)
            else:
                if (await state_reg(message.from_user.id, data)):
                    await state.finish()




