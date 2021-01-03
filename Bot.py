import telegram
import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1462708728:AAE7gqxjqBI1qKP3XVA3b_gHUW2xuSJOt5s"


def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200):
        data = response.json()
        print(data['Global'])
        context.bot.send_message(chat_id = update.effective_chat_id, text = data['Global'])
    else:
        context.bot.send_message(chat_id = update.effective_chat_id, text = "Error, Something went wrong.")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('summary', summary))

    updater.start_polling()

if __name__ == "__main__":
    main()