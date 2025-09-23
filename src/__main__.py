from telegram import Bot
from telegram.ext import (
    ApplicationBuilder,
)

import config

bot = Bot(config.BOT_TOKEN)


def main():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.run_polling()


if __name__ == "__main__":
    main()
