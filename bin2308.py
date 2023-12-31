import telebot
from telebot import types

token = '' #'6979653503:AAFzUb0ubmRUyQ0p_7Xwp3eotZQ5g7yFuUk'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button_disciplines=types.InlineKeyboardButton(text='Дисциплины', callback_data="disciplines_data")
    keyboard.add(button_disciplines)
    bot.send_message(message.chat.id, 'Приветствую чем могу помочь?', reply_markup=keyboard)


@bot.message_handler(commands=['info'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button_disciplines=types.InlineKeyboardButton(text='Назад 🔙', callback_data="start")
    keyboard.add(button_disciplines)
    bot.send_message(message.chat.id, f'Приветствую👋! Данный бот был разработан в рамках дисциплины "Введение в профессию" учащимеся "МТУСИ" академической группы "БИИН2308".\n'
                                      f'© Авторы работы: Федякин Егор, Ермаков Дмитрий, Гусев Иван, Валеев Тимур, Беляев Григорий, Тафинцев Егор.\n'
                                      f'Для получения информации о возможностях бота воспользуйтесь командой /help ', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    button_disciplines=types.InlineKeyboardButton(text='Назад 🔙', callback_data="start")
    keyboard.add(button_disciplines)
    bot.send_message(message.chat.id, f'Приветствую👋! Данный бот был разработан с целью: помочь первокурсникам получить доступ к структурированной системе знаний базовых дисциплин📖.\n'
                                      f'Вы можете выбрать любую дисциплину из перечня и получить каталог пособий📚, полезных сайтов🌐, а также видеокурсов🎥 на интерсующую вас тему по выбранной дисцииплине.\n'
                                      f'Приятного пользования ❤️!',  reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'start')
def spisok_btn(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()
    button_disciplines = types.InlineKeyboardButton(text='Дисциплины', callback_data="disciplines_data")
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
def philosopy(call):
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

    button_vishmat10 = types.InlineKeyboardButton(text='Тема №10: Дифференциальное исчисление функций нескольких переменных', callback_data="vishmat10_data")
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

    bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=A5LpC4yKWI8&list=PLqgCjH6Mu4yVIu_EbCv0MU0Tmtj0R1z7V&pp=iAQB')
    bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=iWite2swD0A&list=PLqgCjH6Mu4yXLH4APQX-ZFGhvKj3Ertx4' )
    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=T2ndcLNDWcs&list=PLtaqFZsfPcLkRUc4qJA6xjXdScmbg-JFj', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat_possobie_data')
def vishmat_possobie(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    file1="BQACAgIAAxkBAAPtZYBitDxrRzFLDfB9La6Ww9ns2VAAAsI9AAKUzQABSAtb0UlNgbV7MwQ"
    file2="BQACAgIAAxkBAAPzZYBpw-71RkeDCHw5kXuwHYNegBQAAhw-AAKUzQABSKCjkGJqwtR1MwQ"
    file3="BQACAgIAAxkBAAIBB2WAa3sYBVbq9as0SjA4ht2vkpoUAAIvPgAClM0AAUhWUHSE2V7k6zME"

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_data")
    keyboard.add(button_back)

    bot.send_document(message.chat.id, file1)
    bot.send_document(message.chat.id, file2)
    bot.send_document(message.chat.id, file3, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics_possobie_data')
def physics_possobie(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    file1="BQACAgIAAxkBAAIBEmWAbISAowABBuCDL6AjwHWO_GsnSQACPD4AApTNAAFIApKcfAauYcQzBA"
    file2="BQACAgIAAxkBAAIBFGWAbbqBdUuOT6YsamnAqzNnRP6LAAJMPgAClM0AAUi8Poi-f0xeHjME"
    file3="BQACAgIAAxkBAAIBFWWAbmBpryyXlh5hTVZc5vaGi6qGAAJdPgAClM0AAUgec8P6YtpkHDME"

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_data")
    keyboard.add(button_back)

    bot.send_document(message.chat.id, file1)
    bot.send_document(message.chat.id, file2)
    bot.send_document(message.chat.id, file3, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal_possobie_data')
def linal_possobie(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    file1="BQACAgIAAxkBAAIBG2WAcTrjuZNjrdydGISOAdKON67yAAJ0PgAClM0AAUiBjMjIHxHL2zME"
    file2="BQACAgIAAxkBAAIBHGWAcdi3uV1_utjam79VjJzwBhD0AAJ4PgAClM0AAUg5hQo6mU9oMDME"
    file3="BQACAgIAAxkBAAIBHWWAcnuoBpLagtG9GbrhwFM_qpk7AAJ_PgAClM0AAUge1PZFdlF1tDME"

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_data")
    keyboard.add(button_back)

    bot.send_document(message.chat.id, file1)
    bot.send_document(message.chat.id, file2)
    bot.send_document(message.chat.id, file3, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'philosophy_possobie_data')
def philosophy_possobie(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    file1="BQACAgIAAxkBAAIBJ2WAdGhfUFSy0roGfkfO_D0vc3e2AAKSPgAClM0AAUh_OXpbmnJOVTME"
    file2="BQACAgIAAxkBAAIBKGWAdKthVZqB0tYCtB8JG_QM9kU-AAKYPgAClM0AAUjTPp6bGea0uTME"
    file3="BQACAgIAAxkBAAIBKWWAdTGTNx2yandYtgGzzhxe0JP8AAKfPgAClM0AAUjauGSFk2I20zME"

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="philosophy_data")
    keyboard.add(button_back)

    bot.send_document(message.chat.id, file1)
    bot.send_document(message.chat.id, file2)
    bot.send_document(message.chat.id, file3, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vvit_possobie_data')
def vvit_possobie(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    file1="BQACAgIAAxkBAAIBlWWAmjQg17BnyLpvbEt3Ddtuvou_AAIhQAAClM0AAUj1HurVsPQ2FTME"
    file2="BQACAgIAAxkBAAIBlmWAmpU3wF_cS91sZn6fNBD6MXSbAAIlQAAClM0AAUgfNp8fKWJQZjME"
    file3="BQACAgIAAxkBAAIBl2WAmsNKJQVGBSJX9vCXQeKwuj2tAAImQAAClM0AAUgwiTGKPK-oNDME"

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vvit_data")
    keyboard.add(button_back)

    bot.send_document(message.chat.id, file1)
    bot.send_document(message.chat.id, file2)
    bot.send_document(message.chat.id, file3, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'org_possobie_data')
def org_possobie(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    file1="BQACAgIAAxkBAAIBo2WAm6hYzhEUENOq5jx-15JiRj-4AAItQAAClM0AAUgIwIONRbzeRjME"

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="org_data")
    keyboard.add(button_back)

    bot.send_document(message.chat.id, file1, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat_sites_data')
def vishmat_sites(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id,'http://mathportal.net/')
    bot.send_message(message.chat.id,'http://www.mathprofi.ru/' )
    bot.send_message(message.chat.id, 'https://mathter.pro/algebra/index.html', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics_sites_data')
def physics_sites(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id,'https://online.mephi.ru/local/staticpage/view.php?page=open-courses-physic')
    bot.send_message(message.chat.id,'https://www.fxyz.ru/формулы_по_физике/' )
    bot.send_message(message.chat.id, 'http://alexandr4784.narod.ru/lktf.html', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal_sites_data')
def linal_sites(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'http://mathportal.net/')
    bot.send_message(message.chat.id, 'http://www.mathprofi.ru/')
    bot.send_message(message.chat.id, 'https://mathter.pro/algebra/index.html', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'philosophy_sites_data')
def philosophy_sites(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="philosophy_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://philosophy.ru/')
    bot.send_message(message.chat.id, 'https://filosofka.ru/', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vvit_sites_data')
def vvit_sites(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vvit_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://practicum.yandex.ru/')
    bot.send_message(message.chat.id, 'https://pythontutor.com/')
    bot.send_message(message.chat.id, 'https://github.com/', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'org_sites_data')
def org_sites(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="org_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'http://kremlin.ru/acts/constitution')
    bot.send_message(message.chat.id, 'https://www.prlib.ru/section/675770', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat1_data')
def vishmat1(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/SPMRNnpN-d8?si=PvtpDQCj3CgBVlG2', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat2_data')
def vishmat2(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/CpvRFvbEazs?si=ng6lJUEjFCMEoQTC', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat3_data')
def vishmat3(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/XDqBj15EikU?si=VS6jNjWxZely5wbo', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat4_data')
def vishmat4(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/dx_GkybeWjA?si=GrNWhvTlB9RnX7Dd', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat5_data')
def vishmat5(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/vOdANRQ2894?si=I7TKSjR6Hm87xg_Z', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat6_data')
def vishmat6(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/t1sGt1eAaR4?si=pjs_1tT8Hd-d3kuE', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat7_data')
def vishmat7(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/-HOAQt_ysLs?si=AfVo-F5z3W0bDUcI', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat8_data')
def vishmat8(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/IZrJsHninBY?si=FiUop54DMnhJp3C3', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat9_data')
def vishmat9(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/bLU30iUnG-g?si=1afEayEuC7YcvXXf', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'vishmat10_data')
def vishmat10(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="vishmat_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/6ARoQIBYizc?si=QwH_b6JCqP6ofF_c', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics1_data')
def physics1(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/I_kJK7HLgRE?si=OuVjKDqkzfCi5B-J', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics2_data')
def physics2(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/KVhPa_gicVA?si=XC5soGnM0QILOJ8R', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics3_data')
def physics3(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=6Vz1WQ4FiVU&list=PLtkGmqQ5HKX69m31ZYr-dSRkEYs5Fa1In', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics4_data')
def physics4(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://www.youtube.com/playlist?list=PLDRwwWq7BiXXRO6wBxVaTH8L7PSiHzH-7', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics5_data')
def physics5(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/H-xrkK3_HsQ?si=cYmFJplipBMW70op', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics6_data')
def physics6(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=SBEtiXnLtpw&list=PLcsjsqLLSfNDqvcsTsKJM1Ee6V8Aaobl0', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'physics7_data')
def physics7(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="physics_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://www.youtube.com/playlist?list=PLcsjsqLLSfNCfd1y8EE-JrpIFziq9KAhc', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal1_data')
def linal1(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/UW3BkIRuoD4?si=auSMOmYXSO9tAa5f', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal2_data')
def linal2(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/Ko1GJgrc0LE?si=3la727Yc_0r2issq', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal3_data')
def linal3(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/Yr_5FJChGJc?si=CC8mdNheyO9iRGBT', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal4_data')
def linal4(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/4ezaIkdsSa8?si=QYeq5FVC4xNVdBhB', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal5_data')
def linal5(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/qbGg3-kgSMA?si=UpHXwK6uqQ0_oKXH', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal6_data')
def linal6(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/lUp4zAyxi_8?si=xGm9t2NbDMW4ioVV', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal7_data')
def linal7(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/YAnAhSnfUgI?si=5XmVyf7y3O__MWn5', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'linal8_data')
def linal8(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="linal_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/62WBR6zTxpQ?si=gekNa1Sv45M4GoJv', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'philosophy1_data')
def philosophy1(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="philosophy_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/aCP1S8cULM4?si=TJUEX3IT0S3tTAHI', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'philosophy2_data')
def philosophy2(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="philosophy_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/sNbc5X2p0VY?si=YcPZ6CvIHtQukwBK', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'philosophy3_data')
def philosophy3(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="philosophy_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/EQw8HtCKpIE?si=ypTneL2SkCEvl90F', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'philosophy4_data')
def philosophy4(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="philosophy_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://youtu.be/1yQ2QyUcRTg?si=9msGWNCZRPN_rFyQ', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'philosophy5_data')
def philosophy5(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="philosophy_video_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://www.youtube.com/playlist?list=PLA7fOvwFVwW6UCxHmTH79hUPreryUOomV', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'inyaz_sites_data')
def inyaz_sites(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="inyaz_data")
    keyboard.add(button_back)

    bot.send_message(message.chat.id, 'https://www.duolingo.com/')
    bot.send_message(message.chat.id, 'https://www.fluentu.com/')
    bot.send_message(message.chat.id, 'https://www.memrise.com/', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'inyaz_possobie_data')
def inyaz_possobie(call):
    message = call.message
    keyboard = types.InlineKeyboardMarkup()

    file1="BQACAgIAAxkBAAIDFGWBgLKWEnoFYmEebtwGZ06OuKejAAIkOwACRcwQSOPDQhVyZI2iMwQ"

    button_back = types.InlineKeyboardButton(text='Назад 🔙', callback_data="inyaz_data")
    keyboard.add(button_back)

    bot.send_document(message.chat.id, file1, reply_markup=keyboard)


bot.infinity_polling()
