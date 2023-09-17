import sys
import getpass
import hashlib

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

def login():
    print("логинимся")

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