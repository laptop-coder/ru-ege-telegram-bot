from datetime import date

from consts import days_of_week
from enums import Category
from get_info import get_info
from get_one_table_info import get_one_table_info
from set_all_records_in_table_unused import set_all_records_in_table_unused
from telegram import Bot
from templates import ru_ege_info_message_template
import config


bot = Bot(config.BOT_TOKEN)


async def send_ru_ege_info_message() -> None:
    current_date = date.today()
    formatted_date = (
        current_date.strftime("%d.%m.%Y")
        + ", "
        + days_of_week[current_date.isoweekday()]
    )

    info = get_info()

    for item in Category:
        if info[item.name] is None:
            set_all_records_in_table_unused(item)
            info[item.name] = get_one_table_info(item)

    ru_ege_info_message = ru_ege_info_message_template.render(
        date=formatted_date,
        orthoepy=info[Category.orthoepy.name],
        paronyms=info[Category.paronyms.name],
        phraseological_unit=info[Category.phraseological_unit.name],
        unstressed_at_root=info[Category.unstressed_at_root.name],
    )

    await bot.send_message(config.CHANNEL_ID, ru_ege_info_message, parse_mode="HTML")
