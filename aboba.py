import telebot
from telebot import types

token = '6603598160:AAGs5mpzmXHfE7qjxoGgM42it19tsSb9Ti4'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button_disciplines=types.InlineKeyboardButton(text='Дисциплины', callback_data="disciplines_data")
    keyboard.add(button_disciplines)
    bot.send_message(message.chat.id, 'Приветствую чем могу помочь?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'disciplines_data')
def spisok_btn(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_vishmat = types.InlineKeyboardButton(text='Высшая математика 🧠', callback_data="vishmat_data")
    keyboard.add(button_vishmat)

    button_matan = types.InlineKeyboardButton(text='Линейная алгебра и аналитическая геометрия 📐', callback_data="linal_data")
    button_physics = types.InlineKeyboardButton(text='Физика ⚛️', callback_data="physics_data")
    keyboard.add(button_physics, button_matan)

    button_philosophy = types.InlineKeyboardButton(text='Философия 🗿', callback_data="philosophy_data")
    button_vvit = types.InlineKeyboardButton(text='ВвИТ 💻', callback_data="vvit_data")
    keyboard.add(button_philosophy, button_vvit)

    button_org = types.InlineKeyboardButton(text='ОРГ 🇷🇺', callback_data="org_data")
    button_inyaz = types.InlineKeyboardButton(text='Иностранные языки 💬 ', callback_data="inyaz_data")
    keyboard.add(button_org, button_inyaz)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="start")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Выберите одну из дисциплин', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat_data')
