from db import connection
from enums import Category


def set_all_records_in_table_unused(table_name: Category):
    with connection:
        cursor = connection.cursor()
        cursor.execute(f"""UPDATE {table_name.name} SET used=0;""")
