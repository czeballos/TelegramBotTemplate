#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import telebot

from utils.commands import *

token = os.environ['token']
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    # =====================================================
    # It respond including a reply of the original message.
    # bot.reply_to(message, 'Welcome!')
    # =====================================================

    bot.send_message(message.chat.id, 'Welcome!')


@bot.message_handler(commands=['help'])
def help(message):
    """Return a list or available commands"""
    bot.send_message(message.chat.id, HELP_MESSAGE)


@bot.message_handler(commands=['cmd1'])
def save(message):
    """Asks for an input"""
    bot.send_message(message.chat.id, 'please write something')
    bot.register_next_step_handler(message, next_step)


def next_step(message):
    """Returns an answer for a previous input"""
    bot.send_message(message.chat.id, 'this is a response')


@bot.message_handler(commands=['cmd2'])
def photo(message):
    """Sends an image file"""
    with open('cat.png', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption='This is a title')


@bot.message_handler(commands=['cmd3'])
def audio(message):
    """Sends an audio file"""
    try:
        with open('audio.mp3', 'rb') as audio:
            bot.send_message(message.chat.id, 'Please wait, this can take a few minutes.')
            caption = 'message caption'             # Optional
            duration = 20                           # Optional
            performer = 'name of interpreter'       # Optional
            title = 'title song'                    # Optional
            bot.send_audio(message.chat.id, audio, caption=caption, duration=duration, performer=performer, title=title)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    bot.infinity_polling(True)
