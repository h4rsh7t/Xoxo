import os
import asyncio
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
    # Yahan MoneyPrinter ka code ayega

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, make_video))
    loop.run_until_complete(app.run_polling())

web = Flask(__name__)
@web.route('/')
def home(): return "Bot Running"

if __name__ == "__main__":
    Thread(target=run_bot).start()
    web.run(host="0.0.0.0", port=10000)
