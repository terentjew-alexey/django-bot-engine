from . import bot
from .models import Account
from .types import Message


@bot.handler
def simple_echo(message: Message, account: Account):
    """
    Simple echo chat bot.
    """
    account.send_message(message)
    # TODO: implement the ability to add buttons to menu buttons


@bot.button_handler
def button_echo(message: Message, account: Account):
    """
    Simple echo on the button.
    """
    account.send_message(message)
