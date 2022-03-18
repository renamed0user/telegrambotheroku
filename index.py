import logging
import os
import telebot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telebot import types
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5288239676:AAH40vF7Ymn41ODeJZYbTZKE-Wg1EbgkOoI'
APP_NAME='https://telebottobrother.herokuapp.com/'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def build_menu(buttons, n_cols=1, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, 2, n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def start(update, context):
    update.message.reply_text('Hi!')
    button_list = []
    for each in ["English", "Українська"]:
        button_list.append(InlineKeyboardButton(each, callback_data=each))
    update.message.reply_text('Hi!')
    reply_markup = InlineKeyboardMarkup(build_menu(button_list))
    update.message.reply_text('Hi!')
    context.bot.send_message(update.message.chat_id, "Choose a language\nВиберіть мову", reply_markup=markup)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Developed by @Renamed_user11\nYou can use this bot but not forget that it is not your property')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def button_press(update, context):
    if update.message.text=='English':
        update.message.reply_text('You choose English!')
    elif update.message.text=='Українська':
        update.message.reply_text('Ви вибрали Українську\nСлава Україні!\nСмерть москалям!')

def button_pressed(bot, update):
    query=update.callback_query
    bot.send_message(query.message.chat_id,str(query.data))
def main():
    """Start the bot."""

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(button_pressed))
    dp.add_handler(MessageHandler(Filters.text, button_press))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path=TOKEN,webhook_url=APP_NAME + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()