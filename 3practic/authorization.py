from client import Client
from employees import Employees
from exportImport import ImpExp

class Authorization:
    def __init__(self, login: str, password: int):
        self.login = login
        self.password = password

    @staticmethod
    def authorizationUsers(users, employees, orders):

        while True:
            try:
                vibor = int(input("Выберите способ входа: 1) Пользователь \n"
                                  "2) Админ\n"
                                  "3) Таксист\n"
                                  "4) Выйти\n"
                                  "Ответ: "))
            except ValueError:
                print("Введите число!")
                continue

            if vibor in [1, 2, 3]:
                username = input("Введите логин: ")
                password = input("Введите пароль: ")


                for user in users:
                    if user.name == username and user.get_password() == password:
                        print("Успешная авторизация!")

                        if vibor == 1 and user.role == 'client':
                            user.clients()
                            user.users_prava(orders, employees)
                        elif vibor == 2 and user.role == 'admin':
                            user.admins()
                            user.admins_prava(orders, employees)
                        elif vibor == 3 and user.role == 'employee':
                            user.printEmp()
                        break
                else:
                    print("Неверный логин или пароль")

            elif vibor == 4:
                print("Вы вышли из авторизации.")
                break
            else:
                print("Введите число от 1 до 4")

    @staticmethod            
    def registrationUsers(users):
        print("Регистрация")
        username = input("Введите логин: ")
        password = input("Введите пароль: ")

        while True:
            try:
                new_role = int(input("Введите роль: 1) Client  2) Employee: "))
                if new_role == 1:
                    role = "client"
                    break
                elif new_role == 2:
                    role = "employee"
                    break
                else:
                    print("Некорректный выбор")
            except ValueError:
                print("Введите число 1 или 2")

        for user in users:
            if user.name == username:
                print("логин уже существует")
                return
        if role == "client":
            new_user = Client(username,"",[],0,'28.02.25')
        else:
            new_user = Employees(username,"",[],0,0)
            
        new_user.set_password(password)
            
        users.append(new_user)
        
        ImpExp.exportUsers(users)

        
