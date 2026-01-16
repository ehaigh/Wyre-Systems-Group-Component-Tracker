import hashlib
from EmployeeClass import Employee
from DatabaseWriterClass import DatabaseWriter


class EmployeeController:
    def __init__(self):
        self.employeeObjects = []
        self.db = DatabaseWriter()

    def create_employee(self, employeeId, username, password, isManager, updateDatabase=True):
        hashedPassword = self.hash_password(password)
        employee = Employee(employeeId, username, hashedPassword, isManager)
        self.employeeObjects.append(employee)

        if updateDatabase:
            self.db.create_employee_db(employeeId, username, hashedPassword, isManager)

    def edit_employee(self, oldemployeeId, newemployeeId, newusername, newpassword, newisManager, doHashPassword):
        for employee in self.employeeObjects:
            if employee.get_employeeId() == oldemployeeId:
                if newemployeeId:
                    employee.set_employeeId(newemployeeId)
                if newusername:
                    employee.set_username(newusername)
                if newpassword and doHashPassword:
                    employee.set_password(self.hash_password(newpassword))
                if newisManager is not None:
                    employee.set_isManager(newisManager)

                self.db.edit_employee_db(
                    oldemployeeId,
                    employee.get_employeeId(),
                    employee.get_username(),
                    employee.get_password(),
                    employee.get_isManager()
                )
                return True
        return False

    def delete_employee(self, employeeId):
        for employee in self.employeeObjects:
            if employee.get_employeeId() == employeeId:
                self.employeeObjects.remove(employee)
                self.db.delete_employee_db(employeeId)
                return True
        return False

    def get_employee_objects(self):
        return self.employeeObjects

    def validate_credentials(self, username, password):
        hashed = self.hash_password(password)
        for employee in self.employeeObjects:
            if employee.get_username() == username and employee.get_password() == hashed:
                return True, employee.get_isManager()
        return False, None

    def hash_password(self, rawPassword):
        return hashlib.sha256(rawPassword.encode("utf-8")).hexdigest()

