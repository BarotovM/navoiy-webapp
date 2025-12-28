from telebot import TeleBot, types

bot = TeleBot("8274009318:AAHY4nNLqC7Ue2y_a2KplZSsOposc6-5a-Y")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(
            text="🛍 Magazin",
            web_app=types.WebAppInfo(
                url="https://github.com/BarotovM/navoiy-webapp/"
            )
        )
    )
    bot.send_message(
        message.chat.id,
        "Xush kelibsiz Navoiy Deals!",
        reply_markup=markup
    )

@bot.message_handler(content_types=['web_app_data'])
def web_app_data(message):
    bot.send_message(
        message.chat.id,
        f"Ma'lumot qabul qilindi:\n{message.web_app_data.data}"
    )

bot.polling()
