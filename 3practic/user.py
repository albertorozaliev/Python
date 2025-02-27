class User(object):
    def __init__(self, name: str, password: str, role:str):
        self.name = name
        self.__password = password
        self.role = role


    def getName(self):
        return f"{self.name} {self.role}"
    
    def get_password(self):
        return self.__password
    
    def set_password(self, new_password: str):
        self.__password = new_password