import logging
import os
import telebot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5288239676:AAH40vF7Ymn41ODeJZYbTZKE-Wg1EbgkOoI'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text(update.message.message_id)
    bot = telebot.TeleBot('5288239676:AAH40vF7Ymn41ODeJZYbTZKE-Wg1EbgkOoI')
    update.message.reply_text(update.message.message_id)
    bot.send_message(update.message.chat_id,"df")
    markup = types.InlineKeyboardMarkup()
    update.message.reply_text(update.message.message_id)
    b1=types.InlineKeyboardButton(text='English', callback_data='English')
    update.message.reply_text(update.message.message_id)
    b2=types.InlineKeyboardButton(text='Українська', callback_data='Українська')
    b3=types.InlineKeyboardButton(text='Русский', callback_data='Русский')
    markup.add(b1,b2,b3)
    bot.send_message(update.message.chat_id.id,"dsf",reply_markup=markup)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Developed by renamed_user\nYou can use this but not forget that it is your property')


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
    APP_NAME='https://telebottobrother.herokuapp.com/'
    
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN,webhook_url=APP_NAME + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()