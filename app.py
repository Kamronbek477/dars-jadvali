from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,Dispatcher
from telegram import Update,Bot
from handler import (start,
                     menu
                     )
from flask import Flask, request
import os

# get token from environment variable
TOKEN = '6198972222:AAFMAYd6f3bJFSh-1FA6ZnqdZTtAIRhbjyE'

bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return 'OK'

@app.route('/webhook', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        return 'hi from Python2022I'
    elif request.method == "POST":
        data = request.get_json(force = True)
        
        dp: Dispatcher = Dispatcher(bot, update_queue=None, workers=0)
        update:Update = Update.de_json(data, bot)
    
        #update 
                
        dp.add_handler(CommandHandler("start",start))
        dp.add_handler(CallbackQueryHandler(menu))


        
        dp.process_update(update)
        return 'ok'