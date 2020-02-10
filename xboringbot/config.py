#!/usr/bin/env python3

import yaml
import sys
import logging


path = 'config/config.yaml'
if len(sys.argv) == 2:
    path = sys.argv[1]
try:
    with open(path, 'r') as stream:
        conf = yaml.load(stream, Loader=yaml.FullLoader)
except IOError:
    print('\nWARNING:\n'
          'before of running this bot you should create a file named `config.yaml` in `config`'
          '.\n\nOpen `config/config.example.yaml`'
          '\ncopy all'
          '\ncreate a file named `config.yaml`'
          '\nPaste and replace sample variables with true data.'
          '\nIf the file is in another path, you can specify it as the first parameter.')
    sys.exit()


BOT_TOKEN = conf['bot_token']
ADMINS = conf['admins']
ERROR_LOG = conf['error_log_location']


# default is False now.
# you should turn it off while the bot runing.
maintenance_mode = False
debug_mode = False
# the int time stamp.
bot_start_time = 0

# static vaule.
MAINTENANCE_TEXT = '<b>Sorry, this service is under maintenance, please check the administrator notification</b>'
NEW_USER_WELCOME_TEXT = '<b>😉%s，花姑娘？</b>'
MATERIAL_PATH = '/etc/'
NAME_TEXT = '%s个%s'
