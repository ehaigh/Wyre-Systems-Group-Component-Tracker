#need source to createEmployee, createComponent and createLog implementation from other classes

class DatabaseReader:
    def __init__(self, connection):
        self.connection = connection

    def load_all(self):
        self.load_employees()
        self.load_components()
        self.load_logs()
    def load_employees(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM UserTable")
        for row in cursor.fetchall():
            isActive = bool(row[3])
            create_employee(row[0], row[1], row[2], isActive)
    def load_components(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ComponentTable")
        for row in cursor.fetchall():
            create_component(row[0], row[1], row[2], row[3], row[4])
    def load_logs(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM LogTable")
        for row in cursor.fetchall():
            create_log(row[0], row[1], row[2], row[3])
