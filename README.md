# acme-be

Space ACME backend re-built with fastAPI.

## Getting Started

This backend uses FastAPI with Tortoise OEM, postgres seeded and migrated with aeirch, all contained with docker.
You'll need to install dependencies with pip. Run `python3 -m pip install -r requirements.txt` from the directory where requirements.txt is located.

### Starting Docker

run `docker-compose up -d --build` from the root directory (where docker-compose.yml is located).
To tear down images, run `docker-compose down -v`.
You can ensure the server is live by visting `localhost:8080`.

### Postgres Setup

To initialize the database, run `docker-compose exec acme aerich init -t app.db.TORTOISE_ORM`
Create the first migration: `docker-compose exec acme aerich init-db`
To ensure it was succesful, you can query the postgres database by using `docker-compose exec acme-db psql -U postgres`, `\c acme_dev`, `\dt`. It should list the created relations.

#### Troubleshooting

If the postgres setup commands have been run but you don't see the relations or you get a "model not found" error, try running: `docker-compose exec acme aerich upgrade`. This will create any tables defined within the `upgrade` method.

### Testing

This project should try to use test driven developement whenever possible. This means writing tests, ensuring failures, and then writing the code to make that test pass.
This backend uses Pytest as it's testing framework.

Run tests: `docker-compose exec acme python -m pytest`
Useful commands:

```
# normal run
$ docker-compose exec acme python -m pytest

# disable warnings
$ docker-compose exec acme python -m pytest -p no:warnings

# run only the last failed tests
$ docker-compose exec acme python -m pytest --lf

# run only the tests with names that match the string expression
$ docker-compose exec acme python -m pytest -k "summary and not test_read_summary"

# stop the test session after the first failure
$ docker-compose exec acme python -m pytest -x

# enter PDB after first failure then end the test session
$ docker-compose exec acme python -m pytest -x --pdb

# stop the test run after two failures
$ docker-compose exec acme python -m pytest --maxfail=2

# show local variables in tracebacks
$ docker-compose exec acme python -m pytest -l

# list the 2 slowest tests
$ docker-compose exec acme python -m pytest --durations=2
```
