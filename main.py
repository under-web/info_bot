import time
import telebot
from config import bot_token
from text import intro_text, google_text
import markups as mark

bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    intro_photo = open('secretary.jpg', 'rb')
    bot.send_photo(message.chat.id, intro_photo)
    bot.send_message(message.chat.id, intro_text, reply_markup=mark.main_menu)


@bot.message_handler(content_types=['text'])
def send_client_message(message):
    if message.text == 'Нужен Гугл Парсер (GoogleParser)':
        bot.send_message(message.chat.id, google_text)
        bot.send_video(message.chat.id,
                       "BAACAgIAAxkBAAEOKSlhh_6rVA3B033NN7NCqzrwDYuXUgAC3hUAAsDPQEiE_oVdkmB7iCIE",
                       reply_markup=mark.back_menu)
    elif message.text == 'Мне нужна рассылка Whatsapp':
        bot.send_video(message.chat.id,
                       "BAACAgIAAxkBAAEOKT1hiAWajyTX-R-LucGTFgABTTBlfskAAi0WAALAz0BI7WrMk95PQOgiBA",
                       reply_markup=mark.back_menu)
    elif message.text == 'Назад':
        send_welcome(message)

while True:  # функция для пулинга
    print('=^.^=')

    try:
        bot.polling(none_stop=True, interval=3, timeout=20)
        print('Этого не должно быть')
    except telebot.apihelper.ApiException:
        print('Проверьте связь и API')
        time.sleep(10)
    except Exception as e:
        print(e)
        time.sleep(60)
