import sqlite3
from werkzeug.security import generate_password_hash

class DatabaseOperations:
    def __init__(self, database='bank.db'):
        self.database = database

    def get_db(self):
        conn = sqlite3.connect(self.database)
        return conn

    def add_user(self, username, password):
        hashed_password = generate_password_hash(password, method='sha256')
        conn = self.get_db()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, hashed_password))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return False
        conn.close()
        return True

    def add_client(self, name, surname, address, pesel, email, phone, balance):
        conn = self.get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Klienci (name, surname, address, pesel, email, phone, balance) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, surname, address, pesel, email, phone, balance))
        conn.commit()
        conn.close()

    def get_user_id(self, username):
        conn = self.get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM Users WHERE username=?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user[0] if user else None

    def get_client(self, id):
        conn = self.get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Klienci WHERE id=?", (id,))
        row = cursor.fetchone()
        conn.close()
        return row