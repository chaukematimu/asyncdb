# asyncdb

Asynchronous postgresql database package.

## Requirements

Python 3.10+

## Installation

```shell
$ git clone git@github.com:chaukematimu/asyncdb.git
$ cd asyncdb
$ sed -ie 's/<DB_NAME>/test/' asyncdb/setup.sql
$ sed -ie 's/<DB_USER>/test/' asyncdb/setup.sql
$ sed -ie 's/<DB_USER_PASSWORD>/test/' asyncdb/setup.sql
$ script/setup
```

## Common Errors:

Solution :

`script/setup: line 11: psql: command not found`

Solution :

```shell
brew unlink postgresql@15 && brew link postgresql@15 --force
```

## Migrations

Generate new migration:

```shell
$ alembic revision --autogenerate -m "Added oauth2 tables"
```

Run Migrations :

```shell
$ alembic upgrade head
```