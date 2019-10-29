#!/usr/bin/env python3

import datetime
import random

from telegram import ParseMode
from telegram.ext import DispatcherHandlerStop
from telegram.ext.dispatcher import run_async

from xboringbot import keyboards
from xboringbot import config
from xboringbot import funny
from xboringbot.utils import only_admin
# from xboringbot.utils import DeleteSameValueOrNot
from xboringbot.utils import utils_check_admin
from xboringbot import log


def _other_process(bot, update, message):
    # text = 'Sorry, this kind of media is not supported yet'
    # text = 'Thanks'
    # message.reply_text(text=text, quote=True)
    return


def _game_process(bot, update, message):
    # text = 'Sorry, telegram doesn't allow to echo this message'
    # message.reply_text(text=text, quote=True)
    return


def _video_note_process(bot, update, message):
    # media = message.video_note.file_id
    # length = message.video_note.length
    # duration = message.video_note.duration
    # message.reply_video_note(video_note=media, length=length, duration=duration)
    return


def _location_process(bot, update, message):
    # longitude = message.location.longitude
    # latitude = message.location.latitude
    # message.reply_location(latitude=latitude, longitude=longitude)
    return


def _venue_process(bot, update, message):
    # longitude = message.venue.location.longitude
    # latitude = message.venue.location.latitude
    # title = message.venue.title
    # address = message.venue.address
    # foursquare_id = message.venue.foursquare_id
    # message.reply_venue(longitude=longitude, latitude=latitude, title=title, address=address, foursquare_id=foursquare_id)
    return


def _contact_process(bot, update, message):
    # phone_number = message.contact.phone_number
    # first_name = message.contact.first_name
    # last_name = message.contact.last_name
    # message.reply_contact(phone_number=phone_number, first_name=first_name, last_name=last_name)
    # re_text = '<b>What is this?</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _video_process(bot, update, message):
    # media = message.video.file_id
    # duration = message.video.duration
    # message.reply_video(video=media, duration=duration, caption=caption, parse_mode=ParseMode.HTML)
    # re_text = '<b>Excellent~~ o(*￣▽￣*)ブ</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _audio_process(bot, update, message):
    # media = message.audio.file_id
    # duration = message.audio.duration
    # performer = message.audio.performer
    # title = message.audio.title
    # message.reply_audio(audio=media, duration=duration, performer=performer, title=title, caption=caption, parse_mode=ParseMode.HTML)
    # re_text = '<b>What is this?</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _document_process(bot, update, message):
    # media = message.document.file_id
    # filename = message.document.file_name
    # message.reply_document(document=media, filename=filename, caption=caption, parse_mode=ParseMode.HTML)
    # re_text = '<b>What is this?</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _animation_process(bot, update, message):
    # for gif
    # re_text = '<b>Wow!</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _sticker_process(bot, update, message):
    # media = message.sticker.file_id
    # message.reply_sticker(sticker=media)
    return


def _photo_process(bot, update, message):
    '''
    '''
    # This is what the bot do now
    # we will send all the message
    # media = message.photo[-1].file_id
    # from_chat_id = message.chat.id
    # config.FROM_CHAT_ID_LIST.append(from_chat_id)

    # message_id = message.message_id
    # config.MESSAGE_ID_LIST.append(message_id)
    # message.reply_photo(photo=media, caption=caption, parse_mode=ParseMode.HTML)
    # re_text = '<b>Excellent~~ o(*￣▽￣*)ブ</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _voice_process(bot, update, message):
    '''
    '''
    # media = message.voice.file_id
    # duration = message.voice.duration
    # message.reply_voice(voice=media, duration=duration, caption=caption, parse_mode=ParseMode.HTML)
    # if util_appreciate_list_delay(update) == True:
    #     return
    # re_text = '<b>What is this?</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _text_process(bot, update, message):
    '''Process the text.
    '''
    cid = message.chat.id

    # print(message.text)
    verb = funny.check_verb(str(message.text).strip())
    if not verb:
        return

    # print(verb)

    name = funny.get_random_name()
    re_text = config.NAME_TEXT % (verb, name)
    bot.send_message(chat_id=cid, text=re_text, parse_mode=ParseMode.HTML)
    return


def _supergroup_chat_process(bot, update, message, caption):
    '''
    for normal user use
    '''

    if message.from_user:
        user_first_name = message.from_user.first_name
        user_last_name = message.from_user.last_name

        if user_first_name == 'Telegram' and user_last_name == 'Updates':
            return

    # welcome the new user
    if message.new_chat_members:
        cid = message.chat.id
        re_text = config.NEW_USER_WELCOME_TEXT % str(
            message.new_chat_members[0].first_name)

        bot.send_message(chat_id=cid, text=re_text, parse_mode=ParseMode.HTML)
        return

    if message.text:
        # add 1/100.
        i = random.randint(0, 99)
        if i == 88:
            _text_process(bot, update, message)

    elif message.voice:
        _voice_process(bot, update, message)

    elif message.photo:
        _photo_process(bot, update, message)

    elif message.sticker:
        _sticker_process(bot, update, message)

    elif message.animation:
        _animation_process(bot, update, message)

    elif message.document:
        _document_process(bot, update, message)

    elif message.audio:
        _audio_process(bot, update, message)

    elif message.video:
        _video_process(bot, update, message)

    elif message.contact:
        _contact_process(bot, update, message)

    elif message.venue:
        _venue_process(bot, update, message)

    elif message.location:
        _location_process(bot, update, message)

    elif message.video_note:
        _video_note_process(bot, update, message)

    elif message.game:
        _game_process(bot, update, message)

    else:
        _other_process(bot, update, message)


@run_async
def _private_chat_process(bot, update, message, caption):
    '''Doing nothing here.
    '''
    return


@run_async
def message_process(bot, update, remove_caption=False, custom_caption=None):

    if update.edited_message:
        message = update.edited_message
    elif remove_caption:
        message = update.message.reply_to_message
    elif custom_caption is not None:
        message = update.message.reply_to_message
    else:
        message = update.message

    if custom_caption is None:
        # caption is message title.
        try:
            caption = message.caption_html if (
                message.caption and remove_caption is False) else None
        except AttributeError:
            return
    else:
        caption = custom_caption

    # print(message.text)

    if message:
        if message.chat.type == 'private':
            # only the admin allow the use the private chat or submission
            # print('here')
            _private_chat_process(bot, update, message, caption)

        elif message.chat.type == 'supergroup':
            _supergroup_chat_process(bot, update, message, caption)
    else:
        return
