import sqlite3

class DatabaseWriter:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')

    def close(self):
        self.connection.close()

    def create_employee_db(self, employeeId, username, password, isManager):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO UserTable VALUES (?, ?, ?, ?)",
            (employeeId, username, password, int(isManager))
        )
        self.connection.commit()
    def edit_employee_db(self, oldemployeeId, newemployeeId, newusername, newpassword, newisManager):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            UPDATE UserTable
            SET employeeId = ?, username = ?, password = ?, isManager = ?
            WHERE employeeId = ?
            """,
            (newemployeeId, newusername, newpassword, int(newisManager), oldemployeeId)
        )
        self.connection.commit()
    def delete_employee_db(self, employeeId):
        cursor = self.connection.cursor()
        cursor.execute(
            "DELETE FROM UserTable WHERE employeeId = ?",
            (employeeId,)
        )
        self.connection.commit()

    def create_component_db(self, componentId, componentName, quantity, minQuantity, status):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO ComponentTable VALUES (?, ?, ?, ?, ?)",
            (componentId, componentName, quantity, minQuantity, status)
        )
        self.connection.commit()
    def edit_component_db(self, oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            UPDATE ComponentTable
            SET componentId = ?, componentName = ?, quantity = ?, minQuantity = ?, status = ?
            WHERE componentId = ?
            """,
            (newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus, oldcomponentId)
        )
        self.connection.commit()
    def delete_component_db(self, componentId):
        cursor = self.connection.cursor()
        cursor.execute(
            "DELETE FROM ComponentTable WHERE componentId = ?",
            (componentId,)
        )
        self.connection.commit()

    def create_log_db(self, logId, action, date, time):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO LogTable VALUES (?, ?, ?, ?)",
            (logId, action, date, time)
        )
        self.connection.commit()

