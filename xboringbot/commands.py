#!/usr/bin/env python3

import logging
import copy
import random
import time
from datetime import datetime
from datetime import timedelta
import uuid

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
from telegram import InlineQueryResultArticle
from telegram import InputTextMessageContent


@run_async
def job_load_flag(context):

    ctf_flag.load_flag()


@run_async
@only_admin
def command_maintenance(update, context):

    if config.debug_mode == False:
        config.debug_mode = True
        text = '<b>Maintenance mode enabled</b>'
        update.message.reply_text(text=text, parse_mode=ParseMode.HTML)

    elif config.debug_mode == True:
        config.debug_mode = False
        text = '<b>Maintenance mode disabled</b>'
        update.message.reply_text(text=text, parse_mode=ParseMode.HTML)


@run_async
@only_admin
def command_debug(update, context):

    if config.debug_mode == False:
        config.debug_mode = True
        text = '<b>Debug mode enabled</b>'
        update.message.reply_text(text=text, parse_mode=ParseMode.HTML)

    elif config.debug_mode == True:
        config.debug_mode = False
        text = '<b>Debug mode disabled</b>'
        update.message.reply_text(text=text, parse_mode=ParseMode.HTML)


def command_check_flag_inline(update, context):
    '''
    '''

    text = update.inline_query.query
    text = text.strip()
    if len(text) == 0:
        return

    if 'flag' not in text:
        return

    uuid_me = uuid.uuid4()
    results = list()
    if ctf_flag.check_flag(text):
        # uid = update.inline_query.from_user.id
        username = update.inline_query.from_user.username
        correct_string = 'Good job!'
        username_with_correct_string = correct_string + ' ' + str(username)
        results.append(InlineQueryResultArticle(id=uuid_me, title=correct_string, description=username_with_correct_string,
                                                input_message_content=InputTextMessageContent(correct_string, parse_mode=ParseMode.HTML)))
        try:
            update.inline_query.answer(
                results, cache_time=60, is_personal=True)
        except Exception:
            pass
    else:
        username = update.inline_query.from_user.username
        not_correct_string = 'Sorry, %s your answer is not right!'
        username_with_not_correct_string = not_correct_string % str(username)
        results.append(InlineQueryResultArticle(id=uuid_me, title=correct_string, description=username_with_not_correct_string,
                                                input_message_content=InputTextMessageContent(correct_string, parse_mode=ParseMode.HTML)))
        try:
            update.inline_query.answer(
                results, cache_time=60, is_personal=True)
        except Exception:
            pass


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
