token = "448526934:AAGE5d8EzYQru28AiKg8y1FkR8wMkABZT90"
import telebot
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def stat_my_bot(message):
    bot.send_message(message.chat.id, "Привет, красавица? Хочешь увидеть заю?", reply_markup=markup )

@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    keyboard_hider = types.ReplyKeyboardRemove()
    if message.text == "Да":
        bot.send_photo(message.chat.id, photo=open('ann.jpg', 'rb'), caption='Вот она!', reply_markup=keyboard_hider)
    elif (message.text =="Нет"):
       bot.send_message(message.chat.id, 'Как нет? Подумай', reply_markup=markup)
    else:
        text = 'Что значит "'+message.text+'"?! Заю хочешь увидеть?'
        bot.send_message(message.chat.id, text, reply_markup=markup)


def generate_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    list_items = ["Да", "Нет"]
    for item in list_items:
        markup.add(item)
    return markup

if __name__ == '__main__':
    markup = generate_markup()
    bot.polling(none_stop=True)
