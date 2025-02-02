from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime
import random

TOKEN = "7661557303:AAFEIiReDyIw-VtQRT7VxqnhVlBTV1WT55M"

# Список шуток
JOKES = [
    "Почему программисты предпочитают темную тему? Потому что свет притягивает баги!",
    "Что сказал нуль восьмерке? 'Норм пояса!'",
    "Почему Python не может завести друзей? Потому что он всегда теряет self!",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я твой бот. Используй /help для списка команд.")

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

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = """
    🤖 Мой функционал:
    - Отвечать на сообщения
    - Показывать время
    - Рассказывать шутки
    - И многое другое!
    """
    await update.message.reply_text(info_text)

async def show_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_time = datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"⏰ Текущее время: {current_time}")

async def tell_joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = random.choice(JOKES)
    await update.message.reply_text(f"🎭 {joke}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"Вы сказали: {user_text}")

def main():
    application = Application.builder().token(TOKEN).build()
    
    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("time", show_time))
    application.add_handler(CommandHandler("joke", tell_joke))
    
    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    application.run_polling()

if __name__ == "__main__":
    main()