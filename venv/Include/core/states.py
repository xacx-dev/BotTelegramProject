from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):

    REG_PASS = State()
    REG_LASTNAME = State()
    REG_FIRSTNAME = State()
    REG_GROUP = State()
    REG_CITY = State()
    REG_YEARENTER = State()
    REG_DAYMONTHENTER = State()
    REG_EMAIL = State()
    REG_VK = State()
    REG_FB = State()
    REG_TEL = State()
    REG_BITRH = State()
    REG_PHOTO = State()
