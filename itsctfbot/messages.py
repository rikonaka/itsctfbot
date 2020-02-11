#!/usr/bin/env python3

import datetime
import random
from time import sleep

from telegram import ParseMode
from telegram.ext import DispatcherHandlerStop
from telegram.ext.dispatcher import run_async

from itsctfbot import keyboards
from itsctfbot import config
from itsctfbot import funny
from itsctfbot import ctf_flag
from itsctfbot.utils import only_admin
# from itsctfbot.utils import DeleteSameValueOrNot
from itsctfbot.utils import utils_check_admin


def _flag_process(update, context):

    number_string = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    message = update.message
    if message.text:
        if 'flag' in message.text and message.text[0] in number_string:
            if ctf_flag.check_flag(message.text):
                update.message.reply_text(text='Good job!')
            else:
                update.message.reply_text(
                    text='Sorry, your answer is not right!')


def _other_process(update, context):
    # text = 'Sorry, this kind of media is not supported yet'
    # text = 'Thanks'
    # message.reply_text(text=text, quote=True)
    return


def _game_process(update, context):
    # text = 'Sorry, telegram doesn't allow to echo this message'
    # message.reply_text(text=text, quote=True)
    return


def _video_note_process(update, context):
    # media = message.video_note.file_id
    # length = message.video_note.length
    # duration = message.video_note.duration
    # message.reply_video_note(video_note=media, length=length, duration=duration)
    return


def _location_process(update, context):
    # longitude = message.location.longitude
    # latitude = message.location.latitude
    # message.reply_location(latitude=latitude, longitude=longitude)
    return


def _venue_process(update, context):
    # longitude = message.venue.location.longitude
    # latitude = message.venue.location.latitude
    # title = message.venue.title
    # address = message.venue.address
    # foursquare_id = message.venue.foursquare_id
    # message.reply_venue(longitude=longitude, latitude=latitude, title=title, address=address, foursquare_id=foursquare_id)
    return


def _contact_process(update, context):
    # phone_number = message.contact.phone_number
    # first_name = message.contact.first_name
    # last_name = message.contact.last_name
    # message.reply_contact(phone_number=phone_number, first_name=first_name, last_name=last_name)
    # re_text = '<b>What is this?</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _video_process(update, context):
    # media = message.video.file_id
    # duration = message.video.duration
    # message.reply_video(video=media, duration=duration, caption=caption, parse_mode=ParseMode.HTML)
    # re_text = '<b>Excellent~~ o(*￣▽￣*)ブ</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _audio_process(update, context):
    # media = message.audio.file_id
    # duration = message.audio.duration
    # performer = message.audio.performer
    # title = message.audio.title
    # message.reply_audio(audio=media, duration=duration, performer=performer, title=title, caption=caption, parse_mode=ParseMode.HTML)
    # re_text = '<b>What is this?</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _document_process(update, context):
    # media = message.document.file_id
    # filename = message.document.file_name
    # message.reply_document(document=media, filename=filename, caption=caption, parse_mode=ParseMode.HTML)
    # re_text = '<b>What is this?</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _animation_process(update, context):
    # for gif
    # re_text = '<b>Wow!</b>'
    # message.reply_text(text=re_text, parse_mode=ParseMode.HTML)
    return


def _sticker_process(update, context):
    # media = message.sticker.file_id
    # message.reply_sticker(sticker=media)
    return


def _photo_process(update, context):
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


def _voice_process(update, context):
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


def _delete_process(update, context):

    cid = update.message.chat.id
    mid = update.messge.message_id
    text = update.message.text

    first_name = update.message.from_user.first_name

    if not cid or not mid or not text or not first_name:
        return

    if '考' in text or '404' in first_name:
        re_text = '再逼逼干你信不信！'
        context.bot.send_message(
            chat_id=cid, text=re_text, parse_mode=ParseMode.HTML)
        sleep(5)
        context.bot.delete_message(chat_id=cid, message_id=mid)

    return


def _text_process_pink(update, context):

    cid = update.message.chat.id

    re_text = funny.get_random_pink_quotes()
    context.bot.send_message(chat_id=cid, text=re_text,
                             parse_mode=ParseMode.HTML)
    return


def _text_process(update, context):
    '''Process the text.
    '''
    cid = update.message.chat.id

    # print(message.text)
    verb = funny.check_verb(str(update.message.text).strip())
    if not verb:
        return

    name = funny.get_random_name()
    re_text = config.NAME_TEXT % (verb, name)
    context.bot.send_message(chat_id=cid, text=re_text,
                             parse_mode=ParseMode.HTML)
    return


def _supergroup_chat_process(update, context):
    '''
    for normal user use
    '''

    message = update.message

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

        context.bot.send_message(
            chat_id=cid, text=re_text, parse_mode=ParseMode.HTML)
        return

    if message.text:
        # add 1/100.
        _delete_process(update, context)

        if config.debug_mode:
            _text_process(update, context)
            _text_process_pink(update, context)

        elif 'flag' in message.text:
            # print(message.text)
            _flag_process(update, context)

        else:
            i = random.randint(0, 29)
            if i == 24:
                _text_process(update, context)
                _text_process_pink(update, context)

    elif message.voice:
        _voice_process(update, context)

    elif message.photo:
        _photo_process(update, context)

    elif message.sticker:
        _sticker_process(update, context)

    elif message.animation:
        _animation_process(update, context)

    elif message.document:
        _document_process(update, context)

    elif message.audio:
        _audio_process(update, context)

    elif message.video:
        _video_process(update, context)

    elif message.contact:
        _contact_process(update, context)

    elif message.venue:
        _venue_process(update, context)

    elif message.location:
        _location_process(update, context)

    elif message.video_note:
        _video_note_process(update, context)

    elif message.game:
        _game_process(update, context)

    else:
        _other_process(update, context)


@run_async
def _private_chat_process(update, context):
    '''Let the bot check the flag now.
    '''

    _flag_process(update, context)

    return


@run_async
def message_process(update, context):

    if update.message:
        if update.message.chat.type == 'private':
            # only the admin allow the use the private chat or submission
            # print('here')
            _private_chat_process(update, context)

        elif update.message.chat.type == 'supergroup':
            _supergroup_chat_process(update, context)
    else:
        return
