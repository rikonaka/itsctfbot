#!/usr/bin/env python3
import random

from xboringbot import config
from xboringbot.utils import utils_get_line

def random_verb():
    path = config.MATERIAL_PATH + 'verb_chinese'

    verb_list = utils_get_line(path)
    if not verb_list:
        return None

    return random.choice(verb_list)


def random_name():
    path = config.MATERIAL_PATH + 'name_chinese'

    name_list = utils_get_line(path)
    if not name_list:
        return None

    return random.choice(name_list)

    