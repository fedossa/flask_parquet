# flask_parquet

Toy api to serve parquet files over authenticated api

Usage

- Run `db.py` to initialize a `sqlite3` database with a user table
- Use the `create_user.py` script to create a user and save the key
- start the flask app


A test of how clinets can access the files is in `test/test_access.py`