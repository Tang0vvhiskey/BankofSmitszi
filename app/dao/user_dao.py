import sqlite3


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
        c.execute("""
            INSERT INTO users VALUES(?, ?, ?, ?, ?)""",
                (user.login, user.hashpass, user.age, user.phone_number, user.email))
        db.commit()
        db.close()
