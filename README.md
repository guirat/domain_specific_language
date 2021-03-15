# domain_specific_language

This is an api for a domain specific language to retrieve data from database throw dsl json query.


## Getting started
Dependencies required:
* Postgresql
* Makefile
* Python

Start by installing dependencies:

```
make install
```

```
make create_db
```
Then run the app
```
make run
```
it will run on the default http://127.0.0.1:8000/

----------

to make migrations:
```
make migrations
```
to migrate:
```
make migrate
```

to lunch tests:
```
make test
```
to format the code for a better PEP8 friendly:
```
make format
```
to lint the code:
```
make lint
```
to delete the database:
```
make drop_db
```


