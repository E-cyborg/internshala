import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import httpx

BOT_TOKEN = '8112394410:AAFJnqM9cuL48z-VYwGveIreafHnVDjiUi0'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if user.username:
        name_to_show = f"@{user.username}"
        name_to_send = user.username
    else:
        full_name = user.first_name or ""
        if user.last_name:
            full_name += " " + user.last_name
        name_to_show = full_name.strip() or "there"
        name_to_send = name_to_show

    await update.message.reply_text(f"Hello {name_to_show}, welcome!")

    url = 'http://127.0.0.1:8000/api/tel'
    data = {'name': name_to_send}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, data=data)
            response.raise_for_status()
        except httpx.HTTPError as e:
            print(f"HTTP error occurred: {e}")

def run_bot():
    # Create and set a new event loop for this thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("🚀 Telegram Bot is polling...")
    app.run_polling()
