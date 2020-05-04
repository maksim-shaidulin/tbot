import os
import telebot
from telebot import apihelper

token = os.getenv("TOKEN")

bot = telebot.TeleBot(token)

@bot.message_handler()
def hangle_message(message):
    print(message.text)
    bot.send_message(message.chat.id, f'You said: {message.text}')
    # bot.send_location(message.chat.id, 55,55)

bot.polling()

