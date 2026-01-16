import sqlite3

class DatabaseReader:
    def __init__(self, employeeController, componentController, logController):
        self.connection = None
        self.employeeController = employeeController
        self.componentController = componentController
        self.logController = logController

    def load_all(self):
        self.connection = sqlite3.connect('database.db')
        self.load_employees()
        self.load_components()
        self.load_logs()
        self.connection.close()
        self.connection = None

    def load_employees(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM UserTable")
        for row in cursor.fetchall():
            employeeId, username, password, isManager = row
            self.employeeController.create_employee(employeeId, username, password, isManager, updateDatabase=False)

    def load_components(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ComponentTable")
        for row in cursor.fetchall():
            componentId, componentName, quantity, minQuantity, status = row
            self.componentController.create_component(componentId, componentName, quantity, minQuantity, status, updateDatabase=False)

    def load_logs(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM LogTable")
        for row in cursor.fetchall():
            logId, action, date, time = row
            self.logController.create_log(logId, action, date, time, updateDatabase=False)
        




