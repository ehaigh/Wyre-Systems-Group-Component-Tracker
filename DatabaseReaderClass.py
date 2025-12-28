#need source to createEmployee, createComponent and createLog implementation from other classes

class DatabaseReader:
    def __init__(self, connection):
        self.connection = connection

    def load_all(self):
        employeeObjects = self.load_employees()
        componentObjects = self.load_components()
        logObjects = self.load_logs()
        return employeeObjects, componentObjects, logObjects
    def load_employees(self):
        employeeObjects = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM UserTable")
        for row in cursor.fetchall():
            isActive = bool(row[3])
            employeeObjects = create_employee(row[0], row[1], row[2], isActive, False, employeeObjects)
        return employeeObjects
    def load_components(self):
        componentObjects = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ComponentTable")
        for row in cursor.fetchall():
            componentObjects = create_component(row[0], row[1], row[2], row[3], row[4], False, componentObjects)
        return componentObjects
    def load_logs(self):
        logObjects = []
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM LogTable")
        for row in cursor.fetchall():
            logObjects = create_log(row[0], row[1], row[2], row[3], False, logObjects)
        return logObjects
        
