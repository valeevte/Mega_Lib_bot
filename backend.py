import telebot
from telebot import types


token = "6603598160:AAGs5mpzmXHfE7qjxoGgM42it19tsSb9Ti4" #Токен
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard_1.row("Дисциплины")
    bot.send_message(message.chat.id, f'Здравствуйте {message.from_user.username}!\nЯ бот который может дать вам необходимую литературу для обучения в МТУСИ.',
                     reply_markup=keyboard_1)


@bot.message_handler(commands=['help']) #из менюшки команд которая делается в BotFather
def start_message(message):
    bot.send_message(message.chat.id, 'Hyi')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "дисциплины":
        keyboard_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_matmem = telebot.types.KeyboardButton('Высшая математика')
        button_LaiaG = telebot.types.KeyboardButton('Линейная алгебра и анадитическая геометрия')
        button_Fil = telebot.types.KeyboardButton('Философия')
        button_Fiz_ra = telebot.types.KeyboardButton('Физкультура')
        button_Angl = telebot.types.KeyboardButton('Английский язык')
        button_Fizka = telebot.types.KeyboardButton('Физика')
        button_ORG = telebot.types.KeyboardButton('Основы Российской государственности')
        button_VVIT = telebot.types.KeyboardButton('Введение в информационные технологии')
        keyboard_2.add(button_matmem, button_LaiaG, button_Fil,
                       button_Fiz_ra, button_Angl, button_Fizka,
                       button_ORG, button_VVIT)


        bot.send_message(message.chat.id, 'Вот', reply_markup=keyboard_2)
    if message.text.lower() == "Высшая математика":
        bot.send_message(message.chat.id, ' \n', reply_markup=keyboard_2)
    elif message.text.lower() == "Линейная алгебра и анадитическая геометрия":
        bot.send_message(message.chat.id, '', reply_markup=keyboard_2)
    elif message.text.lower() == "Философия":
        bot.send_message(message.chat.id, '', reply_markup=keyboard_2)
    elif message.text.lower() == "Физкультура":
        bot.send_message(message.chat.id, '', reply_markup=keyboard_2)
    elif message.text.lower() == "Английский язык":
        bot.send_message(message.chat.id, '', reply_markup=keyboard_2)
    elif message.text.lower() == "Физика":
        bot.send_message(message.chat.id, '', reply_markup=keyboard_2)
    elif message.text.lower() == "Основы Российской государственности":
        bot.send_message(message.chat.id, '', reply_markup=keyboard_2)
    elif message.text.lower() == "Введение в информационные технологии":
        bot.send_message(message.chat.id, '', reply_markup=keyboard_2)
    elif message.text.lower() == "":
        bot.send_message(message.chat.id, '', reply_markup=keyboard_2)



bot.infinity_polling()