from user import User
from orders import Order
from employees import Employees

class Client(User):
    def __init__(self, name, password, history: str, total_cost: int, visit_date: str):
        super().__init__(name, password, role='client')
        self.history = history
        self.total_cost = total_cost
        self.visit_date = visit_date
        self.basket = [] 

    def clients(self):
        print(f"Добро пожаловать, {self.name}!")
        print(f"Роль: {self.role}")

    def users_prava(self, orders, employees):
        while True:
            print("Выбор действия:")
            print("1. Просмотреть каталог билетов")
            print("2. Найти билет")
            print("3. Купить билет")
            print("4. Просмотреть историю поездок")
            print("5. Сортировать по стоимости билета")
            print("6. Сортировать по рейтингу таксистов")
            print("7. Сортировать по опыту таксистов")
            print("8. Выйти")
            try:
                vibor2 = int(input("Выбор: "))
            except ValueError:
                print("Введите корректное число!")
                continue

            if vibor2 == 1:
                print("Просмотреть каталог билетов")
                for order in orders:
                    print(Order.print_order(order))

            elif vibor2 == 2:
                print("Найти билет")
                bilet = input("Выберете маршрут (Место отправки-Место назначения): ")
                for order in orders:
                    if bilet in order.title:
                        print(f"Билет найден: Маршрут: {order.title}, Стоимость: {order.cost} руб., Класс: {order.classTicket}")
                        s = input("Хотите приобрести? да/нет: ").strip().lower()
                        if s == 'да':
                            print("Поздравляю, вы успешно купили билет!")
                            self.basket.append(order)
                            print(f"Билет {order.title} добавлен в корзину!")
                        break
                else:
                    print("К сожалению, такого билета нет")

            elif vibor2 == 3:
                Order.buy_bilet(self, orders)

            elif vibor2 == 4:
                print(f"История Ваших поездок: {self.history}")

            elif vibor2 == 5:
                Order.sort_cost(orders)

            elif vibor2 == 6:
                Employees.sort_employees_rat(employees)

            elif vibor2 == 7:
                Employees.sort_employees_exp(employees)

            elif vibor2 == 8:
                print("Выход")
                break  

            else:
                print("Неверно")

            vibor3 = input("Хотите продолжить? (да/нет): ").strip().lower()
            if vibor3 != "да":
                print("Выход из программы.")
                break
