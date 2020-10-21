from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Registration(StatesGroup):

    REG_PASS = State()
    REG_LASTNAME = State()
    REG_FIRSTNAME = State()
    REG_ROLE = State()
    REG_CITY = State()
    REG_DATAENTER = State()
    REG_URLSN = State()
    REG_TEL = State()
    REG_BITRH = State()
    REG_PHOTO = State()
