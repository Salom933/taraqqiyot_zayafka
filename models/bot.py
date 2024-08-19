from telebot import TeleBot
import environ
env = environ.Env()
environ.Env.read_env()


bot = TeleBot(token=env("TOKEN"))



ids = 6427338423
def get_post(data):
    bot.send_message(chat_id=ids, text=f"Sizga yangi murojaat mavjud !\n\n\n"
                                          f"Ism: {data['name']}\n"
                                          f"Telefon Raqam: {data['phonenumber']}")