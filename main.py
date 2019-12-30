#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

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


if __name__ == "__main__":
    bot.polling(none_stop=True)
