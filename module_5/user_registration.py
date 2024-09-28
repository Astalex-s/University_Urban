class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибут: логин
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход \n2 - Регистрация \n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f"Вход выполнен, {login}")
                    break
                else:
                    print("Не верный пароль")
                    continue
            else:
                print("Пользователь не найден")
                continue
        if choice == 2:
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if any(c.isupper() for c in password) and any(c.isdigit() for c in password) and len(password) >= 4:
                print("Вы зарегистрированы")
            else:
                print("Пароль должен состоять из не менее чем 4 символов, содержать минимум одну цифру и одну букву "
                      "в верхнем регистре")
            if password != password2:
                print("Пароли не совпадают, попробуйте еще раз")
                continue
            database.add_user(user.username, user.password)
            print(database.data)
