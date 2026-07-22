import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ==========================================
# ТОКЕН (из config.py или прямо здесь)
# ==========================================
BOT_TOKEN = "8254882046:AAHw5R5UA2ObBopYg0A3JN3E5KaMbtleZ6Y"  # ВСТАВЬ СВОЙ ТОКЕН

# ==========================================
# КОМАНДА /start
# ==========================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Привет! Я живой!\n\n"
        "Отправь мне любое сообщение, и я отвечу."
    )

# ==========================================
# КОМАНДА /help
# ==========================================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Команды:\n"
        "/start — приветствие\n"
        "/help — помощь\n"
        "/ping — проверка связи"
    )

# ==========================================
# КОМАНДА /ping
# ==========================================
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong!")

# ==========================================
# ОБРАБОТЧИК ТЕКСТА (на любое сообщение)
# ==========================================
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"🔊 Ты сказал: {text}")

# ==========================================
# ЗАПУСК БОТА
# ==========================================
def main():
    print("🚀 Запуск простого бота...")
    
    # Создаём приложение
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("✅ Бот запущен! Напиши /start в Telegram.")
    
    # Запускаем бота
    app.run_polling()

if __name__ == "__main__":
    main()
