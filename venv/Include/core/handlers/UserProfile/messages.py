from .helper import *
from aiogram import types
from core.helpers import telegram as tg_helper

edit_addon = "\nЕсли не хотите ничего менять отправте 0"
edit_finish = "Редактирование завершено!"

date_error = '<b>Ошибка!</b>\n\nУкажите дату повтороно\nПример: 2020-01-01 '


user_profile_text = 'В данном меню, вы можете работать со свои профилем'
user_profile = {

    ("О проекте", "userprofile_project"),
    ("О учебе", "userprofile_study"),

    ("О работе", "userprofile_work"),
    ("О интересах", "userprofile_hobby"),

    ("О компетенции", "userprofile_competence"),
    ("Изменить информацию", "userprofile_edit")
}

user_profile_btn = tg_helper.create_inline_markup(*user_profile)

#-----------------competence--------------------------#
competence_msg = 'Управление вашими компетенциями'
competence_text_1 = 'Выберите компетенцию, которую хотите добавить'
competence_text_2 = 'Выберите компетенцию, которую хотите удалить'
competence_text_3 = 'Компетенция удалена'
competence_text_4 = 'Компетенция добавлена'
competence = {
    ("Добавить компетенцию", "add_competence"),
    ("Удалить компетенцию", "remove_competence"),
    ("Предыдущее окно","back")
}
competence_btn = tg_helper.create_inline_markup(*competence)
def get_competence_info(tgid):
    competence_data = getcompetences(tgid)
    main_text = []
    id = 0
    main_text.append("Ваши Компетенции:")
    for i in competence_data:
        id += 1
        main_text.append('  {}. #{}'.format(str(id),i['hashtag']))


    fin_text=''
    for i in main_text:
        fin_text += i+"\n"
    return fin_text
#------------------------------------------------#

#-----------------hobby--------------------------#
hobby_msg = 'Управление вашими интересами'
hobby_text_1 = 'Выберите интерес, который хотите добавить'
hobby_text_2 = 'Выберите интерес, который хотите удалить'
hobby_text_3 = 'Интерес удален'
hobby_text_4 = 'Интерес добавлен'
hobby = {
    ("Добавить интерес", "add_hobby"),
    ("Удалить интерес", "remove_hobby"),
    ("Предыдущее окно","back")
}
hobby_btn = tg_helper.create_inline_markup(*hobby)
def get_hobby_info(tgid):
    hobby_data = gethobby(tgid)
    main_text = []
    id = 0
    main_text.append("Ваши интересы:")
    for i in hobby_data:
        id += 1
        main_text.append('  {}. #{}'.format(str(id),i['hashtag']))


    fin_text=''
    for i in main_text:
        fin_text += i+"\n"
    return fin_text
#------------------------------------------------#

#-----------------study--------------------------#
study = {
    ("Добавить учёбу", "add_study"),
    ("Удалить учёбу", "remove_study"),
    ("Предыдущее окно","back")
}
study_btn = tg_helper.create_inline_markup(*study)
study_msg = 'Информация о вашей учебе'
type_study = {
    ("Школьник", "typestudy_sch"),
    ("(Вуз) Бакалавриат", "typestudy_bkl"),
    ("(Вуз) Магистратура", "typestudy_mag"),
    ("(Вуз) Кандидат наук", "typestudy_kad"),
    ("(Вуз) Доктор наук", "typestudy_doc"),
}
type_study_btn = tg_helper.create_inline_markup(*type_study)

study_text_1 = 'Тип вашего обучения ВУЗ/Школа'
study_text_2 = 'Введите Место обучения'
study_text_3 = 'Ваш статус'
state_study = {
    ("Учился", "studystatus_finished"),
    ("Учусь", "studystatus_inprogress")
}
state_study_btn = tg_helper.create_inline_markup(*state_study)

study_text_4 = 'Введите Ваш класс'
study_text_5 = 'Введите Ваш курс'
study_text_6 = 'Введите вашу специальность'

