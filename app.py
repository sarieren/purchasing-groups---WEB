#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
from module_study_word import menu_study_word
from module_test_word import menu_test_word
from translate_word import menu_translate_word
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO, TESTS = range(5)

g =""
def start_menu(update: Update, context: CallbackContext):
    reply_keyboard = [['translate', 'study_word', 'quiz']]
    update.message.reply_text(
        'please choose ',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

def start(update: Update, context: CallbackContext) -> int:
    start_menu(update,CallbackContext)
    print("in start")
    print(update.message.text)
    return GENDER

def gender(update: Update, context: CallbackContext) -> int:
    print("in gender")
    user = update.message.from_user
    if(update.message.text=="study_word" or update.message.text=="next" ):
        s=menu_study_word(update.effective_chat.id,"/study_word")
        context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(s))
        reply_keyboard = [['next', 'go_back']]
        update.message.reply_text(
            'hey',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return PHOTO
    if(update.message.text=="go_back"):
        start_menu(update, CallbackContext)
        return GENDER
    if(update.message.text=="translate"):
        update.message.reply_text('please enter a word')
        return BIO
    if update.message.text== "quiz" or update.message.text== "more_test":
        reply_keyboard = [['words_test'], ['photo_test'],['go_back']]
        update.message.reply_text(
            'hey',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
        return GENDER
    if (update.message.text == "words_test"):
           s=menu_test_word(update.effective_chat.id,"/test")
           update.message.reply_text(s)
           return LOCATION
    else:
        print("here")
        print(update.message.text)
        return ConversationHandler.END

def photo(update: Update, context: CallbackContext) -> int:
    print("in photo")
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download('user_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, 'user_photo.jpg')
    update.message.reply_text(
        'Gorgeous! Now, send me your location please, ' 'or send /skip if you don\'t want to.'
    )

    return LOCATION


def skip_photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a photo.", user.first_name)
    update.message.reply_text(
        'I bet you look great! Now, send me your location please, ' 'or send /skip.'
    )

    return LOCATION


def location(update: Update, context: CallbackContext) -> int:
    if (update.message.text == "go_back"):
        start_menu(update, CallbackContext)
        return GENDER
    print("in location")
    s = menu_test_word(update.effective_chat.id, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(s))
    reply_keyboard = [['more_test', 'go_back']]
    update.message.reply_text(
        'hey',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )
    return GENDER


def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'You seem a bit paranoid! ' 'At last, tell me something about yourself.'
    )

    return BIO


def bio(update: Update, context: CallbackContext) -> int:
    print("in bio")
    if (update.message.text == "go_back"):
        start_menu(update, CallbackContext)
        return GENDER
    user = update.message.from_user
    s=menu_translate_word(update.effective_chat.id, update.message.text)
    update.message.reply_text(s)
    reply_keyboard = [['go_back']]
    update.message.reply_text(
            'hey',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
    return BIO
def tests(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['words_test'],['photo_test']]
    update.message.reply_text(
            'hey',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can talk again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN = '1267251022:AAGxFzIuefMui68W-YF-gHBg2nv08CJ1Vd8'

    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            GENDER: [MessageHandler(Filters.regex('^(translate|study_word|quiz|go_back|more_test|words_test|photo_test)$'), gender)],
            PHOTO: [MessageHandler(Filters.regex('^(next|go_back|more_test)$'), gender)],
            LOCATION: [MessageHandler(Filters.text & ~Filters.command, location)],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
            TESTS: [MessageHandler(Filters.regex('^(words_test|photo_test)$'), tests)]
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()