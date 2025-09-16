from telegram import Update
from telegram import Bot
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    filters,
)

import config


bot = Bot(config.BOT_TOKEN)


async def send_ru_ege_info_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    ru_ege_info_message = """Hello!"""
    await bot.send_message(config.CHANNEL_ID, ru_ege_info_message)


def main():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ChatType.PRIVATE, send_ru_ege_info_message))
    app.run_polling()


if __name__ == "__main__":
    main()
