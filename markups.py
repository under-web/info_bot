import telebot

# --- Main menu ---
main_menu = telebot.types.ReplyKeyboardMarkup(True)
main_menu.row('Нужен Гугл Парсер (GoogleParser)', 'Мне нужна рассылка Whatsapp')

# ---back menu ---
back_menu = telebot.types.ReplyKeyboardMarkup(True)
back_menu.row('Назад')

# --- Delete markup ---
del_markup = telebot.types.ReplyKeyboardRemove()