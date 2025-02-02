from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Ваш токен
TOKEN = "7661557303:AAFEIiReDyIw-VtQRT7VxqnhVlBTV1WT55M"

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я твой бот. Как дела?")

# Функция для ответа на текстовые сообщения
def echo(update: Update, context: CallbackContext):
    user_text = update.message.text
    update.message.reply_text(f"Вы сказали: {user_text}")

# Основная функция
def main():
    # Создаем объект Updater и передаем ему токен
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
