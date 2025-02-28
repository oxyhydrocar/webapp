import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

USERNAME = "admin"
PASSWORD = "password123"

def login(user, pw):
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pw}'"
    result = cursor.execute(query).fetchall()
    return result

user = input("Enter username: ")
pw = input("Enter password: ")
print(login(user, pw))

conn.close()
