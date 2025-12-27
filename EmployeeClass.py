class Employee:
    def __init__(self, employeeId, username, password, isManager):
        self.employeeId = employeeId
        self.username = username
        self.password = hashPassword(password)
        self.isManager = isManager