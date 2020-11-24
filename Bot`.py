import telebot
import main_updater
bot = telebot.TeleBot("711206308:AAFgfif_YviD5mHtpt2b2IRm-XZNsByXe_c")
# def log(message, answer):
#     from datetime import datetime
#     print("\n -------")
#     print("Время отправки сообщения: "+ str(datetime.now()))
#     print("Сообщение от {0} {1}. id = {2}. \nТекст - {3}".format(message.from_user.first_name,
#                                                                   message.from_user.last_name,
#                                                                   str(message.from_user.id), message.text))
#     print("Бот ответил: " + str(answer))
#     with open("Logs", "w") as file:
#         file.write(str(log(message, answer)))
#     file.close()
@bot.message_handler(commands=['programing'])
def programing(message):
    for x in main_updater.get_sites("programing"):
        bot.send_message(message.chat.id, x)
@bot.message_handler(commands=['discovery'])
def discovery(message):
    for x in main_updater.get_sites("discovery"):
        bot.send_message(message.chat.id, x)
@bot.message_handler(commands=['art'])
def art(message):
    for x in main_updater.get_sites("art"):
        bot.send_message(message.chat.id, x)
@bot.message_handler(commands=['music'])
def music(message):
    for x in main_updater.get_sites("music"):
        bot.send_message(message.chat.id, x)
@bot.message_handler(commands=['kyivnews'])
def kyivnews(message):
    for x in main_updater.get_sites("Kyiv news"):
        bot.send_message(message.chat.id, x)
@bot.message_handler(commands=['ai'])
def ai(message):
    for x in main_updater.get_sites("ai"):
        bot.send_message(message.chat.id, x)
@bot.message_handler(commands=['art'])
def art(message):
    for x in main_updater.get_sites("art"):
        bot.send_message(message.chat.id, x)
@bot.message_handler(commands=['f'])
def respects(message):
    bot.send_message(message.chat.id, "Respects have been payed!!!")
    # bot.send_sticker(message.chat.id, "CAADAgADJAQAApzW5wpksJrMUrpH7BYE")
    bot.send_sticker(message.chat.id, "CAADAgADsAADTptkAler0GVnHyzGFgQ")
    # bot.send_sticker(message.chat.id, "CAADBAADfwcAApcfgwF8FKI6AsPPDBYE")
@bot.message_handler(commands=['some_programming_articles'])
def programing(message):
    for x in main_updater.get_sites("some_articles_programming"):
        bot.send_message(message.chat.id, x)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Hello':
        # answer = 'Hello, my user'
        # log(message, answer)
        bot.send_message(message.chat.id, 'Hello, my user')
    elif message.text == 'Bye':
        # answer = 'Bye, user'
        # log(message, answer)
        bot.send_message(message.chat.id, 'Bye, user')
bot.polling()
