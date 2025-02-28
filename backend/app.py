import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"

def login(user, pw):
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pw}'"  # SQL Injection risk!
    result = cursor.execute(query).fetchall()
    return result

# No error handling
user = input("Enter username: ")
pw = input("Enter password: ")
print(login(user, pw))  # Outputs raw DB result

conn.close()
