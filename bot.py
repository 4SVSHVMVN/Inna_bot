#!/usr/bin/env python
# -*- coding: utf-8
import telebot
import config
import inn
bot = telebot.TeleBot(config.token)

#2396808748


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, друг, меня зовут Инна.')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Позволь я тебе помогу:')
    bot.send_message(message.chat.id, 'Для того чтобы расшифровать ИНН код введи - "/INN код"')



@bot.message_handler(commands=['inn', 'INN'], content_types=['text'])
def inn_reader(message):
    try:
        inna = "".join([message.text][0].split(' ')[1])
    except Exception as e:
        bot.send_message(message.chat.id, "Упс, что-то пошло не так. Попробуйте еще раз")
        return False
    msg = ""
    flag_valid = inn.check(inna)
    if flag_valid:
        msg += "ИНН " + inna + " введен правильно"
    else:
        msg += "ИНН " + inna + " введен неправильно, попробоуй еще раз"
    bot.send_message(message.chat.id, msg)
    if flag_valid:
        bot.send_message(message.chat.id, inn.info(inna))


@bot.message_handler(content_types=["text"])
def wtf(message):
    bot.send_message(message.chat.id, "Прости, я не понимаю о чем ты\nПопробуй ввести /help")


if __name__ == '__main__':
    bot.polling(none_stop=True)
