import sqlite3
import uuid


class User():

    def __init__(self, _id, user_name, user_email, user_key=None):
        self.id = _id
        self.user_name = user_name
        self.user_email = user_email
        self.user_key = user_key or uuid.uuid4().hex

    @classmethod
    def find_by_name_and_email(cls, user_name, user_email):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE user_name=? AND user_email=?"
        result = cursor.execute(query, (user_name, user_email))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_api_key(cls, api_key):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE user_key=?"
        result = cursor.execute(query, (api_key,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    def __str__(self):
        return f'User name: {self.user_name} \nEmail: {self.user_email} \nAPI key: {self.user_key}'
