import db
import config
from enums import Category
from set_record_used import set_record_used


def get_info():
    cursor = db.connection.cursor()
    with open(config.PATH_TO_GET_INFO_SQL_QUERIES, "r") as file:
        sql_queries = file.read()
        data = cursor.execute(sql_queries).fetchone()
        info: dict[str, str] = {
            Category.orthoepy.name: data[0],
            Category.paronyms.name: data[1],
            Category.phraseological_unit.name: data[2],
            Category.unstressed_at_root.name: data[3],
        }

        for item in Category:
            set_record_used(item, info[item.name])

        return info
