from aiogram import types
from config import bot,dp
from Include.core.states import Registration
from .messages import *
from aiogram.dispatcher import FSMContext
from Include.core.helpers import requestsApi
from Include.core.helpers import telegram as tg_helper
from Include.core.helpers.Utils import *
import re
import json

async def state_reg(usertgid,data):
    userData = requestsApi.getUserData(usertgid)
    print(userData)
    if userData['last_name'] == "awaiting":
        await Registration.REG_LASTNAME.set()
        await bot.send_message(usertgid, last_name_txt)
        return
    elif userData['first_name'] == "awaiting":
        await Registration.REG_FIRSTNAME.set()
        await bot.send_message(usertgid, first_name_txt)
        return
    elif "fond" not in data and  userData['group'] == "awaiting" :
        await Registration.REG_GROUP.set()
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
        btns = tg_helper.create_inline_markup(*groups_list,row_width=1)
        await bot.send_message(usertgid, group_text, reply_markup=btns)
        return
    elif "city" not in data and userData['city'] == "awaiting":
        await Registration.REG_CITY.set()

        btns = await get_btns_param(userData, "city",data)
        await bot.send_message(usertgid, city_where, reply_markup=btns)

        return
    elif "1970-01-01" == userData['startdate']:
        await Registration.REG_YEARENTER.set()
        btns = await get_btns_param(userData,"year",data)
        await bot.send_message(usertgid, year_join, reply_markup=btns)

        return
    elif userData['email'] == "awaiting":
        await Registration.REG_EMAIL.set()
        await bot.send_message(usertgid, email_text)
        return
    elif userData['vk'] == "awaiting":
        await Registration.REG_VK.set()
        await bot.send_message(usertgid, vk_text)
        return
    elif userData['fb'] == "awaiting":
        await Registration.REG_FB.set()
        await bot.send_message(usertgid, fb_text)
        return
    elif userData['telnum'] == "awaiting":
        await Registration.REG_TEL.set()
        await bot.send_message(usertgid, telnum_text)
        return
    elif "1970-01-01" == userData['birthday']:
        await Registration.REG_BITRH.set()
        await bot.send_message(usertgid, birthday_text)
        return
    elif not check_photo(usertgid):
        await Registration.REG_PHOTO.set()
        await bot.send_message(usertgid, photo_text)
        return
    else:

        await bot.send_message(usertgid,finished_reg_text,reply_markup=MAIN_KB)
        return True


async def get_btns_param(userData,param,data):
    curgroup = data['fond']
    data_list = []
    groups = requestsApi.getgroups()
    for i in range(0, len(groups)):
        if curgroup == groups[i]['fond'] or curgroup == "mentor" or curgroup == "cofounder" or curgroup == "team":
            parametr = groups[i][param]
            tulist = (parametr, "fond"+param+"_" + parametr)
            if tulist not in data_list:
                data_list.append(tulist)
    btns = tg_helper.create_inline_markup(*reversed(data_list), row_width=2)
    return btns



