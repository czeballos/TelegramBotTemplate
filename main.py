#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

from telebot import TeleBot, types

from utils.commands import HELP_MESSAGE

token = os.environ['token']
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    # =====================================================
    # It respond including a reply of the original message.
    # bot.reply_to(message, 'Welcome!')
    # =====================================================

    bot.send_message(message.chat.id, 'Welcome!, use /help get a list of available commands')


@bot.message_handler(commands=['help'])
def help(message):
    """Return a list or available commands"""
    bot.send_message(message.chat.id, HELP_MESSAGE)


@bot.message_handler(commands=['cmd01'])
def save(message):
    """Asks for an input"""
    bot.send_message(message.chat.id, 'please write something')
    bot.register_next_step_handler(message, next_step)


def next_step(message):
    """Returns an answer for a previous input"""
    bot.send_message(message.chat.id, 'this is a response')


@bot.message_handler(commands=['cmd02'])
def photo(message):
    """Sends an image file"""
    with open('cat.png', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption='This is a title')


@bot.message_handler(commands=['cmd03'])
def audio(message):
    """Sends an audio file"""
    try:
        with open('audio.mp3', 'rb') as audio:
            bot.send_message(message.chat.id, 'Please wait, this can take a few minutes.')
            caption = 'message caption'             # Optional
            duration = 29                           # Optional
            performer = 'name of interpreter'       # Optional
            title = 'title song'                    # Optional
            bot.send_audio(message.chat.id, audio, caption=caption, duration=duration, performer=performer, title=title)
    except Exception as err:
        print(err)


@bot.message_handler(commands=['cmd04'])
def document(message):
    """Sends a document file"""
    try:
        with open('document.pdf', 'rb') as doc:
            bot.send_message(message.chat.id, 'Please wait, this can take a few minutes.')
            caption = 'message caption'             # Optional
            bot.send_document(message.chat.id, doc, caption=caption)
    except Exception as err:
        print(err)


@bot.message_handler(commands=['cmd05'])
def video(message):
    """Sends a video file"""
    try:
        with open('video.mp4', 'rb') as video:
            bot.send_message(message.chat.id, 'Please wait, this can take a few minutes.')
            caption = 'message caption'             # Optional
            duration = 105							# Optional
            bot.send_video(message.chat.id, video, caption=caption, duration=duration)
    except Exception as err:
        print(err)


@bot.message_handler(commands=['cmd06'])
def location(message):
    """Sends location"""
    lat = '-17.7833839'
    long = '-63.1822053'
    bot.send_location(message.chat.id, lat, long)


@bot.message_handler(commands=['cmd07'])
def action(message):
    """
    Sends location
    It must be some of following strings:
    typing,
    upload_photo,
    record_video,
    upload_video,
    record_audio,
    upload_audio,
    upload_document,
    find_location,
    record_video_note,
    upload_video_note
    """
    bot.send_chat_action(message.chat.id, 'typing')


@bot.message_handler(commands=['cmd08'])
def venue(message):
    """Sends location of a venue"""
    title = 'Venue\'s name'
    address = 'This is the venue\'s address'
    lat = '-17.783803'
    long = '-63.1810534'
    foursquare = '58a6357b4988da0f65e87610'         # Optional
    bot.send_venue(message.chat.id, lat, long, title=title, address=address, foursquare_id=foursquare)


@bot.message_handler(commands=['cmd09'])
def conctact(message):
    """Sends conctact's information"""
    phone = '+59177777777'
    first_name = 'John'
    last_name = 'Doe'
    bot.send_contact(message.chat.id, phone, first_name, last_name)


@bot.message_handler(commands=['cmd10'])
def button1(message):
    """Creates buttons with "add" function"""
    markup = types.ReplyKeyboardMarkup(row_width=5)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    itembtn4 = types.KeyboardButton('4')
    itembtn5 = types.KeyboardButton('5')
    itembtn6 = types.KeyboardButton('6')
    itembtn7 = types.KeyboardButton('7')
    itembtn8 = types.KeyboardButton('8')
    itembtn9 = types.KeyboardButton('9')
    itembtn10 = types.KeyboardButton('10')
    back = types.KeyboardButton('⬅️')
    cancel = types.KeyboardButton('❌')
    forward = types.KeyboardButton('➡️')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    markup.add(itembtn6, itembtn7, itembtn8, itembtn9, itembtn10)
    markup.add(back, cancel, forward)
    bot.send_message(message.chat.id, 'Press a button', reply_markup=markup)


@bot.message_handler(commands=['cmd11'])
def button2(message):
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    itembtn3 = types.KeyboardButton('3')
    itembtn4 = types.KeyboardButton('4')
    itembtn5 = types.KeyboardButton('5')
    itembtn6 = types.KeyboardButton('6')
    itembtn7 = types.KeyboardButton('7')
    itembtn8 = types.KeyboardButton('8')
    itembtn9 = types.KeyboardButton('9')
    itembtn10 = types.KeyboardButton('10')
    back = types.KeyboardButton('⬅️')
    cancel = types.KeyboardButton('❌')
    forward = types.KeyboardButton('➡️')
    markup.row(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    markup.row(itembtn6, itembtn7, itembtn8, itembtn9, itembtn10)
    markup.row(back, cancel, forward)
    bot.send_message(message.chat.id, 'Press a button', reply_markup=markup)


if __name__ == "__main__":
    bot.infinity_polling(True)
