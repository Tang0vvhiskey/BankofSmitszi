import sqlite3
from app.serveces.user import User


class UserDao:
    def create(self, user):
        db = sqlite3.connect("bank.db")
        c = db.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS
                users (login TEXT,
                    hashpass TEXT,
                    age INT,
                    phone_number TEXT,
                    email TEXT)""")
        c.execute("""INSERT INTO users VALUES(?, ?, ?, ?, ?)""",
                  (user.login, user.hashpass, user.age,
                   user.phone_number, user.email))
        db.commit()
        db.close()

    def find_by_login(self, login):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
        data = cursor.fetchone()
        conn.close()
        if not data:
            return None

        return User(data[0], data[1], data[2], data[3], data[4])
