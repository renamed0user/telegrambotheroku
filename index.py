import os
import telebot
from flask import Flask, request
from telebot import types


PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5288239676:AAH40vF7Ymn41ODeJZYbTZKE-Wg1EbgkOoI'
APP_NAME='https://telebottobrother.herokuapp.com/'

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)
bot.deleteWebhook()

def cb_en(chat_id):
    bot.send_message(chat_id,"You choose English")

def cb_ua(chat_id):
    bot.send_message(chat_id,"Ви вибрали Українську\nСлава Україні!\nСмерть москалям!")

@bot.message_handler(commands=['start'])
def start(update, context):
    update.message.reply_text('Hi!')
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(types.InlineKeyboardButton("English",callback_data='cb_en:update.message.chat_id'),
                               types.InlineKeyboardButton("Українська",callback_data='cb_ua:update.message.chat_id'))
    bot.send_message(update.message.chat_id, "Choose a language\nВиберіть мову", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Developed by @Renamed_user11\nYou can use this bot but not forget that it is not your property')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


bot.set_webhook(APP_NAME + TOKEN)
app.run()

