#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

import telebot

from utils.commands import *

token = os.environ['token']
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    # ================================================================================
    # It respond including a reply of the original message.
    # bot.reply_to(message, 'Welcome!')
    # ================================================================================

    bot.send_message(message.chat.id, 'Welcome!')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)


if __name__ == "__main__":
    bot.polling()
