import os
import logging


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


BOT_TOKEN = os.getenv("BOT_TOKEN", "")
if BOT_TOKEN == "":
    logger.error("Please specify BOT_TOKEN env variable")
    os._exit(1)

CHANNEL_ID = os.getenv("CHANNEL_ID", "")
if CHANNEL_ID == "":
    logger.error("Please specify CHANNEL_ID env variable")
    os._exit(1)

PATH_TO_DB = os.getenv("PATH_TO_DB", "")
if PATH_TO_DB == "":
    logger.error("Please specify PATH_TO_DB env variable")
    os._exit(1)

PATH_TO_INITIAL_SQL_QUERIES = os.getenv("PATH_TO_INITIAL_SQL_QUERIES", "")
if PATH_TO_INITIAL_SQL_QUERIES == "":
    logger.error("Please specify PATH_TO_INITIAL_SQL_QUERIES env variable")
    os._exit(1)

PATH_TO_GET_INFO_SQL_QUERIES = os.getenv("PATH_TO_GET_INFO_SQL_QUERIES", "")
if PATH_TO_GET_INFO_SQL_QUERIES == "":
    logger.error("Please specify PATH_TO_GET_INFO_SQL_QUERIES env variable")
    os._exit(1)
