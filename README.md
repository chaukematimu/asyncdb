# asyncdb

Asynchronous postgresql database package.

## Requirements

Python 3.10+

## Installation

```shell
$ pip install asyncdb
$ cd asyncdb
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
$ alembic revision --autogenerate -m "Added test table"
```

Run Migrations :

```shell
$ alembic upgrade head
```