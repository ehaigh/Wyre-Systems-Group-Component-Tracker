#need source to createEmployee, createComponent and createLog implementation from other classes

class DatabaseReader:
    def __init__(self, connection):
        self.connection = connection

        self.createEmployees()
        self.createComponents()
        self.createLogs()
    def createEmployees():
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM UserTable")
        for row in cursor.fetchall():
            createEmployee(row[0], row[1], row[2], True if row[3] == 1 else False)
    def createComponents():
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ComponentTable")
        for row in cursor.fetchall():
            createComponent(row[0], row[1], row[2], row[3], row[4])
    def createLogs():
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM UserTable")
        for row in cursor.fetchall():
            createLog(row[0], row[1], row[2], row[3])