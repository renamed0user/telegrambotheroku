import os
import telebot
from aiohttp import web
from telebot import types


PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5288239676:AAH40vF7Ymn41ODeJZYbTZKE-Wg1EbgkOoI'
APP_NAME='https://telebottobrother.herokuapp.com/'

app = web.Application(APP_NAME,PORT)
bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()

async def handle(request):
    if request.match_info.get("token") == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)

app.router.add_post("/{token}/", handle)
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

web.run_app(app)
