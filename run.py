#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Don't forget to enable inline mode with @BotFather

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from html import escape
from uuid import uuid4
from os import getenv, getcwd


from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.error("test error")
#import admins-id from fedederation.json file
import json

#with open(f"{getcwd()}/data/federation.json", "r") as f:
#    MODLIST = json.loads(f.read())
MODLIST = ["1053817374", "124894107", "795197076"]

def is_mod(userID):
    #check if userID in MODLIST
    if userID in MODLIST:
        return True
    else:
        return False

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hi!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def del_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /del is issued."""
    await update.message.reply_text("del_command")

async def mute_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("mute_command")

async def unmute_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("unmute_command")

async def ban_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("ban_command")

async def unban_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("unban_command")

from telegram import User


class UserURL:
    """Simle class to generate URL to user which can be sent in message.

    Usage
    -----
        ...
        # example
        user = update.message["reply_to_message"].from_user
        update.message.reply_text(
            f'User {UserURL(user)} has been muted.', 
            parse_mode="markdown"
        )
        ...
    """

    def __init__(self, user: User) -> None:
        self.user = user

    def __repr__(self) -> str:
        return f"[{self.user.first_name}](tg://user?id={self.user.id})"

async def debug_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /debug is issued."""
    # in_federation=mod.chat_id in FEDERATION
    #user_id = User.send_message("text")
    #user_url = UserURL(user)
    print(update)
    print("\n")
    print(context)
    print("\n")
    print(update.message.from_user.id)
    print("\n")
    print(MODLIST)
    print("\n")
    print(is_mod(update.message.from_user.id))
    await update.message.reply_text("see console\n")
    #await update.message.reply_text("debug_command - info:\n"+ update.inline_query.query)

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query

    if query == "":
        return

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bold",
            input_message_content=InputTextMessageContent(
                f"<b>{escape(query)}</b>", parse_mode=ParseMode.HTML
            ),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italic",
            input_message_content=InputTextMessageContent(
                f"<i>{escape(query)}</i>", parse_mode=ParseMode.HTML
            ),
        ),
    ]

    await update.inline_query.answer(results)


def main() -> None:

    TOKEN = getenv("TOKEN")

    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    #self-created
    application.add_handler(CommandHandler("del", del_command))
    application.add_handler(CommandHandler("mute", mute_command))
    application.add_handler(CommandHandler("unmute", unmute_command))
    application.add_handler(CommandHandler("ban", ban_command))
    application.add_handler(CommandHandler("unban", unban_command))
    #debug command for output
    application.add_handler(CommandHandler("debug", debug_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(InlineQueryHandler(inline_query))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()