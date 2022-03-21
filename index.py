import logging
import os
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5124121118:AAH42elBsKKyC5IQmnPctrE2EBEifCPCzss'
APP_NAME='https://telebottobrother.herokuapp.com/'
OPENWEATHER_API='d80a4a56bbbc6aad2f5aeabaeab2cdaf'
config_dict = get_default_config()
config_dict['language'] = 'ua'
owm = OWM(OPENWEATHER_API, config_dict)
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
        for each in ["Weather"]:
            button_list.append([KeyboardButton(each, request_location=True)])
        context.bot.send_message(update.callback_query.message.chat_id,text="You choose English\nSelect tusk", reply_markup=ReplyKeyboardMarkup(button_list[:1]), parse_mode='HTML')
    elif update.callback_query.data=='Українська':
        for each in ["Погода"]:
            button_list.append([KeyboardButton(each, request_location=True)])
        context.bot.send_message(update.callback_query.message.chat_id,text="Ви вибрали Українську\nСлава Україні!\nСмерть москалям!\nОберіть завдання", reply_markup=ReplyKeyboardMarkup(button_list[:1]), parse_mode='HTML')
 
def get_weather(update, context):
    Lat=update.message.location.latitude
    Lng=update.message.location.longitude
    mg=owm.weather_manager()
    weather=mg.weather_around_coords(Lat, Lng).weather
    temp = weather.temperature('celsius')['temp']
    status = weather.detailed_status
    context.bot.send_message(update.message.chat_id,text='yfjgfjh')

def main():
    """Start the bot."""

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(button_press))
    dp.add_handler(MessageHandler(Filters.text, button_press))
    dp.add_handler(MessageHandler(Filters.location, get_weather))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN,webhook_url=APP_NAME + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
