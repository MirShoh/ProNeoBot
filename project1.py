from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

def start(update, context):
    first_name = update.message.from_user.first_name
    update.message.reply_text(
        text=f"Salom, {first_name}! Botimizga xush kelibsiz!")
    buttons = [
        [KeyboardButton(text="🇺🇿 O'zbek tili"), KeyboardButton(text="🇷🇸 Русский язык")]
    ]
    update.message.reply_text(
        text="Marhamat tilni tanlang:\n\nПожалуйста, выберите язык:",
        reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )
def back(update, context):
    buttons = [
        [KeyboardButton(text="🇺🇿 O'zbek tili"), KeyboardButton(text="🇷🇸 Русский язык")]
    ]
    update.message.reply_text(
        text="Marhamat tilni tanlang:\n\nПожалуйста, выберите язык:",
        reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    )

def first_name(update, context):
    global first_name
    first_name = update.message.text
    update.message.reply_text(text="Ism-familiyangizni kiriting:")

def age(update, context):
    global age
    age = update.message.text
    update.message.reply_text(text="Yoshingizni kiriting:")

def message_handler(update, context):
    message = update.message.text
    if message == "🇺🇿 O'zbek tili":
        buttons = [
            [KeyboardButton(text="👤 Registratsiya"), KeyboardButton(text="ℹ️ Bot haqida"), KeyboardButton(text="⬅️ Ortga")]
        ]
        update.message.reply_text(
            text="Kerakli bo'limni tanlang:",
            reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
        )

    elif message == "ℹ️ Bot haqida":
        update.message.reply_text(text = "Bu bot orqali siz ro'yxatdan o'tishingiz mumkin!")

    elif message == "⬅️ Ortga":
        back(update, context)

    elif message == "👤 Registratsiya":
        first_name(update, context)

    elif message == "🇷🇸 Русский язык":
        buttons = [
            [KeyboardButton(text="👤 Регистрация"), KeyboardButton(text="ℹ️ О боте"), KeyboardButton(text="⬅️ Назад")]
        ]
        update.message.reply_text(
            text="Выберите нужный раздел:",
            reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
        )
    
    elif message == "👤 Регистрация":
        update.message.reply_text(text="Введите свое имя и фамилию: ")

    elif message == "ℹ️ О боте":
        update.message.reply_text(text = "Вы можете зарегистрироваться через этого бота!")
    
    elif message == "⬅️ Назад":
        back(update, context)

def main():
    updater = Updater("1776334506:AAEg2YEfu28F4dWJ2WF9sNyXNBGe7tgi3Ps")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
