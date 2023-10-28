import sys
import getpass
import hashlib
import json
import os

from app.serveces.user import User
from app.serveces.balance import Balance
from app.dao.user_dao import UserDao
from app.dao.balance_dao import BalanceDao


def registration() -> None:
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
    balance = Balance(login, 100)
    BalanceDao().create(balance)


def login() -> None:
    while True:
        login = input("Введите ваш login: ")
        input_hashpass = getpass.getpass("Введите пароль: ")
        hashpass = hashlib.sha256(input_hashpass.encode("utf-8")).hexdigest()

        user_dao = UserDao()
        user = user_dao.find_by_login(login)

        if not user:
            print("Пользователь не найден!")
            continue
        if user.hashpass != hashpass:
            print("Неверный пароль!")
            continue
        print('Авторизация успешна. Добро пожаловать,', login)
        data = {
            "login": login,
            "hashpass": hashpass,
        }
        if not os.path.exists(".cache"):
            os.makedirs(".cache")
        with open(".cache/data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        break


def whoami() -> None:
    if not os.path.exists(".cache/data.json"):
        print("Вы не авторизованы")
        return
    with open('.cache/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    login = data['login']

    user_dao = UserDao()
    user = user_dao.find_by_login(login)

    if not user:
        print("Такого пользователя нет!")
        return
    print((
        f"Добро пожаловать {user.login}!\n"
        f"Ваш возраст: {user.age} лет\n"
        f"Ваш номер телефона: {user.phone_number}\n"
        f"Ваша почта: {user.email}"
    ))


def logout() -> None:
    filename = '.cache/data.json'
    if os.path.exists(filename):
        os.remove(filename)
    print("Вы вышли из системы!")


def get_local_data():
    if not os.path.exists(".cache/data.json"):
        return None
    with open('.cache/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def transfer():
    data = get_local_data()
    if not data:
        print("Вы не авторизованы!")
        return

    user = UserDao().find_by_login(data['login'])
    assert(user != None)
    print(user.login)
    login = input("Введите логин получателя: ")
    amount = int(input("Введите сумму: "))
    target_user = UserDao().find_by_login(login)
    if not target_user:
        print("Такого пользователя не существует")
        return
    balance = BalanceDao().find_by_login(user.login)
    assert(balance != None)
    target_balance = BalanceDao().find_by_login(login)
    assert(target_balance != None)
    balance.balance -= amount
    target_balance.balance += amount
    BalanceDao().update(balance)
    BalanceDao().update(target_balance)
    print("Перевод выполнен успешно!")



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
    elif command == "transfer":
        transfer()
    else:
        print("БЛЯ РЕБЯТ ЧЕ ЕБАНУЛИСЬ СОВСЕМ?")
        return 1
    return 0


if __name__ == '__main__':
    main()

