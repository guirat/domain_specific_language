RUNPIPENV :=pipenv run
MANAGE := python manage.py

install:
	pip install pipenv
	pipenv install

migrations:
	$(RUNPIPENV) $(MANAGE) makemigrations

migrate:
	$(RUNPIPENV) $(MANAGE) migrate

run:
	$(RUNPIPENV) $(MANAGE) runserver 8000

test:
	$(RUNPIPENV) pytest

format:
	$(RUNPIPENV) black .

lint:
	$(RUNPIPENV) flake8 --doctests .

create_db:
	$(RUNPIPENV) python create_drop_db.py
	$(RUNPIPENV) $(MANAGE) makemigration
	$(RUNPIPENV) $(MANAGE) migrate
	$(RUNPIPENV) python populate_db.py

drop_db:
	$(RUNPIPENV) python -c 'from create_drop_db import drop_database; drop_database()'