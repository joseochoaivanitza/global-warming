import telebot
from fact import *

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("global_warming")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = get_fact()
    bot.reply_to(message, fact)

@bot.message_handler(commands=['reasons'])
def send_fact(message):
    reasons = get_reasons()
    bot.reply_to(message, reasons)

@bot.message_handler(commands=['prevention'])
def send_fact(message):
    prevention = get_prevention()
    bot.reply_to(message, prevention)

# Запускаем бота
bot.polling()
