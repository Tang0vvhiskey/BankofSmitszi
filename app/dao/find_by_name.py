# import sqlite3


# class UserDao_find_by_name:
#     def authenticate(self, login, hashpass):
#         conn = sqlite3.connect('bank.db')
#         cursor = conn.cursor()

#         cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
#         user = cursor.fetchone()

#         conn.close()

#         if user and user[1] == hashpass:
#             print('Авторизация успешна. Добро пожаловать,', login)
#             return True

#         else:
#             print('Ошибка авторизации. Пожалуйста, проверьте логин и пароль.')
#             return False

#         conn.close()