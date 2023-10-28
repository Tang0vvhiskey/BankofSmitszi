class User:
    def __init__(self, login: str, hashpass: str, age: str, phone_number: str, email: str) -> None:
        self.login: str = login
        self.age: str = age
        self.phone_number: str = phone_number
        self.email: str = email
        self.hashpass: str = hashpass

