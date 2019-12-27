import os

import telebot

token = os.environ['token']
bot = telebot.TeleBot(token)


@bot.message_handler(commands='start')
def start(message):
    bot.reply_to(message, 'Welcome!')


if __name__ == "__main__":
    bot.polling()
