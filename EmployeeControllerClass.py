import hashlib
from EmployeeClass import Employee
from DatabaseWriterClass import DatabaseWriter


class EmployeeController:
    def __init__(self):
        #Creates empty list of employee objects
        self.employeeObjects = []
        #Access to database
        self.db = DatabaseWriter()
    def create_employee(self, employeeId, username, password, isManager, updateDatabase=True):
        #Password instantly hashed for security
        hashedPassword = self.hash_password(password)
        #Creates employee object
        employee = Employee(employeeId, username, hashedPassword, isManager)
        #Adds to list of employees
        self.employeeObjects.append(employee)
        #If necessary, update the database.
        if updateDatabase:
            self.db.create_employee_db(employeeId, username, hashedPassword, isManager)
    def edit_employee(self, oldemployeeId, newemployeeId, newusername, newpassword, newisManager, doHashPassword):
        #Check if employeeId matches
        for employee in self.employeeObjects:
            if employee.get_employeeId() == oldemployeeId:
                #If matches, set new attributes
                if newemployeeId:
                    employee.set_employeeId(newemployeeId)
                if newusername:
                    employee.set_username(newusername)
                if newpassword and doHashPassword:
                    employee.set_password(self.hash_password(newpassword))
                if newisManager is not None:
                    employee.set_isManager(newisManager)
                #Edit employee in database
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
        #Check if employeeId matches
        for employee in self.employeeObjects:
            if employee.get_employeeId() == employeeId:
                #If matches, delete employee object and from database
                self.employeeObjects.remove(employee)
                self.db.delete_employee_db(employeeId)
                return True
        return False
    def get_employee_objects(self):
        return self.employeeObjects
    def validate_credentials(self, username, password):
        #Hashes twice as employee object's passwords are hashed again on creation
        hashed = self.hash_password(self.hash_password(password))
        for employee in self.employeeObjects:
            #If matches, accept credentials
            if employee.get_username() == username and employee.get_password() == hashed:
                return True, employee.get_isManager()
        #If doesn't match, don't accept credentials        
        return False, None
    def hash_password(self, rawPassword):
        #Hashes password with a one-way algorithm for security
        return hashlib.sha256(rawPassword.encode("utf-8")).hexdigest()