study_error_sch = 'Неправильный номер класса, введите число от 8 до 11'
study_error_vuz = 'Неправильный номер курса, введите число от 1 до 7'

study_added = 'Учеба добавлена'
study_deleted = 'Учеба удалена'
def get_study_info(tgid):
    study_data = getstudy(tgid)
    main_text = []
    id = 0
    for i in study_data:
        id += 1
        if i['type'] == "sch":
            main_text.append('{}. Тип: {}'.format(str(id),"Школа"))
        elif i['type'] == "bkl":
            main_text.append('{}. Тип: {}'.format(str(id), "(Вуз) Бакалавриат"))
        elif i['type'] == "mag":
            main_text.append('{}. Тип: {}'.format(str(id), "(Вуз) Магистратура"))
        elif i['type'] == "kad":
            main_text.append('{}. Тип: {}'.format(str(id), "(Вуз) Кандидат наук"))
        elif i['type'] == "doc":
            main_text.append('{}. Тип: {}'.format(str(id), "(Вуз) Доктор наук"))

        main_text.append('Название: {}'.format(i['name']))

        if not i['status']:
            if i['type'] == "sch":
                main_text.append('Класс: {}'.format(i['step']))
                main_text.append('Статус: учусь')
            else:
                main_text.append('Курс: {}'.format(i['step']))
                main_text.append('Специальность: {}'.format(i['speciality']))
                main_text.append('Статус: учусь')
        else:
            if i['type'] == "sch":
                main_text.append('Класс: {}'.format(i['step']))
                main_text.append('Статус: закончил обучение')
            else:
                main_text.append('Курс: {}'.format(i['step']))
                main_text.append('Специальность: {}'.format(i['speciality']))
                main_text.append('Статус: закончил обучение')


        main_text.append("")

    fin_text=''
    for i in main_text:
        fin_text += i+"\n"
    return fin_text
#--------------------------------------------------#



#-----------------Work--------------------------#
works = {
    ("Добавить работу", "add_work"),
    ("Удалить работу", "remove_work"),
    ("Предыдущее окно","back")
}
works_btn = tg_helper.create_inline_markup(*works)
work_msg = 'Информация о ваших работах'
work_text_1 = 'Введите Название вашей работы\\организации'
work_text_2 = 'Введите вашу должность'
work_text_3 = 'Ваш статус'
state_work = {
    ("Ушел с работы", "workstatus_finished"),
    ("Работаю", "workstatus_inprogress")
}
state_work_btn = tg_helper.create_inline_markup(*state_work)
work_text_4 = 'Когда начали работать\nВведите дату в формате 2020-01-01'
work_text_5 = 'Когда закончили работать\nВведите дату в формате 2020-01-01'
work_deleted = 'Работа удалена'
def get_works_info(tgid):
    works_data = getworks(tgid)
    main_text = []
    id = 0
    for i in works_data:
        id += 1
        main_text.append('{}. Название: {}'.format(str(id),i['name']))
        main_text.append('Должность: {}'.format(i['position']))
        if i['status']:
            main_text.append('Статус: работую')
            main_text.append('Дата начала: {}'.format(i['startdate']))
        else:
            main_text.append('Статус: ушел с работы')
            main_text.append('Дата начала: {}'.format(i['startdate']))
            main_text.append('Дата конца: {}'.format(i['enddate']))
        main_text.append("")

    fin_text=''
    for i in main_text:
        fin_text += i+"\n"
    return fin_text
#--------------------------------------------------#




