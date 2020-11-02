from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class UserProfileEdit(StatesGroup):
    EDIT_LASTNAME = State()
    EDIT_FIRSTNAME = State()
    EDIT_GROUP = State()
    EDIT_CITY = State()
    EDIT_YEARENTER = State()
    EDIT_DAYMONTHENTER = State()
    EDIT_EMAIL = State()
    EDIT_VK = State()
    EDIT_FB = State()
    EDIT_TEL = State()
    EDIT_BITRH = State()
    EDIT_PHOTO = State()

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


class AddProject(StatesGroup):
    Name = State()
    Info = State()
    Status = State()
    datestart = State()
    datefinish = State()

    hasGrant = State()
    ifhasGrant = State()

    statusInvestetion = State()
    InvestetionInfo = State()

class AddWork(StatesGroup):
    Organization = State()
    Status = State()
    inWork = State()
    dateStart = State()
    dateFinish = State()

class AddStudy(StatesGroup):
    TypeStudy = State()
    Location = State()
    progress = State()
    progress_stage = State()
    Specialty = State()

class Finder(StatesGroup):
    WRITE_DATA = State()


