import datetime
import json
import pytz
import traceback
import telebot
import bunker
import settings


P_TIMEZONE = pytz.timezone(settings.TIMEZONE)
TIMEZONE_COMMON_NAME = settings.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(settings.TOKEN)
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Hello and welcome to the bunker.\nTo start new game press /newgame.\n \
        To get help press /help.'
        )
    
@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/jamalgaigaridze'
        )
    )
    bot.send_message(
        message.chat.id,
        "1) To start new game press /newgame.\n \
         2) To see the game's rules press /rules",
        reply_markup=keyboard
        )
    
@bot.message_handler(commands=['rules'])
def rules_command(message):
    with open('rules.txt', 'r', encoding = "utf-8") as file:
        text = file.read()
        bot.send_message(
            message.chat.id, file
            )
        
@bot.message_handler(commands=['newgame'])
def newgame_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('5', callback_data='5'),  
        telebot.types.InlineKeyboardButton('6', callback_data='6')  
    )  
    keyboard.row(  
        telebot.types.InlineKeyboardButton('7', callback_data='7'),  
        telebot.types.InlineKeyboardButton('8', callback_data='8')  
    )
    keyboard.row(  
        telebot.types.InlineKeyboardButton('9', callback_data='9'),  
        telebot.types.InlineKeyboardButton('10', callback_data='10')  
    )
    bot.send_message(  
        message.chat.id,   
        'How many players will participate:',  
        reply_markup=keyboard
        )
    @bot.callback_query_handler(func=lambda call: True)  
    def iq_callback(query):  
        data = query.data   
        get_callback(query)
    
    def get_callback(query):  
        bot.answer_callback_query(query.id)  
        send_result(query.message, query.data)
    
    def send_result(message, players):
        players = int(players)
        bunker.filler(players)
        bunker.writer(players)
        for i in range(1, players+1):
            with open(f'player_{i}.txt', 'rb') as doc:
                bot.send_document(chat_id, doc)
bot.polling(none_stop=True)