from django.db import connection


def db_table_exists(table):
    try:
        cursor = connection.cursor()

        if not cursor:
            raise Exception

        table_names = connection.introspection.get_table_list(cursor)
    except:
        raise Exception("unable to determine if the table '%s' exists" % table)
    else:
        return table in table_names