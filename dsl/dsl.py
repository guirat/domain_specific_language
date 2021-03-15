import json


class Dsl:
    sql_query = ""
    fields = []

    def __init__(self, model, dsl_query):
        self.model = model
        self.dsl_query = dsl_query
        self.sql_query = ""

    def validate(self):
        pass

    def convert_to_sql_query(self):
        try:
            self.fields = ",".join(json.loads(self.dsl_query)["fields"])
        except TypeError:
            raise ("Unable to serialize the object")

        return f"SELECT {self.fields} FROM {self.model};"
