from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random
import os

# Mengambil API Token dari environment variable (GitHub Secrets)
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')  # Mengambil API Token dengan nama TELEGRAM_API_TOKEN

# Daftar pesan unik yang akan dibalas oleh bot
unique_messages = [
    "Keep pushing, you're doing great!",
    "Success is a journey, not a destination.",
    "Believe in yourself and all that you are.",
    "Challenges are what make life interesting.",
    "The harder you work for something, the greater you'll feel when you achieve it."
]

def start(update: Update, context: CallbackContext) -> None:
    """Command /start: Menyapa pengguna ketika bot dijalankan."""
    update.message.reply_text("Hello! I'm your unique bot. Type any message and I'll send something cool back!")

def help(update: Update, context: CallbackContext) -> None:
    """Command /help: Memberikan informasi tentang cara menggunakan bot."""
    update.message.reply_text("Send me any message and I'll reply with a unique quote!")

def echo(update: Update, context: CallbackContext) -> None:
    """Menangani pesan teks dan mengirimkan pesan unik."""
    random_message = random.choice(unique_messages)
    update.message.reply_text(random_message)

def main() -> None:
    """Menjalankan bot Telegram dan menunggu pesan dari pengguna."""
    # Menggunakan API Token dari environment variable
    updater = Updater(API_TOKEN)  # Menggunakan TELEGRAM_API_TOKEN di sini
    dispatcher = updater.dispatcher

    # Menambahkan handler untuk perintah /start, /help, dan pesan lainnya
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Memulai polling dan menunggu pesan
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
