from user import User

class Employees(User):
    def __init__(self, name, password,  history: str, rating:int, experience:int):
        super().__init__(name, password, role='employee')
        self.history = history
        self.rating = rating
        self.experience = experience
        
    def printEmp(self):
        print("Вы таксист") 
        
            
    def sort_employees_rat(employees):
     print("Сортировка по рейтингу:")
     for i in sorted(employees, key=lambda emp: emp.rating):  
        print(f"Имя: {i.name}, Рейтинг: {i.rating}, Опыт: {i.experience}, История: {i.history}")

    def sort_employees_exp(employees):
     print("Сортировка по опыту:")
     for i in sorted(employees, key=lambda emp: emp.experience): 
        print(f"Имя: {i.name}, Рейтинг: {i.rating}, Опыт: {i.experience}, История: {i.history}")