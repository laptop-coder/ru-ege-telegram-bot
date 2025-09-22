import db
from enums import Category
from set_record_used import set_record_used


def get_one_table_info(table_name: Category):
    cursor = db.connection.cursor()
    [info] = cursor.execute(
        f"""SELECT info FROM {table_name.name} WHERE used=0 ORDER BY RANDOM() LIMIT 1;"""
    ).fetchone()

    set_record_used(table_name, info)

    return info
