from telegram import Update, Bot
from telegram.error import TelegramError
from telegram.ext import CommandHandler, Filters, Updater
from modules.notifier.functions import generate_diff, split_text, get_platform_profile, shorten_string

# Replace TOKEN with your bot token
bot = Bot(token='TOKEN', parse_mode=telegram.ParseMode.MARKDOWN)

def send_notification(data, webhook_url):
    try:
        chat_id = webhook_url.split('/')[-1]
        message = ""

        if data["isRemoved"]:
            message = removed_program_message(data)
        elif data["isNewProgram"]:
            message = new_program_message(data)
        else:
            message = changed_program_message(data)

        if message:
            send_message = bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
            if send_message.status_code != 200:
                print(data["programName"])
                print("Error sending message:", send_message.content)
    except TelegramError as e:
        print(f'Error sending message: {e}')

def send_startup_message(webhook_url):
    try:
        chat_id = webhook_url.split('/')[-1]
        message = f"🎉 Successful Start of Programs Watcher 🎉\n\nHi, welcome to ** Programs Watcher **! 🎉\nThe program has started successfully and is now waiting for a change. 🗼✨\n\n** Github page: ** https://github.com/Alikhalkhali/programs-watcher"

        send_message = bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        if send_message.status_code != 200:
            print("There was an error sending the Discord message")
    except TelegramError as e:
        print(f'Error sending message: {e}')
