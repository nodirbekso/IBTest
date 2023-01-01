import telebot
from telebot import types
from functions import *


bot = telebot.TeleBot("5636756137:AAFY2wijoV2iwvF0WYOSh2f7cbRy30B7r2I")

@bot.message_handler(commands=["start"])
def start(message):
  if check_user(str(message.from_user.id)) is True:
    mess = f"<b>Добро пожаловать {message.from_user.first_name}, Вам разрешен доступ! </b>"
    bot.send_message(message.chat.id, mess, parse_mode="html")
    image = open('accept.png','rb')
    bot.send_photo(message.chat.id,image)
  else:
    bot.send_message(message.chat.id, "У Вас нет доступа, просим обратится к Администратору!!!", parse_mode="html")
    image = open('deny.png','rb')
    bot.send_photo(message.chat.id,image)
  zapis(message.from_user.id,message.from_user.first_name, message.text)

@bot.message_handler(commands=['add'])
def add(message):
    try:
        mText=message.text.split()
        if chekadmin(str(message.from_user.id)) == True:
            addUser(mText[1])
            bot.send_message(message.chat.id, f'Для ID {mText[1]} доступ разрешен', parse_mode="html")
        else:
            bot.send_message(message.chat.id, "У Вас нет доступа, просим обратится к Администратору!!!", parse_mode="html")
            image = open('deny.png', 'rb')
            bot.send_photo(message.chat.id, image)
        zapis(message.from_user.id, message.from_user.first_name, message.text)
    except:
        bot.send_message(message.chat.id, 'Введите команду в формате /add 123123123', parse_mode="html")
    zapis(message.from_user.id, message.from_user.first_name, message.text)

@bot.message_handler(commands=['getlog'])
def sendfile(message):
    try:
        if chekadmin(str(message.from_user.id)) == True:
            bot.send_document(message.chat.id, document=open('log.txt','rb'))
        else:
            bot.send_message(message.chat.id, "У Вас нет доступа, просим обратится к Администратору!!!", parse_mode="html")
            image = open('deny.png', 'rb')
            bot.send_photo(message.chat.id, image)
    except:
        bot.send_message(message.chat.id, 'Неизвестная ошибка!!!', parse_mode="html")
    zapis(message.from_user.id, message.from_user.first_name, message.text)

@bot.message_handler(commands=['clearlog'])
def sendfile(message):
    try:
        if chekadmin(str(message.from_user.id)) == True:
            f = open('log.txt', 'w')
            f.close()
            bot.send_message(message.chat.id, 'Лог очишен')
        else:
            bot.send_message(message.chat.id, "У Вас нет доступа, просим обратится к Администратору!!!", parse_mode="html")
            image = open('deny.png', 'rb')
            bot.send_photo(message.chat.id, image)
    except:
        bot.send_message(message.chat.id, 'Неизвестная ошибка!!!', parse_mode="html")
    zapis(message.from_user.id, message.from_user.first_name, message.text)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if check_user(str(message.from_user.id)) is True:
        mess = f"{message.from_user.first_name}, Я пока ничего не умею. \n"
        bot.send_message(message.chat.id, mess, parse_mode="html")
        image = open('jamshud.png','rb')
        bot.send_photo(message.chat.id,image)
    else:
        bot.send_message(message.chat.id, "У Вас нет доступа, Просим обратится к Администратору!!!", parse_mode="html")
        image = open('deny.png','rb')
        bot.send_photo(message.chat.id,image)
    zapis(message.from_user.id,message.from_user.first_name, message.text)

print('Bot starting...')

bot.polling(none_stop=True)