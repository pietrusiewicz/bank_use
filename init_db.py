import sqlite3

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create Clients table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Klienci (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    address TEXT NOT NULL,
    pesel TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance REAL DEFAULT 0.0
)
''')

# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT 0
)
''')

conn.commit()
conn.close()