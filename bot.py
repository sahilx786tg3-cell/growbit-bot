import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "APNA_NAYA_TOKEN"
ADMIN_ID = 6520878121
APP_URL = "https://legendary-starburst-b72020.netlify.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    ref_id = None
    if context.args:
        try:
            ref_id = int(context.args[0])
        except:
            pass
    url = f"{APP_URL}?ref={ref_id}" if ref_id else APP_URL
    welcome_text = (
        "🎯 *Welcome to GrowBit!*\n\n"
        "💎 Earn rewards, complete tasks,\n"
        "📈 invest coins & withdraw easily!\n\n"
        "⚡️ Invest coins & earn daily profits\n"
        "🎁 Claim daily rewards\n"
        "👥 Refer friends & earn bonus\n"
        "🏆 Compete on leaderboard\n\n"
        "👇 *Tap below to start!*"
    )
    keyboard = [
        [InlineKeyboardButton("🎮 Enter GrowBit", web_app=WebAppInfo(url=url))],
        [InlineKeyboardButton("📢 GrowBit Updates", url="https://t.me/LiteDropX")]
    ]
    if user.id == ADMIN_ID:
        keyboard.append([InlineKeyboardButton("👑 Admin Panel", url=f"{APP_URL}/admin.html")])
    await update.message.reply_text(
        welcome_text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("GrowBit Bot running...")
    app.run_polling(drop_pending_updates=True)
