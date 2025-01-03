from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

API_TOKEN = '8011173029:AAETtYiqyLMKgTSyNYvKsxJpMbPQC0kcl0E'

unique_messages = [
    "Keep pushing, you're doing great!",
    "Success is a journey, not a destination.",
    "Believe in yourself and all that you are.",
    "Challenges are what make life interesting.",
    "The harder you work for something, the greater you'll feel when you achieve it."
]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your unique bot. Type any message and I'll send something cool back!")

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me any message and I'll reply with a unique quote!")

def echo(update: Update, context: CallbackContext) -> None:
    random_message = random.choice(unique_messages)
    update.message.reply_text(random_message)

def main() -> None:
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
