import sqlite3
from typing import Optional

from app.serveces.balance import Balance



class BalanceDao:
    def create(self, balance: Balance) -> None:
        db = sqlite3.connect("bank.db")
        c = db.cursor()

        c.execute("""
            CREATE TABLE IF NOT EXISTS
                balances (login TEXT,
                    balance INT)""")
        c.execute("""INSERT INTO balances VALUES(?, ?)""",
                  (balance.login, balance.balance))
        db.commit()
        db.close()


    def find_by_login(self, login: str) -> Optional[Balance]:
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM balances WHERE login = ?', (login,))
        data = cursor.fetchone()
        conn.close()
        if not data:
            return None

        return Balance(data[0], int(data[1]))


    def update(self, balance: Balance) -> None:
        db = sqlite3.connect("bank.db")
        c = db.cursor()
        c.execute('UPDATE balances SET balance = ? WHERE login = ?;', (balance.balance, balance.login))
        db.commit()
        db.close()