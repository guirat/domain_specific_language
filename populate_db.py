import os

# Need to run this before calling models from application!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "domspeclang.settings")
import django

# Import settings
django.setup()

from town.models import Town
from faker import Faker
import random


fake = Faker()


def populate_db():
    for i in range(10):
        Town.objects.create(
            code=fake.random_int(),
            name=fake.city(),
            population=fake.random_int(),
            average_age=random.uniform(10.5, 75.5),
            district_code=fake.random_int(),
            department_code=fake.random_int(),
            region_code=fake.random_int(),
            region_name=fake.street_name(),
        )


if __name__ == "__main__":
    populate_db()
