import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, ParseMode
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
from picture_test import get_url, check_result_picture
from test_after_translate import test_after_translate
from translate_word import menu_translate_word

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

GENDER, PHOTO, LOCATION, BIO, TESTS = range(5)

def start_menu(update: Update, context: CallbackContext):
    reply_keyboard = [['Translate Words 🌏', 'Study Words 📚', 'Take A Quiz 📝']]

    update.message.reply_text(
        '<i> Please Click An Option 👇🏻 </i>',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),parse_mode=ParseMode.HTML
    )

def start(update: Update, context: CallbackContext) -> int:
    start_menu(update,CallbackContext)
    return GENDER

def gender(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    if(update.message.text == 'Study Words 📚' or update.message.text == 'Next Word ➡️' ):
        s = menu_study_word(update.effective_chat.id,'/study_word')
        context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(s),parse_mode=ParseMode.HTML)
        reply_keyboard = [['Next Word ➡️', 'Go Back To Menu ↩️']]
        update.message.reply_text(
            '<i> Please Click An Option 👇🏻</i>',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),parse_mode=ParseMode.HTML
        )
        return PHOTO

    if(update.message.text == 'Go Back To Menu ↩️'):
        start_menu(update, CallbackContext)
        return GENDER
    if(update.message.text == 'Translate Words 🌏'):
        update.message.reply_text('Please Enter A Word To Translate')
        return BIO
    if(update.message.text == "Lets Go To Test 📝"):
        update.message.reply_text(test_after_translate(update.effective_chat.id))
        return LOCATION
    if update.message.text == 'Take A Quiz 📝' or update.message.text == 'For Another Test 📝':
        reply_keyboard = [['Test On Words 🆎'], ['Test On Images 🌅'], ['Go Back To Menu ↩️']]
        update.message.reply_text(
            '<i> Please Click An Option 👇🏻</i>',
            reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),parse_mode=ParseMode.HTML
        )
        return GENDER
    if (update.message.text == 'Test On Words 🆎'):
           s = menu_test_word(update.effective_chat.id,'/test')
           update.message.reply_text(s, parse_mode=ParseMode.HTML)
           return LOCATION
    if (update.message.text == 'Test On Images 🌅'):
           s = get_url(update.effective_chat.id)
           update.message.reply_text(s, parse_mode=ParseMode.HTML)
           return TESTS
    else:
        return ConversationHandler.END


def location(update: Update, context: CallbackContext) -> int:
    if (update.message.text == 'Go Back To Menu ↩️'):
        start_menu(update, CallbackContext)
        return GENDER
    s = menu_test_word(update.effective_chat.id, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(s), parse_mode=ParseMode.HTML)
    reply_keyboard = [['For Another Test 📝', 'Go Back To Menu ↩️']]
    update.message.reply_text(
        '<i> Please Click An Option 👇🏻</i>',
        reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),parse_mode=ParseMode.HTML
    )
    return GENDER

def bio(update: Update, context: CallbackContext) -> int:
    if (update.message.text == "Lets Go To Test 📝"):
        s = test_after_translate(update.effective_chat.id)
        update.message.reply_text(s, parse_mode=ParseMode.HTML)
        return LOCATION
    if (update.message.text == 'Go Back To Menu ↩️'):
        start_menu(update, CallbackContext)
        return GENDER
    user = update.message.from_user
    s = menu_translate_word(update.effective_chat.id, update.message.text)
    split_s = s.split('\n\n')
    update.message.reply_text(split_s[0], parse_mode=ParseMode.HTML)
    reply_keyboard = [["Lets Go To Test 📝"]]
    update.message.reply_text(
            split_s[1],
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),parse_mode=ParseMode.HTML
        )
    return BIO

def tests(update: Update, context: CallbackContext) -> int:
    if (update.message.text == 'Go Back To Menu ↩️'):
        start_menu(update, CallbackContext)
        return GENDER
    s = check_result_picture(update.effective_chat.id, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(s), parse_mode=ParseMode.HTML)
    reply_keyboard = [['For Another Test 📝', 'Go Back To Menu ↩️']]
    update.message.reply_text(
       '<i> Please Click An Option 👇🏻</i>',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),parse_mode=ParseMode.HTML
    )
    return GENDER

def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'Bye! I hope we can learn English together again some day.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN = '1435032122:AAEmEoNH8Empwoo9OMQbvk2J8VWfBKw_Tk0'

    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            GENDER: [MessageHandler(Filters.regex('^(Translate Words 🌏|Study Words 📚|Take A Quiz 📝|Go Back To Menu ↩️|For Another Test 📝|Test On Words 🆎|Test On Images 🌅)$'), gender)],
            PHOTO: [MessageHandler(Filters.regex('^(Next Word ➡️|Go Back To Menu ↩️|For Another Test 📝)$'), gender)],
            LOCATION: [MessageHandler(Filters.text & ~Filters.command, location)],
            BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
            TESTS: [MessageHandler(Filters.text & ~Filters.command, tests)]
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



main()