import signal
import asyncio

from config import logger

from send_ru_ege_info_message import send_ru_ege_info_message


def receive_signal(signal_number, frame):
    match signal_number:
        case signal.SIGUSR1:
            logger.info("Received signal SIGUSR1")
            asyncio.create_task(send_ru_ege_info_message())
