#!/usr/bin/env python3

from itsctfbot import constants
from itsctfbot import config

from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup


def keyboard_inline():
    bot_link = 'https://t.me/{}'.format(constants.GET_ME.username)
    button0 = InlineKeyboardButton(text='Private chat', url=bot_link)

    button1 = InlineKeyboardButton(
        text='Source code',
        url='https://github.com/rikonaka/itsctfbot.git')
    buttons_list = [[button0, button1]]
    keyboard = InlineKeyboardMarkup(buttons_list)
    return keyboard


def keyboard_admin():
    '''Use the inline keyboard now.
    '''
    custom_keyboard = [['/maintenance']]
    # reply_markup = ReplyKeyboardMarkup(
    #     custom_keyboard, one_time_keyboard=True, selective=True)
    keyboard = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True, selective=True)

    # cid = update.message.chat.id
    # text = '<b>What\'s your choice?</b>'
    # bot.send_message(chat_id=cid, text=text,
    #                  parse_mode=ParseMode.HTML, reply_markup=reply_markup)
    # update.message.reply_text(
    #     text=text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)
    return keyboard


def keyboard_user():

    custom_keyboard = [['/help', '/ping', '/version']]
    keyboard = ReplyKeyboardMarkup(
        custom_keyboard, one_time_keyboard=True, selective=True)

    return keyboard
