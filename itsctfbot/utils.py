#!/usr/bin/env python3

import random

from functools import wraps
from itsctfbot import config

from telegram.ext.dispatcher import run_async
from telegram import ParseMode


def utils_check_admin(update):
    '''Check the user is administrator or not.

    Returns:
        True(bool): if this guy is admin.
        False(bool): if this guy not admin.
    '''
    uid = str(update.message.from_user.id)
    if uid not in config.ADMINS:
        return False
    else:
        return True


def utils_get_line(path):
    '''
    Args:
        path: is the whole path of the text file.

    Returns:
        A list.
        None.
    '''
    if path:
        fp = open(path, 'r')
        rlist = list()
        for c in fp.readlines():
            if '#' not in c:
                rlist.append(c)
        return rlist
    else:
        return None


def invalid_command(update, context):
    text = 'this command is invalid'
    update.message.reply_text(text=text, quote=True)
    pass


def only_admin(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        if str(update.message.from_user.id) not in config.ADMINS:
            invalid_command(update, context, *args, **kwargs)
        else:
            return func(update, context, *args, **kwargs)
    return wrapped
