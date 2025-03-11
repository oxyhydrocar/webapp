import sqlite3

from backend.cal import greet_user

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

USERNAME = "admin"
PASSWORD = "password123"

def login(user, pw):
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pw}'"
    greet_user(user, "15")
    result = cursor.execute(query).fetchall()
    return result

user = input("Enter username: ")
pw = input("Enter password: ")
print(login(user, pw))

conn.close()
