from aiogram import types
from core.helpers import telegram as tg_helper


finder_msg = 'В данном меню, ты можешь осуществить поиск пользователя.\nВыберите параметр по которому будет осуществлен' \
             'поиск'
finders_type = [
    ("По фамилии", "finder_lastname"),
    ("По сыллке вк", "finder_vk"),
    ("По сыллке файсбук", "finder_fb"),
    ("По telegram_id", "finder_tg"),
    ("По интересу", "finder_hobby"),
    ("По компетенции", "finder_competence")
]

finder_btn = tg_helper.create_inline_markup(*finders_type, row_width=2)

find_lastname_txt = 'Введите фамилию пользователя ("нет" - для отмены)'
find_telegramid_text = 'Введите id пользователя telegram ("нет" - для отмены)'

find_vk_text = 'Введите сыллку на вк ("нет" - для отмены)'
find_fb_text = 'Введите сыллку на facebook ("нет" - для отмены)'
find_url_error = 'Ошибка в сыллке на соц. сеть пользователя'

find_hobbyes_text = 'Выбирите хобби для поиска ("нет" - для отмены)'
find_competences_text = 'Выбирите компетенцию для поиска ("нет" - для отмены)'

users_not_found = 'Пользователей не найдено'
user_not_found  = 'Пользователь не найден'

find_cancled = 'Поиск отменен'

other_err = 'Ошибка поиска! попробуйте ввести данные еще раз'

def btns_users(tgid):
    btns = []
    btns.append(("Образование", "findusereducation_" + str(tgid)))
    btns.append(("Проекты", "finduserprojects_" + str(tgid)))
    btns.append(("Работа", "finduserwork_" + str(tgid)))
    btns.append(("На главную", "tomainfind"))
    finish_btns = tg_helper.create_inline_markup(*btns, row_width=2)
    return finish_btns