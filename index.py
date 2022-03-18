import logging
import os
import telebot
import config
from telebot import types

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


bot = telebot.TeleBot(config.TOKEN)

def start(update, context):
    update.message.reply_text('Hi!')
    b1=types.KeyboardButton('English')
    b2=types.KeyboardButton('Українська')
    b3=types.KeyboardButton('Русский')
    update.message.reply_text('Hi!')
    markup = types.ReplyKeyboardMarkup()
    update.message.reply_text('Hi!')
    markup.add(b1,b2,b3)
    update.message.reply_text('Hi!')
    bot.send_message(update.message.chat_id, "Choose a language\nВиберіть мову\nВыберите язык", reply_markup=markup)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Developed by @Renamed_user11\nYou can use this bot but not forget that it is not your property')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    
    updater = Updater(config.TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",port=config.PORT,url_path=config.TOKEN,webhook_url=config.APP_NAME + congig.TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()