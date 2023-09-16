class User:
    def __init__(self, login, hashpass, age, phone_number, email):
        self.login = login
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.hashpass = hashpass