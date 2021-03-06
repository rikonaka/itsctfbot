#!/usr/bin/env python3

# python lib
import logging
from threading import Thread
import sys
import os
import time

# files
from itsctfbot import config
from itsctfbot import commands
from itsctfbot import messages
from itsctfbot import utils
from itsctfbot import custom_filters
from itsctfbot import version

# use the python-telegram-bot lib
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update, context, error):
    logger.warning('Update %s caused error %s' % (update, error))


def main():

    current_version = version.version()
    running_message = 'itsctfbot: v%s\nrunning...' % current_version
    print(running_message)

    config.bot_start_time = time.time()

    updater = Updater(token=config.BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    # def stop_and_restart():
    #     '''Gracefully stop the Updater and replace the current process with a new one'''
    #     updater.stop()
    #     os.execl(sys.executable, sys.executable, *sys.argv)

    # def restart(update, context):
    #     update.message.reply_text('Bot is restarting...')
    #     Thread(target=stop_and_restart).start()

    # job = updater.job_queue
    # dp.add_handler(MessageHandler(custom_filters.album,
    #                               albums.album_collect, pass_job_queue=True), 1)
    job = updater.job_queue
    job.run_repeating(
        commands.job_load_flag, interval=6, first=0)
    dp.add_handler(MessageHandler(
        Filters.all, messages.message_process), 1)

    '''Administrator commands'''

    dp.add_handler(CommandHandler('maintenance',
                                  commands.command_maintenance), 2)
    dp.add_handler(CommandHandler('debug',
                                  commands.command_debug), 2)

    '''User's command'''

    dp.add_handler(CommandHandler('help', commands.command_user_help), 2)
    dp.add_handler(CommandHandler('ping', commands.command_ping), 2)
    dp.add_handler(CommandHandler('version', commands.command_bot_version), 2)
    dp.add_handler(MessageHandler(Filters.command, utils.invalid_command), 2)

    '''Add inline query handle.'''
    dp.add_handler(InlineQueryHandler(commands.command_check_flag_inline))

    # handle errors
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
