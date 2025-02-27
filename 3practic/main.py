from client import Client
from employees import Employees
from orders import Order
from admin import Admin
from authorization import Authorization
from exportImport import ImpExp

saved_users = ImpExp.importUsers()
clients = Client('Tom', 123, 'Москва-Воронеж', 4500, '2024-10-20')

admin = Admin('admin',123, 'admin')
employees1 = Employees('Maga', 123, 'Москва - Воронеж', 4.5, 10)
employees2 = Employees('Alex', 123, 'Москва - Пекин', 5, 8)

employees = [employees1, employees2]



users = saved_users + [clients] + employees + [admin]



print("Добро пожаловать в Такси-Везёт")
while True:
    try:
        choice = int(input("Выберите 1) Регистрация 2) Авторизация 3) Выйти: "))
        if choice == 1:
            Authorization.registrationUsers(users)
        elif choice == 2:
            Authorization.authorizationUsers(users, [], [])
        elif choice == 3:
            break
        else:
            print("Неверный выбор")
    except ValueError:
        print("Ошибка! Введите целое число.")







