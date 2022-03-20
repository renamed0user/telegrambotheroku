import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5124121118:AAH42elBsKKyC5IQmnPctrE2EBEifCPCzss'
APP_NAME='https://telebottobrother.herokuapp.com/'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def start(update, context):
    button_list = []
    for each in ["English", "Українська"]:
        button_list.append([InlineKeyboardButton(each, callback_data=each)])
    update.message.reply_text(text="Hello!\nChoose a language\nВиберіть мову", reply_markup=InlineKeyboardMarkup(button_list[:2]), parse_mode='HTML')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Developed by @Renamed_user11\nYou can use this bot but not forget that it is not your property')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def button_press(update, context):
    button_list = []
    if update.callback_query.data=='English':
        for each in ["Weather", "Weather"]:
            button_list.append([InlineKeyboardButton(each, callback_data=each)])
        update.message.reply_text(text="You choose English\nSelect tusk", reply_markup=InlineKeyboardMarkup(button_list[:2]), parse_mode='HTML')
    elif update.callback_query.data=='Українська':
        for each in ["Погода", "Погода"]:
            button_list.append([InlineKeyboardButton(each, callback_data=each)])
        update.message.reply_text(text="Ви вибрали Українську\nСлава Україні!\nСмерть москалям!\nОберіть завдання", reply_markup=InlineKeyboardMarkup(button_list[:2]), parse_mode='HTML')
    elif update.callback_query.data=='Weather' or update.callback_query.data=='Погода':
        update.message.reply_text('latitude: %s; longitude: %s'%(update.message.location.latitude,update.message.location.longitude))

 

def main():
    """Start the bot."""

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(button_press))
    dp.add_handler(MessageHandler(Filters.text, button_press))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN,webhook_url=APP_NAME + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
