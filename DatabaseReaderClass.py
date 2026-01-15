from EmployeeControllerClass import create_employee
from ComponentControllerClass import create_component
from LogControllerClass import create_log

class DatabaseReader:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')

    def close(self):
        self.connection.close()

    def load_all(self):
        self.load_employees()
        self.load_components()
        self.load_logs()
    def load_employees(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM UserTable")
        for row in cursor.fetchall():
            isActive = bool(row[3])
            create_employee(row[0], row[1], row[2], isActive, False)
    def load_components(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ComponentTable")
        for row in cursor.fetchall():
            create_component(row[0], row[1], row[2], row[3], row[4], False)
    def load_logs(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM LogTable")
        for row in cursor.fetchall():
            create_log(row[0], row[1], row[2], row[3], False)
        



