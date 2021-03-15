import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import environ
from faker import Faker
import os

# Need to run this before calling models from application!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "domspeclang.settings")
import django

# Import settings
django.setup()

fake = Faker()

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()


configuration = {
    "user": env("USER_DB"),
    "password": env("PASSWORD"),
    "host": env("HOST"),
    "port": env("PORT"),
}


def drop_database():
    connexion = psycopg2.connect(**configuration)
    connexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with connexion.cursor() as cursor:
        sql_create_database = f"DROP DATABASE {env('DB_NAME')};"
        cursor.execute(sql_create_database)
        cursor.close()


def create_database():
    connexion = psycopg2.connect(**configuration)
    connexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connexion.cursor()
    sql_create_database = f"CREATE DATABASE {env('DB_NAME')}  WITH OWNER = postgres;"
    cursor.execute(sql_create_database)
    cursor.close()


if __name__ == "__main__":
    create_database()
