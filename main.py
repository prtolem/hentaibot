import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=["start", "info"])
def command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    box_hentai = types.KeyboardButton("Hentai")
    markup.add(box_hentai)

    bot.send_message(message.chat.id, "Select an action:", reply_markup=markup)


@bot.message_handler(content_types=["text"], func=lambda m: True)
def function(message):
    if message.text == "Hentai":
        response = requests.get("https://nekos.life/api/v2/img/lewdk")
        json_data = json.loads(response.text)
        bot.send_photo(message.chat.id, json_data["url"])
    else:
        print('there`s no such thing')


bot.polling(none_stop=True)