#----------------PROJECT-----------------------#
project_msg = 'Информация о ваших проектах'
project_deleted = 'Проект удален'
project_text_1 = 'Введите Название проекта'
project_text_2 = 'Введите описание проекта'
project_text_3 = 'Выберите статус проекта'
state_project = {
    ("Завершен", "projectstatus_finished"),
    ("В процессе", "projectstatus_inprogress")
}
state_project_btn = tg_helper.create_inline_markup(*state_project)
project_text_4 = 'Когда вы начали проект?\nВведите дату в формате 2020-01-01'
project_text_5 = 'Когда планируете закончить проект?\nВведите дату в формате 2020-01-01'
project_text_6 = 'Получены ли грант или инвестиции?'
grant_project = {
    ("Да", "projectgrant_yes"),
    ("Нет", "projectgrant_no")
}
grant_project_btn = tg_helper.create_inline_markup(*grant_project)
project_text_7 = 'От кого вы получили поддержку'
project_text_8 = 'Нужны ли инвестиции?'
invest_project = {
    ("Да", "projectinvestition_yes"),
    ("Нет", "projectinvestition_no")
}
invest_btn = tg_helper.create_inline_markup(*invest_project)
project_text_9 = 'Какая вам нужна сумма для поддержки (число в долларах)'
project_text_10 = 'Проект добавлен!'
projects = {
    ("Добавить проект", "add_project"),
    ("Удалить проект", "remove_project"),
    ("Предыдущее окно","back")
}
projects_btn = tg_helper.create_inline_markup(*projects)

def get_project_info(tgid):

    projects_data = getprojects(tgid)
    main_text = []
    id = 0
    for i in projects_data:
        id += 1
        main_text.append('{}. Название: {}'.format(str(id),i['name']))
        main_text.append('Описание: {}'.format(i['description']))
        if i['status'] == 0:
            main_text.append('Статус: в процессе')
        else:
            main_text.append('Статус: завершен')
        main_text.append('Дата начала: {}'.format(i['startdate']))
        main_text.append('Дата конца: {}'.format(i['enddate']))
        if i['investor']:
            main_text.append('Информация о инвесторах: {}'.format(i['investor']))
        if i['investneedsum']:
            main_text.append('Нужная сумма инвестиции: {}'.format(i['investneedsum']))
        main_text.append("")

    fin_text=''
    for i in main_text:
        fin_text += i+"\n"
    return fin_text
#--------------------------------------------------#





def main_data(tgid):
    main_text = []
    main_data = getdata(tgid)
    study_data = getstudy(tgid)
    work_data = getworks(tgid)
    hobby_data = gethobby(tgid)
    competence_data = getcompetences(tgid)
    projects_data = getprojects(tgid)

    main_text.append('🙍‍♂{}, {}'.format(main_data['first_name'], main_data['last_name']))
    main_text.append('Участник проекта "{}" с {} года'.format(main_data['group'], str(main_data['startdate']).split("-")[0]))
    main_text.append("")
    main_text.append('🌃Город: {}'.format(main_data['city']))

    if study_data:

        study = ''
        for i in study_data:
            study = study + i['name'] + " "
        main_text.append('👨‍🎓Образование: {}'.format(study))
    else:
        main_text.append('👨‍🎓Образование: не установлено')

    if work_data:
        works = ''
        for i in work_data:
            works = works + i['name'] + " "
        main_text.append('👨‍💼Работа: {} '.format(works))
    else:
        main_text.append('👨‍💼Работа: не установлено')

    if hobby_data:
        hobbyes =''
        for i in hobby_data:
            hobbyes = hobbyes+"#"+i['hashtag']+" "
        main_text.append('🕵‍♂Интересы: {}'.format(hobbyes))
    else:
        main_text.append('🕵‍♂Интересы: нет')

    if competence_data:
        competence =''
        for i in competence_data:
            competence = competence+"#"+i['hashtag']+" "
        main_text.append('🕵‍♂Компетенции: {}'.format(competence))
    else:
        main_text.append('🕵‍♂Компетенции: нет')

    if projects_data:
        projects =''
        for i in projects_data:
            projects = projects+i['name']+" "
        main_text.append('👨‍💻Проекты: {}'.format(projects))
    else:
        main_text.append('👨‍💻Проекты: нет')
    main_text.append("")
    main_text.append('💻Профиль ВКонтакте: {}'.format(main_data["vk"]))
    main_text.append('💻Профиль Facebook: {}'.format(main_data["fb"]))
    main_text.append('☎Телефон: {}'.format(main_data['telnum']))

    fin_text=''
    for i in main_text:
        fin_text += i+"\n"
    return fin_text


