#!/usr/bin/env python3

from xboringbot import constants
from xboringbot import config

from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup


def keyboard_github_link():
    button0 = InlineKeyboardButton(
        text='Source code',
        url='https://github.com/xxx/xxx.git')
    buttons_list = [[button0]]
    keyboard = InlineKeyboardMarkup(buttons_list)
    return keyboard


def keyboard_private_chat():
    bot_link = 'https://t.me/{}'.format(constants.GET_ME.username)
    button0 = InlineKeyboardButton(text='Private chat', url=bot_link)
    buttons_list = [[button0]]
    keyboard = InlineKeyboardMarkup(buttons_list)
    return keyboard


def keyboard_admin(bot, update):
    '''
    show the help icon for admin
    '''
    custom_keyboard = [['/maintenance']]
    # reply_markup = ReplyKeyboardMarkup(
    #     custom_keyboard, one_time_keyboard=True, selective=True)
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    # cid = update.message.chat.id
    text = '<b>What\'s your choice?</b>'
    # bot.send_message(chat_id=cid, text=text,
    #                  parse_mode=ParseMode.HTML, reply_markup=reply_markup)
    update.message.reply_text(
        text=text, parse_mode=ParseMode.HTML, reply_markup=reply_markup)


def keyboard_user(bot, update):

    custom_keyboard = [['/help', '/ping', '/version']]
    reply_markup = ReplyKeyboardMarkup(
        custom_keyboard, one_time_keyboard=True, selective=True)

    return reply_markup
