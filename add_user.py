import sqlite3
import uuid
from user import User


def add_user(user_name, user_email):
    if User.find_by_name_and_email(user_name, user_email):
        print(
            f'A user with the user name "{user_name}" and email "{user_email}" already exists.')
        return None
    user_key = uuid.uuid4().hex
    while User.find_by_api_key(user_key):
        user_key = uuid.uuid4().hex

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    query = 'INSERT INTO users VALUES (NULL, ?, ?, ?)'
    cursor.execute(query, (user_name, user_email, user_key))

    connection.commit()
    connection.close()

    print(
        f'User "{user_name}" ("{user_email}") created successfully. The user api key is "{user_key}"')


def delete_user(user_name, user_email):
    user = User.find_by_name_and_email(user_name, user_email)

    if user is None:
        print(
            f'A user with the user name "{user_name}" email "{user_email}" does not exist.')
        return None

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = 'DELETE FROM users WHERE user_name=? AND user_email=?'
    cursor.execute(query, (user_name, user_email))

    connection.commit()
    connection.close()

    print(f'User "{user_name}" ("{user_email}") deleted successfully.')


# Send an email to the user with the user key
def send_user_key(user_name, user_email):
    user = User.find_by_name_and_email(user_name, user_email)
    if user is None:
        print(
            f'A user with the user name "{user_name}" email "{user_email}" does not exist.')
        return None
    # Send email with user key
    # Your email sending code comes here.
    print(f'An email with the user key has been sent to "{user_email}"')


if __name__ == '__main__':
    # add a user to the database
    add_user('test', 'test@test.com')
