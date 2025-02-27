class A:
    def get_input(self):
        self.a = int(input("Введите число: "))  # Вводим число
        print(self.a)

# Создаем объект
obj = A()
obj.get_input()  # Вызов метода для ввода

