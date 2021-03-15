import os
# Need to run this before calling models from application!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import django

# Import settings
django.setup()

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import environ
from town.models import Town
from faker import Faker


fake = Faker()

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


configuration = {
    "user": env("USER_DB"),
    "password": env("PASSWORD"),
    "host": env("HOST"),
    "port": env("PORT"),
}


def create_database():
    connexion = psycopg2.connect(**configuration)
    connexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connexion.cursor()
    sql_create_database = f"CREATE DATABASE {env('DB_NAME')}  WITH OWNER = postgres;"
    cursor.execute(sql_create_database)


def populate_db():
    for i in range(10):
        Town.objects.create(
            code=fake.random_int(),
            name=fake.address().city(),
            population=fake.random_int(),
            average_age=fake.pyfloat(),
            district_code=fake.address().city(),
            department_code=fake.random_int(),
            region_code=fake.random_int(),
            region_name=fake.address().street_name(),
        )


if __name__ == "__main__":
    create_database()
    populate_db()
