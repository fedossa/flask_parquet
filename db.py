import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user_name text, user_email text, user_key text)"
cursor.execute(create_table)

connection.commit()

connection.close()
