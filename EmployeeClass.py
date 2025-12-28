#need to source hashPassword

class Employee:
    def __init__(self, employeeId, username, password, isManager):
        self.employeeId = employeeId
        self.username = username
        self.password = hashPassword(password)
        self.isManager = isManager
    def get_employeeId(self):
        return self.employeeId
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_isManager(self):
        return self.isManager
    def set_employeeId(self, employeeId):
        self.employeeId = employeeId
    def set_username(self, username):
        self.username = username
    def set_password(self, password):
        self.password = hashPassword(password)
    def set_isManager(self, isManager):
        self.isManager = isManager
