
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(level=logging.INFO)

TOKEN = (
    os.getenv("BOT_TOKEN")
    or os.getenv("TELEGRAM_BOT_TOKEN")
    or os.getenv("TOKEN")
)

if not TOKEN:
    raise RuntimeError(
        "Не найден токен. Добавьте переменную BOT_TOKEN в BotHost."
    )


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "Привет! Бот работает. Скоро подключим поиск "
        "новых объявлений Brawl Stars."
    )


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        "Я буду искать подходящие аккаунты Brawl Stars "
        "и присылать новые объявления."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Telegram-бот запущен и ожидает сообщений.")
    app.run_polling()


if __name__ == "__main__":
    main()

