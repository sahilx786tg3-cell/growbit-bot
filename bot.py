import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8415519466:AAFWdJueDAgECb_Ssq0tIlCWsiQr2-ERhh0"
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

    keyboard = [
        [InlineKeyboardButton("🚀 Open GrowBit", web_app=WebAppInfo(url=f"{APP_URL}{'?ref=' + str(ref_id) if ref_id else ''}"))],
        [InlineKeyboardButton("📢 Join Channel", url="https://t.me/LiteDropX")]
    ]
    if user.id == ADMIN_ID:
        keyboard.append([InlineKeyboardButton("👑 Admin Panel", url=f"{APP_URL}/admin.html")])

    await update.message.reply_text(
        f"👋 Welcome {user.first_name}!\n\n"
        "🪙 *GrowBit* — Invest & Earn Game\n\n"
        "✅ Invest virtual coins\n"
        "✅ Earn daily rewards\n"
        "✅ Refer friends for bonus\n\n"
        "👇 Tap to start!",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
