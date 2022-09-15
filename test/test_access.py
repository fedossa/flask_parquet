import duckdb
import pandas as pd

duckdb.query('LOAD httpfs;')
api_key = 'the_api_key'

file_1 = 'iris'
file_2 = 'flights'

iris = duckdb.query(
    f"SELECT * FROM read_parquet('http://127.0.0.1:5000/{api_key}/{file_1}')",
).df()
print(iris.head(5))

flights = duckdb.query(
    f"SELECT * FROM read_parquet('http://127.0.0.1:5000/{api_key}/{file_2}')",
).df()
print(flights.head(5))
