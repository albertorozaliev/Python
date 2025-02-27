from user import User
from orders import Order
from functools import reduce
class Admin(User):
    def __init__(self, name, password, role):
        super().__init__(name, password, role)
        
    def admins(self):
        print(f"Добро пожаловать, {self.name}!")
        print(f"Роль: {self.role}")
    
    def admins_prava(self, orders,employees):
        while True:
            print("Выбор действия:")
            print("1. Добавить билет\n"
              "2. Удалить билет\n"
              "3. Просмотр количества работников в фирме\n"
              "4. Расчет общей стоимости билетов\n"
              "5. Редактирование билетов\n"
              "6. Выйти")
            try:
                vibor_admin = int(input("Выбор: "))
            except ValueError:
                print("Введите корректное число!")
                continue

            if vibor_admin == 1:
                print("Добавить билет")
                Order.add_order(orders)
                print("Обновленный список заказов:")
                for order in orders:
                    print(order)
            elif vibor_admin == 2:
                print("Удалить билет")
                Order.remove_order(orders)
                print("Обновленный список заказов:")
                for order in orders:
                    print(order)
            elif vibor_admin == 3:
                print("Просмотр количества работников в фирме")
                count_employees = len(employees)
                print(f"Общее количество работников: {count_employees}")
            elif vibor_admin == 4:
                print("Расчет общей и средней стоимости билетов")
                costs=map(lambda order: order.cost, orders)           #map
                total_cost=sum(costs)/len(orders)
                costs2 = reduce(lambda order2, order:order2+order.cost,orders,0) #reduce
                print(f"Общая стоимость билетов: {costs2} Средняя стоимость всех билетов: {total_cost}")
            elif vibor_admin == 5:
                print("Редактирование билетов")
                Order.edit_order(orders)
                print("Список заказов:")
                for order in orders:
                    print(f"Маршрут: {(order.title)} "
                    f"Стоимость: {order.cost} рублей, "
                    f"Класс: {order.classTicket}")
            elif vibor_admin == 6:
                print("Выход")
                break  
            else:
                print("Неверно!")
            vibor3 = input("Хотите продолжить? (да/нет): ").lower().strip()
            if vibor3 != "да":
                print("Выход из программы.")
                break

        