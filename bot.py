from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from datetime import datetime
import random
import logging

# Настройка логирования
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "7661557303:AAFEIiReDyIw-VtQRT7VxqnhVlBTV1WT55M"

# Список шуток
JOKES = [
    "Почему программисты предпочитают темную тему? Потому что свет притягивает баги!",
    "Что сказал нуль восьмерке? 'Норм пояса!'",
    "Почему Python не может завести друзей? Потому что он всегда теряет self!",
]

# Команда /start с кнопками
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🕒 Время", callback_data="time")],
        [InlineKeyboardButton("🎭 Шутка", callback_data="joke")],
        [InlineKeyboardButton("ℹ️ Информация", callback_data="info")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)

# Обработка нажатий на кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        await query.edit_message_text(f"⏰ Текущее время: {current_time}")
    elif query.data == "joke":
        joke = random.choice(JOKES)
        await query.edit_message_text(f"🎭 {joke}")
    elif query.data == "info":
        info_text = """
        🤖 Мой функционал:
        - Отвечать на сообщения
        - Показывать время
        - Рассказывать шутки
        - И многое другое!
        """
        await query.edit_message_text(info_text)

# Команда /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
    Доступные команды:
    /start - Начать диалог
    /help - Помощь и список команд
    /info - Информация о боте
    /time - Текущее время
    /joke - Случайная шутка
    """
    await update.message.reply_text(help_text)

# Обработка текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"Вы сказали: {user_text}")

# Обработка ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}")
    await update.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте позже.")

def main():
    application = Application.builder().token(TOKEN).build()
    
    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    
    # Обработчик нажатий на кнопки
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Обработчик ошибок
    application.add_error_handler(error_handler)
    
    application.run_polling()

if __name__ == "__main__":
    main()