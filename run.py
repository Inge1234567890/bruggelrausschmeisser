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
#import asyncio
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
from telegram import *
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
#logger.error("test error")

#with open(f"{getcwd()}/data/federation.json", "r") as f:
#    MODLIST = json.loads(f.read())
MODLIST = [1053817374, 124894107, 795197076]

#function to check if userID 
def is_mod(userID):
    #check if userID in MODLIST
    if userID in MODLIST:
        return True
    else:
        return False

""" def moderation """

from telegram import Update, ChatPermissions
from telegram.ext import CallbackContext
from typing import Optional, Union
from datetime import datetime


class Moderation(Chat):
    """Class with methods useful for moderating.

    Usage
    -----
        mod = Moderation(update, context)

        # Simple way to get user ID from message you replied with command.
        user_id = update.message["reply_to_message"].from_user.id
        ...
    """

    def __init__(self, update: Update, context: CallbackContext) -> None:
        self.update = update
        self.context = context
        super().__init__(update, context)

    def change_permissions(
        self,
        user_id: int,
        until_date: Union[int, datetime] = None,
        permissions: ChatPermissions = None,
    ) -> None:
        """Change any permission to user in chat."""

        if not self.is_user_admin(user_id):
            self.context.bot.restrict_chat_member(
                self.chat_id, user_id, permissions=permissions, until_date=until_date,
            )
        else:
            raise PermissionError("Cannot change chat admin permissions")

    def mute(self, user_id: int, until_date: Union[int, datetime] = None) -> None:
        """Mute user in chat."""

        perms = ChatPermissions(can_send_messages=False)
        self.change_permissions(user_id, until_date, perms)

    def unmute(self, user_id: int) -> None:
        """Restore permissions to restricted (or muted) user."""

        perms = ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
        )
        self.change_permissions(user_id, permissions=perms)

    def ban(
        self,
        user_id: int,
        until_date: Union[int, datetime] = None,
        revoke_messages: bool = False,
    ) -> None:
        """Ban user in chat."""

        if not self.is_user_admin(user_id):
            self.context.bot.ban_chat_member(
                self.chat_id,
                user_id,
                until_date=until_date,
                revoke_messages=revoke_messages,
            )
        else:
            raise PermissionError("Cannot ban chat admin")

    def unban(self, user_id: int) -> None:
        """Unban banned user in chat."""

        if not self.is_user_admin(user_id):
            self.context.bot.unban_chat_member(self.chat_id, user_id)
        else:
            raise PermissionError("Cannot unban chat admin")



"""" define custom commands """        

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="meddl!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def del_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /del is issued."""
    user = update.message.from_user
    print("user:")
    print(user)
    chat_id = update.message.chat_id
    print("chat_id:")
    print(chat_id)
    print("update.message:")
    print(update.message)
    reply_to_message = update.message.reply_to_message
    if reply_to_message is None:
        logger.error('reply_to_message is None. But it shouldn\'t.')
        update.message.reply_text('There is no message attached. Try again.')
        return
    # ... business logic
    cmd_msg_id = update.message._id_attrs[0]
    print("reply_to_message.id:")
    print(reply_to_message.id)
    print("cmd_msg_id:")
    print(cmd_msg_id)
    feedback1 = await context.bot.delete_message(chat_id, reply_to_message._id_attrs[0])
    print("feedback1:")
    print(feedback1)
    feedback = await context.bot.delete_message(chat_id, cmd_msg_id)
    print("feedback:")
    print(feedback)
    #await update.message.reply_text("del_command")

async def mute_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    #mod = Moderation(update, context)
    #mod = mod.mute
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
    #print(telegram.User.id)
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