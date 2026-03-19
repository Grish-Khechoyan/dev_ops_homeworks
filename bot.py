from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import httpx
from db import init_db, save_new_jobs, read_jobs_from_db
from config import API_URL

TOKEN = "8525535399:AAF2MDYHiZ92KiwqkhlwuIO6-0Q52odkw3E"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello! Use /jobs to see the latest DevOps jobs."
    )

async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Fetching the DevOps jobs...")

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            res = await client.get(API_URL)
            res.raise_for_status()
            data = res.json()

        jobs_list = data.get("jobs", [])
        if not jobs_list:
            await update.message.reply_text("❌ No jobs found.")
            return

        new_jobs_count = save_new_jobs(jobs_list)

        if new_jobs_count == 0:
            await update.message.reply_text("✅ No new jobs found. Showing latest saved jobs.")
        else:
            await update.message.reply_text(f"✅ {new_jobs_count} new job(s) added!")

        saved_jobs = read_jobs_from_db()
        message = "🔥 Latest DevOps jobs:\n\n"
        for job in saved_jobs:
            message += f"💼 {job[0]}\n"
            message += f"🏢 {job[1]}\n"
            message += f"🌍 {job[2]}\n"
            message += f"🔗 {job[3]}\n\n"

        await update.message.reply_text(message)

    except httpx.RequestError as e:
        await update.message.reply_text(f"⚠️ API request error: {e}")
    except httpx.HTTPStatusError as e:
        await update.message.reply_text(f"⚠️ API returned an error code: {e.response.status_code}")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Unexpected error: {e}")

def main():
    init_db()  # Initialize the database
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jobs", jobs))

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()