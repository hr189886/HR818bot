from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config.settings import BOT_TOKEN, ADMIN_USER_ID
from utils.file_writer import write_to_queue

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_USER_ID:
        await update.message.reply_text("🤖 Bot is ready for your commands!")
    else:
        await update.message.reply_text("🚫 Unauthorized user.")

async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_USER_ID:
        return await update.message.reply_text("🚫 Unauthorized")

    content = " ".join(context.args)
    write_to_queue(content)
    await update.message.reply_text("📬 Code sent to queue!")

def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send", send))
    app.run_polling()
