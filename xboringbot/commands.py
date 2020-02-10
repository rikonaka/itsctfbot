#!/usr/bin/env python3

import logging
import copy
import random
import time
from datetime import datetime
from datetime import timedelta

from xboringbot.utils import only_admin
# from xboringbot import keyboards
from xboringbot import messages
from xboringbot import utils
from xboringbot import config
from xboringbot import keyboards
from xboringbot import version
from xboringbot import ctf_flag

# from telegram import MessageEntity
from telegram import ParseMode
# from telegram import constants as t_consts
from telegram.ext.dispatcher import run_async
from telegram import TelegramError


@run_async
def job_load_flag(context):

    ctf_flag.load_flag()


@run_async
@only_admin
def command_maintenance(update, context):

    if config.maintenance_mode == False:
        config.maintenance_mode = True
        text = '<b>Maintenance mode enabled</b>'
        update.message.reply_text(text=text, parse_mode=ParseMode.HTML)

    elif config.maintenance_mode == True:
        config.maintenance_mode = False
        text = '<b>Maintenance mode disabled</b>'
        update.message.reply_text(text=text, parse_mode=ParseMode.HTML)


@run_async
def command_bot_version(update, context):
    current_version = version.version()
    start_time = config.bot_start_time
    end_time = time.time()
    text = 'xboringbot driven by v%s code.\nUptime: %s.' % (
        current_version, str(timedelta(seconds=int(end_time - start_time))))
    update.message.reply_text(
        text=text, parse_mode=ParseMode.HTML)


@run_async
def command_user_help(update, context):
    '''Show the help information for users.
    '''

    # keyboard = keyboards.keyboard_user()
    keyboard = keyboards.keyboard_inline()

    text = '叫爸爸干什么！'
    # update.message.reply_text(
    #     text=text, parse_mode=ParseMode.HTML, reply_markup=keyboard)
    update.message.reply_text(
        text=text, parse_mode=ParseMode.HTML, reply_markup=keyboard)


@run_async
def command_ping(update, context):
    '''for bot test.
    '''
    text = '再测试干你！'
    # update.message.reply_text(
    #     text=text, parse_mode=ParseMode.HTML, reply_markup=keyboard)
    update.message.reply_text(
        text=text, parse_mode=ParseMode.HTML)
