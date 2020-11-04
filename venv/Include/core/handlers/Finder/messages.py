from aiogram import types
from core.helpers import telegram as tg_helper


finder_msg = 'В данном меню, ты можешь осуществить поиск пользователя.\nВыберите параметр по которому будет осуществлен' \
             'поиск'
finders_type = {
    ("По фамилии", "finder_lastname"),
    ("По сыллке вк.", "finder_vk"),
    ("По сыллке файсбук.", "finder_fb"),
    ("По telegram_id", "finder_tg"),
    ("По интересу", "finder_hobby"),
    ("По компетенции", "finder_competence"),
    ("По telegram_id", "finder_tg")
}

finder_btn = tg_helper.create_inline_markup(*finders_type)

find_lastname_txt = 'Введите фамилию пользователя ("нет" - для отмены)'