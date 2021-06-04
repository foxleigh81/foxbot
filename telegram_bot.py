import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import todoist_handler

load_dotenv()

# function to handle the /start command
def show_items(update, context):
    items = todoist_handler.list_items()
    print(items)
    for item in items:
        update.message.reply_text(item)

# function to handle the /help command
def help(update, context):
    update.message.reply_text('Add items to the list by sending one item per line')

# function to handle errors occured in the dispatcher 
def error(update, context):
    update.message.reply_text('an error occured')

def pretty_print_items(items):
    list_length = len(items)
    string = 'Added'
    if (list_length > 1):
        for index, item in enumerate(items):
            if (index == list_length - 1):
                string += ' and'
            string += ' ' + item
            
    else:
        string += ' ' + items[0]
    return string + ' to the list'

# function to handle normal text 
def add_items(update, context):
    text_received = update.message.text
    dirty_items = text_received.split('\n')
    items = []
    for item in dirty_items:
        items.append(item.strip())

    try:
        # Update todoist
        todoist_handler.add_items(items)
        update.message.reply_text(pretty_print_items(items))
    except:
        error()

def main():
    TOKEN = os.getenv('telegram_bot_token')

    # create the updater, that will automatically create also a dispatcher and a queue to 
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("list", show_items))
    dispatcher.add_handler(CommandHandler("help", help))

    # add an handler for adding items
    dispatcher.add_handler(MessageHandler(Filters.text, add_items))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()