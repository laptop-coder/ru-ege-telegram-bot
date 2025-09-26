import signal

from telegram import Bot
from telegram.ext import (
    ApplicationBuilder,
)

from handle_signals import receive_signal
import config

bot = Bot(config.BOT_TOKEN)


def main():
    signal.signal(signal.SIGUSR1, receive_signal)
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.run_polling()


if __name__ == "__main__":
    main()
