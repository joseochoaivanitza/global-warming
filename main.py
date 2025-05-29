import telebot
import os
import random
from fact import *

def get_random_image(folder):
    images = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
    return os.path.join(folder, random.choice(images)) if images else None

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("no")

@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_text = (
        "Здравствуйте! Я бот, посвящённый вопросам глобального потепления и изменений климата.\n"
        "Используйте команду /info, чтобы узнать больше обо мне.\n"
        "Если вам нужно список команд, введите /commands.\n"
        "Чего бы вы хотели узнать сегодня?"
    )
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = get_fact()
    bot.reply_to(message, fact)

@bot.message_handler(commands=['reasons'])
def reasons_command(message):
    image_path = get_random_image('image_reasons')
    caption = get_reasons()
    if image_path:
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=caption)

@bot.message_handler(commands=['prevention'])
def prevention_command(message):
    image_path = get_random_image('image_prevention')
    caption = get_prevention()
    if image_path:
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=caption)

@bot.message_handler(commands=['commands'])
def send_commands_list(message):
    commands_text = (
        "/start - начать взаимодействие с ботом\n"
        "/info - информация о боте\n"
        "/commands - список команд\n"
        "/credits - информация о создателе\n"
        "/fact - интересный факт о глобальном потеплении\n"
        "/reasons - причины глобального потепления\n"
        "/prevention - меры по предотвращению\n"
    )
    bot.send_message(message.chat.id, commands_text)


@bot.message_handler(commands=['credits'])
def send_credits(message):
    credits_text = "Этот бот создан Эриком — увлечённым разработчиком и геймером. Спасибо за использование!"
    bot.send_message(message.chat.id, credits_text)

@bot.message_handler(commands=['info'])
def send_bot_info(message):
    info_text = ("Я — Telegram-бот, созданный для предоставления информации о глобальном потеплении. "
                 "Моя цель — помочь вам узнать больше о причинах, последствиях и мерах по борьбе с изменением климата. "
                 "Используйте команды /commands, чтобы ознакомиться со всеми возможностями бота, и /credits, чтобы узнать о создателе.")
    bot.send_message(message.chat.id, info_text)

# Запускаем бота
bot.polling()
