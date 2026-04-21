from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8680599854:AAEDOlVvxVcV5253JwtxZQ875u1bXerCpk0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📊 فتح التطبيق",
                web_app=WebAppInfo(url="http://127.0.0.1:5000")
            )
        ]
    ]

    await update.message.reply_text(
        "👨‍⚕️ مرحبًا",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.effective_message.web_app_data.data
    await update.message.reply_text(f"📥 تم الاستلام: {data}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, webapp_data))

print("Bot running...")
app.run_polling()