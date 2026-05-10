from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from app.utils.config import settings
from app.bot.handlers import start, button_handler

def run_bot():
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    run_bot()
