"""
http://t.me/IGC_inspection_bot
"""

import telebot
import arshin_request
from config import bottoken
from telebot import types


bot = telebot.TeleBot(bottoken)


@bot.message_handler(commands=['start'])
def start(message: str):
    """Команда start. Приветствие"""
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text=f'Рад тебя видеть, {message.from_user.first_name}!\n'
                                           f'Выбери команду из меню', reply_markup=markup)


@bot.message_handler(commands=['arshin'])
def arshin_step1(message: str):
    """Получение номера свидетельства о поверке. Очистка кнопок"""
    markup = types.ReplyKeyboardRemove(selective=False)
    message = bot.send_message(message.chat.id, text=f'{message.from_user.first_name}, введи последние '
                                                     f'9 цифр свидетельства о поверке', reply_markup=markup)
    bot.register_next_step_handler(message, arshin_step2)


def arshin_step2(message: str):
    """Выдача страницы в Аршин. Очистка кнопок"""
    arshin_page = arshin_request.get_mt_page(str(message.text))
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, text=f'Ссылка на страницу прибора в Аршин\n '
                                           f'{arshin_page}', reply_markup=markup)

bot.polling(none_stop=True)