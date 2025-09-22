from db import connection
from enums import Category


def set_record_used(table_name: Category, info: str):
    with connection:
        cursor = connection.cursor()
        cursor.execute(f"""UPDATE {table_name.name} SET used=1 WHERE info='{info}';""")
