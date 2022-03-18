import logging
import os
import telebot

from telebot import types
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5288239676:AAH40vF7Ymn41ODeJZYbTZKE-Wg1EbgkOoI'
APP_NAME='https://telebottobrother.herokuapp.com/'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


bot = telebot.TeleBot(TOKEN)


def cb_en(update, context):
    bot.send_message(update.message.chat_id,"You choose English")

def cb_ua(update, context):
    bot.send_message(update.message.chat_id,"Ви вибрали Українську\nСлава Україні!\nСмерть москалям!")

def start(update, context):
    update.message.reply_text('Hi!')
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("English",callback_data='cb_en'),
                               types.InlineKeyboardButton("Українська",callback_data='cb_ua'))
    bot.send_message(update.message.chat_id, "Choose a language\nВиберіть мову", reply_markup=markup)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Developed by @Renamed_user11\nYou can use this bot but not forget that it is not your property')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN,webhook_url=APP_NAME + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()