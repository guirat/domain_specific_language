from dsl.dsl import Dsl


def dsl_get(model, dsl_query):
    dsl = Dsl(model, dsl_query)
    return dsl.convert_to_sql_query()
