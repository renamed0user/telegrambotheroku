import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5288239676:AAH40vF7Ymn41ODeJZYbTZKE-Wg1EbgkOoI'
APP_NAME='https://telebottobrother.herokuapp.com/'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



def start(update, context):
    update.message.reply_text('Hi!')
    button_list = []
    for each in ["English", "Українська"]:
        button_list.append(InlineKeyboardButton(each, callback_data=each))
    update.message.reply_text('Hi!')
    reply_markup = InlineKeyboardMarkup(button_list)
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

class InlineKeyboardMarkup(ReplyMarkup):
    """
    This object represents an inline keyboard that appears right next to the message it belongs to.
    Objects of this class are comparable in terms of equality. Two objects of this class are
    considered equal, if their the size of :attr:`inline_keyboard` and all the buttons are equal.
    Args:
        inline_keyboard (List[List[:class:`telegram.InlineKeyboardButton`]]): List of button rows,
            each represented by a list of InlineKeyboardButton objects.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.
    Attributes:
        inline_keyboard (List[List[:class:`telegram.InlineKeyboardButton`]]): List of button rows,
            each represented by a list of InlineKeyboardButton objects.
    """

    __slots__ = ('inline_keyboard', '_id_attrs')

    def __init__(self, inline_keyboard: List[List[InlineKeyboardButton]], **_kwargs: Any):
        # Required
        self.inline_keyboard = inline_keyboard

        self._id_attrs = (self.inline_keyboard,)

    def to_dict(self) -> JSONDict:
        """See :meth:`telegram.TelegramObject.to_dict`."""
        data = super().to_dict()

        data['inline_keyboard'] = []
        for inline_keyboard in self.inline_keyboard:
            data['inline_keyboard'].append([x.to_dict() for x in inline_keyboard])

        return data

    @classmethod
    def de_json(cls, data: Optional[JSONDict], bot: 'Bot') -> Optional['InlineKeyboardMarkup']:
        """See :meth:`telegram.TelegramObject.de_json`."""
        data = cls._parse_data(data)

        if not data:
            return None

        keyboard = []
        for row in data['inline_keyboard']:
            tmp = []
            for col in row:
                btn = InlineKeyboardButton.de_json(col, bot)
                if btn:
                    tmp.append(btn)
            keyboard.append(tmp)

        return cls(keyboard)

    @classmethod
    def from_button(cls, button: InlineKeyboardButton, **kwargs: object) -> 'InlineKeyboardMarkup':
        """Shortcut for::
            InlineKeyboardMarkup([[button]], **kwargs)
        Return an InlineKeyboardMarkup from a single InlineKeyboardButton
        Args:
            button (:class:`telegram.InlineKeyboardButton`): The button to use in the markup
            **kwargs (:obj:`dict`): Arbitrary keyword arguments.
        """
        return cls([[button]], **kwargs)

    @classmethod
    def from_row(
        cls, button_row: List[InlineKeyboardButton], **kwargs: object
    ) -> 'InlineKeyboardMarkup':
        """Shortcut for::
            InlineKeyboardMarkup([button_row], **kwargs)
        Return an InlineKeyboardMarkup from a single row of InlineKeyboardButtons
        Args:
            button_row (List[:class:`telegram.InlineKeyboardButton`]): The button to use in the
                markup
            **kwargs (:obj:`dict`): Arbitrary keyword arguments.
        """
        return cls([button_row], **kwargs)

    @classmethod
    def from_column(
        cls, button_column: List[InlineKeyboardButton], **kwargs: object
    ) -> 'InlineKeyboardMarkup':
        """Shortcut for::
            InlineKeyboardMarkup([[button] for button in button_column], **kwargs)
        Return an InlineKeyboardMarkup from a single column of InlineKeyboardButtons
        Args:
            button_column (List[:class:`telegram.InlineKeyboardButton`]): The button to use in the
                markup
            **kwargs (:obj:`dict`): Arbitrary keyword arguments.
        """
        button_grid = [[button] for button in button_column]
        return cls(button_grid, **kwargs)

    def __hash__(self) -> int:
        return hash(tuple(tuple(button for button in row) for row in self.inline_keyboard))