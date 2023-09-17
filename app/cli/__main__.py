import sys
import getpass
import hashlib
import sqlite3
import getpass


from app.serveces.user import User
from app.dao.user_dao import UserDao


def registration():
    login = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    phone_number = input("Введите ваш номер телефона: ")
    email = input("Введите ваш email: ")
    while True:
        password = getpass.getpass("Введите ваш пароль: ")
        password_repet = getpass.getpass("Подтвердите пароль: ")
        if password == password_repet:
            break
        else:
            print("Попробуйте еще...")
            continue
    print("Пароль принят")
    hashpass = hashlib.sha256(password.encode("utf-8")).hexdigest()
    user = User(login, hashpass, age, phone_number, email)
    user_dao = UserDao()
    user_dao.create(user)


def authenticate(login, hashpass):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    # Выбираем запись пользователя с указанным логином из базы данных
    cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
    user = cursor.fetchone()

    # Проверяем, найден ли пользователь и совпадает ли введенный пароль с хешем в базе данных
    if user and user[1] == hashpass:
        print('Авторизация успешна. Добро пожаловать,', login)
        return True
    else:
        print('Ошибка авторизации. Пожалуйста, проверьте логин и пароль.')
        return False

    conn.close()


def login():
    while True:
        login = input("Введите ваш login: ")
        input_hashpass = getpass.getpass("Введите пароль: ")
        hashpass = hashlib.sha256(input_hashpass.encode("utf-8")).hexdigest()

        if authenticate(login, hashpass):
            break


def whoami():
    print("ХТО Я?")


def logout():
    print("Выход")


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    command = args[0]
    if command == 'registration':
        registration()
    elif command == 'login':
        login()
    elif command == 'whoami':
        whoami()
    elif command == 'logout':
        logout()
    else:
        print("БЛЯ РЕБЯТ ЧЕ ЕБАНУЛИСЬ СОВСЕМ?")
        return 1
    return 0



if __name__ == '__main__':
    main()