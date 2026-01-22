import sqlite3

class DatabaseReader:
    def __init__(self, employeeController, componentController, logController):
        #Establishes controller connections
        self.connection = None
        self.employeeController = employeeController
        self.componentController = componentController
        self.logController = logController
    def load_all(self):
        #Establishes database connection
        self.connection = sqlite3.connect('database.db')
        #Loads all objects on initialisation
        self.load_employees()
        self.load_components()
        self.load_logs()
        #Closes database connection to prevent accidental use
        self.connection.close()
        self.connection = None
    def load_employees(self):
        #Selects all users in database
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM UserTable")
        for row in cursor.fetchall():
            employeeId, username, password, isManager = row
            #Creates each employee into object
            self.employeeController.create_employee(employeeId, username, password, isManager, updateDatabase=False)
    def load_components(self):
        #Selects all components in database
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ComponentTable")
        for row in cursor.fetchall():
            componentId, componentName, quantity, minQuantity, status = row
            #creates each component into object
            self.componentController.create_component(componentId, componentName, quantity, minQuantity, status, updateDatabase=False)
    def load_logs(self):
        #Selects all logs in database
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM LogTable")
        for row in cursor.fetchall():
            logId, action, date, time = row
            #Creates each log into object
            self.logController.create_log(logId, action, date, time, updateDatabase=False)


