#source create_employee_db, edit_employee_db and delete_employee_db from databaseWriter

import hashlib

from EmployeeClass import Employee

class EmployeeController:
    def __init__(self):
        pass
    def create_employee(self, employeeId, username, password, isManager, updateDatabase, employeeObjects):
        employee = Employee(employeeId, username, self.hash_password(password), isManager)
        employeeObjects.append(employee)
        if updateDatabase:
            create_employee_db(employeeId, username, self.hash_password(password), isManager)
        return employeeObjects
    def edit_employee(self, oldemployeeId, newemployeeId, newusername, newpassword, newisManager, employeeObjects):
        itemUpdated = False
        for employee in employeeObjects:
            employeeUpdated = False
            if (oldemployeeId == employee.get_employeeId()):
                itemUpdated = True
                if (newemployeeId != "") and (newemployeeId != None):
                    employee.set_employeeId(newemployeeId)
                    employeeUpdated = True
                if (newusername != "") and (newusername != None):
                    employee.set_username(newusername)
                    employeeUpdated = True
                if (newpassword != "") and (newpassword != None):
                    employee.set_password(self.hash_password(newpassword))
                    employeeUpdated = True
                if (newisManager != "") and (newisManager != None):
                    employee.set_isManager(newisManager)
                    employeeUpdated = True
            if employeeUpdated:
                edit_employee_db(oldemployeeId, employee.get_employeeId(), employee.get_username(), employee.get_password(), employee.isManager())
        return employeeObjects, itemUpdated
    def delete_employee(self,  employeeId, employeeObjects):
        itemDeleted = False
        for employee in employeeObjects:
            if (employeeId == employee.get_employeeId()):
                itemDeleted = True
                delete_employee_db(employeeId)
                employeeObjects.remove(employee)
        return employeeObjects, itemDeleted
    def hash_password(self, rawPassword):
        #encode into bytes
        passwordBytes = rawPassword.encode('utf-8')
        #create SHA-256 hash
        hashedPassword = hashlib.sha256(passwordBytes).hexdigest()
        return hashedPassword
        
    def validate_credentials(self, username, password, employeeObjects):
        validated = False
        for employee in employeeObjects:
            if username == employee.get_username():
                if self.hash_password(password) == employee.get_password():
                    validated = True
        return validated