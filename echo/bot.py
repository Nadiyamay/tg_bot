import json
from telegram import Update
from telegram.ext import Updater, CallbackContext, TypeHandler

import os
from dotenv import load_dotenv

load_dotenv()

def echo(update: Update, context: CallbackContext) -> None:
    text = "Your text: "+update.message.text
    try:
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    except: 
        print("Something went wrong!")


def main() -> None:
    updater = Updater(os.getenv('TOKEN'))

    updater.dispatcher.add_handler(TypeHandler(Update, echo))

    updater.start_polling()

    print('Started')

    updater.idle()


if __name__ == "__main__":
    main()