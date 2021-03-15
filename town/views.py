from django.db import connection
from dsl.views import dsl_get


def get_towns(dsl_query):
    sql_query = dsl_get("town_town", dsl_query)
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        row = cursor.fetchall()
    return row
