from aiogram import types
from config import dp,bot
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
from .messages import *




@dp.message_handler(lambda message: message.text and 'база пользователей' in message.text.lower())
async def base_main(message: types.Message):
    groups_list = []
    groups = requestsApi.getgroups()
    for i in range(1, len(groups)):
        fond = groups[i]['fond']
        tulist = ("Фонд \"" + fond + "\"", "basefond_" + fond)
        if tulist not in groups_list:
            groups_list.append(tulist)
    btns = tg_helper.create_inline_markup(*groups_list, row_width=1)
    await bot.send_message(message.from_user.id, select_fond, reply_markup=btns)


@dp.callback_query_handler(lambda c: str(c.data).split("_")[0].__eq__("basefond"))
async def city(callback_query: types.CallbackQuery):
    print(callback_query.data)