def vishmat(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_possobie = types.InlineKeyboardButton(text='Учебники и пособия 📚', callback_data="vishmat_possobie_data")
    keyboard.add(button_possobie)

    button_sites = types.InlineKeyboardButton(text='Полезные сайты 🌐', callback_data="vishmat_sites_data")
    keyboard.add(button_sites)

    button_video = types.InlineKeyboardButton(text='Темы и видеокурсы 🎥', callback_data="vishmat_video_data")
    keyboard.add(button_video)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="disciplines_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics_data')
def physics(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_possobie= types.InlineKeyboardButton(text='Учебники и пособия 📚', callback_data="physics_possobie_data")
    keyboard.add(button_possobie)

    button_sites = types.InlineKeyboardButton(text='Полезные сайты 🌐', callback_data="physics_sites_data")
    keyboard.add(button_sites)

    button_video = types.InlineKeyboardButton(text='Темы и видеокурсы 🎥', callback_data="physics_video_data")
    keyboard.add(button_video)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="disciplines_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal_data')
def linal(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_possobie = types.InlineKeyboardButton(text='Учебники и пособия 📚', callback_data="linal_possobie_data")
    keyboard.add(button_possobie)

    button_sites = types.InlineKeyboardButton(text='Полезные сайты 🌐', callback_data="linal_sites_data")
    keyboard.add(button_sites)

    button_video = types.InlineKeyboardButton(text='Темы и видеокурсы 🎥', callback_data="linal_video_data")
    keyboard.add(button_video)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="disciplines_data")
    keyboard.add(button_back)


    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'philosophy_data')
def phylosopy(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_possobie = types.InlineKeyboardButton(text='Учебники и пособия 📚', callback_data="philosophy_possobie_data")
    keyboard.add(button_possobie)

    button_sites = types.InlineKeyboardButton(text='Полезные сайты 🌐', callback_data="philosophy_sites_data")
    keyboard.add(button_sites)

    button_video = types.InlineKeyboardButton(text='Темы и видеокурсы 🎥', callback_data="philosophy_video_data")
    keyboard.add(button_video)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="disciplines_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'vvit_data')
def vvit(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_possobie= types.InlineKeyboardButton(text='Учебники и пособия 📚', callback_data="vvit_possobie_data")
    keyboard.add(button_possobie)

    button_sites = types.InlineKeyboardButton(text='Полезные сайты 🌐', callback_data="vvit_sites_data")
    keyboard.add(button_sites)

    button_video = types.InlineKeyboardButton(text='Видеокурсы 🎥', callback_data="vvit_video_data")
    keyboard.add(button_video)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="disciplines_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'org_data')
def org (call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_possobie= types.InlineKeyboardButton(text='Учебники и пособия 📚', callback_data="org_possobie_data")
    keyboard.add(button_possobie)

    button_sites = types.InlineKeyboardButton(text='Полезные сайты 🌐', callback_data="org_sites_data")
    keyboard.add(button_sites)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="disciplines_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'inyaz_data')
def inyaz(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_possobie= types.InlineKeyboardButton(text='Учебники и пособия 📚', callback_data="inyaz_possobie_data")
    keyboard.add(button_possobie)

    button_sites = types.InlineKeyboardButton(text='Полезные сайты 🌐', callback_data="inyaz_sites_data")
    keyboard.add(button_sites)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="disciplines_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat_video_data')
def vishmat_video(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_vishmat1 = types.InlineKeyboardButton(text='Тема №1: Множества', callback_data="vishmat1_data")
    keyboard.add(button_vishmat1)

    button_vishmat2 = types.InlineKeyboardButton(text='Тема №2: Функции', callback_data="vishmat2_data")
    keyboard.add(button_vishmat2)

    button_vishmat3 = types.InlineKeyboardButton(text='Тема №3: Последовательности и пределы', callback_data="vishmat3_data")
    keyboard.add(button_vishmat3)

    button_vishmat4 = types.InlineKeyboardButton(text='Тема №4: Дифференцирование функции одной переменой', callback_data="vishmat4_data")
    keyboard.add(button_vishmat4)

    button_vishmat5 = types.InlineKeyboardButton(text='Тема №5: Производная и дифференциал функции', callback_data="vishmat5_data")
    keyboard.add(button_vishmat5)


    button_vishmat6 = types.InlineKeyboardButton(text='Тема №6: Дифференцирование функций, заданных неявно и параметрически', callback_data="vishmat6_data")
    keyboard.add(button_vishmat6)

    button_vishmat7 = types.InlineKeyboardButton(text='Тема №7: Производные и дифференциалы высших порядков', callback_data="vishmat7_data")
    keyboard.add(button_vishmat7)

    button_vishmat8 = types.InlineKeyboardButton(text='Тема №8: Формула Тейлора', callback_data="vishmat8_data")
    keyboard.add(button_vishmat8)

    button_vishmat9 = types.InlineKeyboardButton(text='Тема №9: Правило Лопиталя', callback_data="vishmat9_data")
    keyboard.add(button_vishmat9)

    button_vishmat10 = types.InlineKeyboardButton(text='Тема №10: Диффирициальное исчисление функций нескольких переменных', callback_data="vishmat10_data")
    keyboard.add(button_vishmat10)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics_video_data')
def physics_video(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_physics1 = types.InlineKeyboardButton(text='Тема №1: Основы механики', callback_data="physics1_data")
    keyboard.add(button_physics1)

    button_physics2 = types.InlineKeyboardButton(text='Тема №2: Основы молекулярной физики и термодинамики', callback_data="physics2_data")
    keyboard.add(button_physics2)

    button_physics3 = types.InlineKeyboardButton(text='Тема №3: Электричество и электромагнетизм', callback_data="physics3_data")
    keyboard.add(button_physics3)

    button_physics4 = types.InlineKeyboardButton(text='Тема №4: Колебания и волны', callback_data="physics4_data")
    keyboard.add(button_physics4)

    button_physics5 = types.InlineKeyboardButton(text='Тема №5: Квантовая природа излучения', callback_data="physics5_data")
    keyboard.add(button_physics5)

    button_physics6 = types.InlineKeyboardButton(text='Тема №6: Элементы квантовой физики атомовБ молекул и твёрдых тел', callback_data="physics6_data")
    keyboard.add(button_physics6)

    button_physics7 = types.InlineKeyboardButton(text='Тема №7: Элементы физики атомного ядра и элементарных частиц', callback_data="physics7_data")
    keyboard.add(button_physics7)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal_video_data')
def linal_video(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_linal1 = types.InlineKeyboardButton(text='Тема №1: Прямая на плоскости', callback_data="linal1_data")
    keyboard.add(button_linal1)

    button_linal2 = types.InlineKeyboardButton(text='Тема №2: Плоскость в пространстве', callback_data="linal2_data")
    keyboard.add(button_linal2)

    button_linal3 = types.InlineKeyboardButton(text='Тема №3: Прямая в пространстве', callback_data="linal3_data")
    keyboard.add(button_linal3)

    button_linal4 = types.InlineKeyboardButton(text='Тема №4: Взаимное расположение прямой и плоскости в пространстве', callback_data="linal4_data")
    keyboard.add(button_linal4)

    button_linal5 = types.InlineKeyboardButton(text='Тема №5: Кривые второго порядка', callback_data="linal5_data")
    keyboard.add(button_linal5)

    button_linal6 = types.InlineKeyboardButton(text='Тема №6: Поверхности второго порядка', callback_data="linal6_data")
    keyboard.add(button_linal6)

    button_linal7 = types.InlineKeyboardButton(text='Тема №7: Линейные операторы', callback_data="linal7_data")
    keyboard.add(button_linal7)

    button_linal8 = types.InlineKeyboardButton(text='Тема №8: Квадратичные и билинейные формы', callback_data="linal8_data")
    keyboard.add(button_linal8)


    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'philosophy_video_data')
def philosophy_video(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_philosophy1 = types.InlineKeyboardButton(text='Тема №1: Философия как мировоззрение', callback_data="philosophy1_data")
    keyboard.add(button_philosophy1)

    button_philosophy2 = types.InlineKeyboardButton(text='Тема №2: Онтология', callback_data="philosophy2_data")
    keyboard.add(button_philosophy2)

    button_philosophy3 = types.InlineKeyboardButton(text='Тема №3: Теория познания', callback_data="philosophy3_data")
    keyboard.add(button_philosophy3)

    button_philosophy4 = types.InlineKeyboardButton(text='Тема №4: Философская антропология', callback_data="philosophy4_data")
    keyboard.add(button_philosophy4)

    button_philosophy5 = types.InlineKeyboardButton(text='Тема №5: Социальная философия', callback_data="philosophy5_data")
    keyboard.add(button_philosophy5)

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="philosophy_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'Что хотите выбрать?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vvit_video_data')
def vvit_video(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vvit_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=A5LpC4yKWI8&list=PLqgCjH6Mu4yVIu_EbCv0MU0Tmtj0R1z7V&pp=iAQB', reply_markup=keyboard)
    bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=iWite2swD0A&list=PLqgCjH6Mu4yXLH4APQX-ZFGhvKj3Ertx4', reply_markup=keyboard)
    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=T2ndcLNDWcs&list=PLtaqFZsfPcLkRUc4qJA6xjXdScmbg-JFj', reply_markup=keyboard)


bot.infinity_polling()