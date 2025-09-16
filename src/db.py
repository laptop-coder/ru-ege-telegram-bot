import os
import sqlite3

import config
from config import logger


init_is_needed = False

if not os.path.exists(config.PATH_TO_DB):
    logger.info("Database file not found, initial SQL queries will be executed...")
    init_is_needed = True
else:
    logger.info("Found database file")

connection = sqlite3.connect(config.PATH_TO_DB)

if init_is_needed:
    with connection:
        cursor = connection.cursor()
        with open(config.PATH_TO_INITIAL_SQL_QUERIES, "r") as file:
            sql_queries = file.read()
            cursor.executescript(sql_queries)
