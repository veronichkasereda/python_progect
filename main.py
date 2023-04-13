import telebot
import requests
from telebot import types  # для указание типов

from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Начать игру")
    button2 = types.KeyboardButton("Есть вопросик")
    button3 = types.KeyboardButton("Узнать правила игры")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот-помощник для проекта фото-квеста 'Назад в прошлое'".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Начать игру"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Задание 1")
        button2 = types.KeyboardButton("Задание 2")
        button3 = types.KeyboardButton("Задание 3")
        home = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, home)
        bot.send_message(message.chat.id,
                         text="Тебе предстоит выполнить 3 задания. Один или вместе с командой ты должен прийти в указанное место, сделать и отправить вашу общую фотографию. Ты можешь посмотреть все задания и выбрать сначала то, что больше тебе понравится, но будь очень внимателен при отправке своего ответа!",
                         reply_markup=markup)
    elif (message.text == "Узнать правила игры"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Начать игру")
        home = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, home)
        bot.send_message(message.chat.id,
                         text="Твоя задача - выполнять задания, которые я буду отправять. Приготовьтесь интересно, а главное - с пользой провести это время!)",
                         reply_markup=markup)

    elif (message.text == "Есть вопросик"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Начать игру")
        home = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, home)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
#в этих трех условиях бот отправляет человеку фоточки заданий с их текстом
    elif (message.text == "Задание 1"):
        img = open('pictures/first_picture.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, text="Круто! Что мы будем делать дальше?")

    elif (message.text == "Задание 2"):
        img = open('pictures/second_picture.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, text="Так держать!")


    elif (message.text == "Задание 3"):
        img = open('pictures/third_picture.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, text="Очень классно получилось!)")


    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Начать игру")
        button2 = types.KeyboardButton("Есть вопросик")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

#тут у нас сохраняется фотография, отправленная пользователем, под именем img.jpg в папке answers
    elif ("Ответ на задание 1" in message.text):
        picture = str(message.text)[19:]
        p = requests.get(picture)
        out = open("answers/img.jpg", "wb")
        out.write(p.content)
        out.close()
        bot.send_message(message.chat.id, text="Очень классно получилось!)")
    else:
        bot.send_message(message.chat.id,
                         text="К сожалению, такой команды я не знаю. Может ты имел ввиду что-то другое?")


bot.polling(none_stop=True)
