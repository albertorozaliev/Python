from client import Client
from employees import Employees
from admin import Admin
class ImpExp:
    @staticmethod
    def exportUsers(users):
        with open('UsersFile.txt', 'w', encoding='utf-8') as file:
            for user in users:
                if user.role == "client":
                    file.write(f"{user.name} {user.get_password()} {user.role} {user.history} {user.total_cost} {user.visit_date}\n")
                elif user.role == "employee":
                    file.write(f"{user.name} {user.get_password()} {user.role} {user.history} {user.rating} {user.experience}\n")
        print("Данные сохранены!")


        
    @staticmethod 
    def importUsers():
        users = []
        try:
            with open('UsersFile.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 6 and parts[2] == "client":
                        users.append(Client(parts[0], parts[1], parts[3], float(parts[4]), parts[5]))
                    elif len(parts) == 6 and parts[2] == "employee":
                        users.append(Employees(parts[0], parts[1], parts[3], float(parts[4]), int(parts[5])))  
                    elif len(parts) == 3 and parts[2] == "admin":
                        users.append(Admin(parts[0], parts[1], parts[2]))
            return users
        except FileNotFoundError:
            return []


        