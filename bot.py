import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("MoneyPrinterTurbo ON hai ✅\nTopic bhejo jaise: 'AI Motivation'")

async def make_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    topic = update.message.text
    await update.message.reply_text(f"🎬 '{topic}' pe video bana raha hu...")

web = Flask(__name__)
@web.route('/')
def home(): return "Bot Running"

def run_flask():
    web.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    # Flask ko side wale thread me bhejo
    Thread(target=run_flask).start()
    
    # Bot ko main thread me chalao
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, make_video))
    app.run_polling()
