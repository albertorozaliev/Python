class Order(object):
    def __init__(self, title: str, cost: int, classTicket: str):
        self.title = title
        self.cost = cost
        self.classTicket = classTicket

    @staticmethod
    def add_order(orders):
        while True:
            title = input("Введите маршрут (Место отправки-Место назначения): ")

            while True:
                try:
                    cost = int(input("Введите стоимость билета: "))
                    if cost < 0:
                        print("Введи положительное число")
                        continue
                    break
                except ValueError:
                    print("Введите целое число")

            while True:
                ticket_class = input("Введите класс билета (Economy, Comfort, Premium, Comfort+): ")
                if ticket_class in ['Economy', 'Comfort', 'Premium', 'Comfort+']:
                    break
                else:
                    print("Неверный класс билета.")

            new_order = Order(title, cost, ticket_class)
            orders.append(new_order)
            print(f"Новый заказ добавлен: {new_order.title}, {new_order.cost} руб., {new_order.classTicket}")

            vibor4 = input("Хотите добавить еще один заказ? (да/нет): ").lower().strip()
            if vibor4 != 'да':
                break

    @staticmethod
    def remove_order(orders):
        for i, order in enumerate(orders, start=1):
            print(f"{i}. Маршрут: {order.title}, Стоимость: {order.cost}, Класс: {order.classTicket}")

        try:
            vibor = int(input("Введите номер маршрута, который хотите удалить: ")) - 1
            if 0 <= vibor < len(orders):
                removed_order = orders.pop(vibor)
                print(f"Маршрут {removed_order.title} успешно удален.")
            else:
                print("Введен некорректный номер.")
        except ValueError:
            print("Ошибка: введите корректное число.")

    @staticmethod
    def edit_order(orders):
        print("Список заказов:")
        for i, order in enumerate(orders, start=1):
            print(f"{i}. Маршрут: {order.title}, Стоимость: {order.cost}, Класс: {order.classTicket}")

        try:
            order_index = int(input("Введите номер заказа, который хотите отредактировать: ")) - 1
            if 0 <= order_index < len(orders):
                new_order = orders[order_index]
                print(f"Вы выбрали: {new_order.title}, Стоимость: {new_order.cost} руб., Класс: {new_order.classTicket}")

                print("Что вы хотите изменить?")
                print("1. Маршрут")
                print("2. Стоимость")
                print("3. Класс")
                choice = int(input("Введите номер изменения: "))

                if choice == 1:
                    new_title = input("Введите новый маршрут (Место отправления-Место назначения): ")
                    new_order.title = new_title
                    print(f"Маршрут успешно изменен на {new_title}.")
                elif choice == 2:
                    while True:
                        try:
                            new_cost = int(input("Введите новую стоимость: "))
                            if new_cost < 0:
                                print("Введи положительное число")
                                continue
                            break
                        except ValueError:
                            print("Ошибочка, введи целое число")

                    new_order.cost = new_cost
                    print(f"Стоимость успешно изменена на {new_cost}")
                elif choice == 3:
                    new_class = input("Введите новый класс (Economy, Comfort, Premium, Comfort+): ")
                    if new_class in ['Economy', 'Comfort', 'Premium', 'Comfort+']:
                        new_order.classTicket = new_class
                        print(f"Класс успешно изменен на {new_class}.")
                    else:
                        print("Некорректный класс билета.")
                else:
                    print("Некорректный выбор.")
            else:
                print("Неверный номер заказа.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите корректные данные.")

    @staticmethod
    def sort_cost(orders):
        print("Сортировка билетов по цене, выберите диапазон стоимости:")
        while True:
            try:
                num1 = int(input('Введите стоимость от: '))
                num2 = int(input('Введите стоимость до: '))
                if num1 < 0 or num2 < 0:
                    print("Стоимость должна быть положительным числом!")
                    continue
                if num1 >= num2:
                    print("Стоимость от должна быть меньше стоимости до!")
                    continue
                break
            except ValueError:
                print("Ошибочка! Введите целое число.")

        sorted_orders = [order for order in orders if num1 <= order.cost <= num2]

        if sorted_orders:
            print("Найденные билеты:")
            for order in sorted_orders:
                print(f"Маршрут: {order.title}, Стоимость: {order.cost} руб., Класс: {order.classTicket}")
        else:
            print("Билетов нет.")

    @staticmethod
    def buy_bilet(user, orders):
        print("Каталог билетов:")
        for i, order in enumerate(orders, start=1):
            print(f"{i}. Маршрут: {order.title}, Стоимость: {order.cost} руб., Класс: {order.classTicket}")

        try:
            vibor = int(input("Введите номер билета, который хотите добавить в корзину: ")) - 1
            if 0 <= vibor < len(orders):
                ticket = orders[vibor]
                user.basket.append(ticket)
                print(f"Билет {ticket.title} добавлен в корзину")

                vibor2 = input("Хотите удалить билеты из корзины? (да/нет): ").lower().strip()
                if vibor2 == 'да':
                    for i, ticket in enumerate(user.basket, start=1):
                        print(f"{i}. Маршрут: {ticket.title}, Стоимость: {ticket.cost} руб., Класс: {ticket.classTicket}")

                    try:
                        vibor3 = int(input("Введите номер билета, который хотите удалить из корзины: ")) - 1
                        if 0 <= vibor3 < len(user.basket):
                            removed_ticket = user.basket.pop(vibor3)
                            print(f"Билет {removed_ticket.title} был успешно удален")
                        else:
                            print("Введено неверное значение.")
                    except ValueError:
                        print("Неверный ввод.")
        except ValueError:
            print("Неверный ввод.")
    
    def __str__(self):
        return f"Маршрут: {self.title}, Стоимость: {self.cost} руб., Класс: {self.classTicket}"

    def __repr__(self):
        return self.__str__()
    @staticmethod
    def print_order(order):
        return f"Маршрут: {order.title}, Стоимость: {order.cost} руб., Класс: {order.classTicket}"
