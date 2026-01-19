import uuid
import datetime
import os
import csv

class UtilitiesController:
    def __init__(self, employeeController, componentController, logController, backupController):
        self.employeeController = employeeController
        self.componentController = componentController
        self.logController = logController
        self.backupController = backupController
    def initialiseSystem(self, dbReader):
        if dbReader:
            dbReader.load_all()
    def setUIController(self, uicontroller):
        self.uicontroller = uicontroller
    def manageBackup(self):
        self.uicontroller.create_popup("Successfully created backup")
        self.logController.create_log(str(uuid.uuid4()), "Successfully created backup", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        self.backupController.create_backup()
    def manageExport(self):
        exports_folder = os.path.join(os.getcwd(), "Exports")
        if not os.path.exists(exports_folder):
            os.makedirs(exports_folder)

        filepath = os.path.join(exports_folder, "export_" + str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".csv")

        try:
            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)

                writer.writerow(["Components:"])
                writer.writerow(["Component ID", "Name", "Quantity", "Minimum Quantity", "Status"])
                for row in self.getComponentData():
                    writer.writerow(row)

                writer.writerow([])

                writer.writerow(["Logs:"])
                writer.writerow(["Log ID", "Action", "Date", "Time"])
                for row in self.getLogData():
                    writer.writerow(row)

            self.uicontroller.create_popup("Successfully exported data\nFile saved at:" + filepath)
            self.logController.create_log(str(uuid.uuid4()), "Successfully exported data", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        except Exception as e:
            self.uicontroller.create_popup("Failed to export data with error:" + str(e))
            self.logController.create_log(str(uuid.uuid4()), "Failed to export data", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
    def getComponentData(self):
        componentObjects = self.componentController.get_component_objects()
        data = []

        for component in componentObjects:
            row = [
                component.get_componentId(),
                component.get_componentName(),
                component.get_quantity(),
                component.get_minQuantity(),
                component.get_status()
            ]
            data.append(row)

        return data
    def getEmployeeData(self):
        employeeObjects = self.employeeController.get_employee_objects()
        data = []
        for emp in employeeObjects:
            data.append([
                emp.get_employeeId(),
                emp.get_username(),
                emp.get_password(),
                "Yes" if emp.get_isManager() else "No"
            ])
        return data
    def getLogData(self):
        logObjects = self.logController.get_log_objects()
        data = []

        for log in logObjects:
            row = [
                log.get_logId(),
                log.get_action(),
                log.get_date(),
                log.get_time()
            ]
            data.append(row)

        return data
    def getAlertData(self):
        data = []
        componentObjects = self.componentController.get_component_objects()
        for component in componentObjects:
            if component.get_status() == "outOfStock":
                data.append(["Component with componentId=" + component.get_componentId() + " is out of stock"])
            if component.get_status() == "faulty":
                data.append(["Component with componentId=" + component.get_componentId() + " is faulty"])
            if component.get_quantity() < component.get_minQuantity:
                data.append(["Component with componentId=" + component.get_componentId() + " has quantity below minimum quantity"])
        return data
    def validateLogin(self, username, password):
        valid, isManager = self.employeeController.validate_credentials(username, password)
        if valid:
            self.logController.create_log(str(uuid.uuid4()), ("Successful login by username=" + username), datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        else:
            self.logController.create_log(str(uuid.uuid4()), "Unsuccessful login", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        return valid, isManager
    def validateAddEmployee(self, employeeId, username, password, isManager):
        validationMessage = ""
        employeeObjects = self.employeeController.get_employee_objects()

        for employee in employeeObjects:
            if employee.get_employeeId() == employeeId:
                validationMessage = "employeeId already exists"
                self.uicontroller.create_popup(validationMessage)

        if employeeId is None or employeeId == "":
            validationMessage = "employeeId must have a value"
            self.uicontroller.create_popup(validationMessage)
        elif not isinstance(employeeId, str):
            validationMessage = "employeeId must be correct type"
            self.uicontroller.create_popup(validationMessage)

        if username is None or username == "":
            validationMessage = "username must have a value"
            self.uicontroller.create_popup(validationMessage)
        elif not isinstance(username, str):
            validationMessage = "username must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif not (0 < len(username) <= 30):
            validationMessage = "username is not between 0 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        if password is None or password == "":
            validationMessage = "password must have a value"
            self.uicontroller.create_popup(validationMessage)
        elif not isinstance(password, str):
            validationMessage = "password must be correct type"
            create_popup(validationMessage)
        elif not (6 < len(password) <= 30):
            validationMessage = "password is not between 6 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        if validationMessage == "":
            self.employeeController.create_employee(employeeId, username, password, isManager)
            validationMessage = "Successfully created employee"
            self.logController.create_log(str(uuid.uuid4()), "Successfully created employee with employeeId=" + employeeId, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
            self.uicontroller.create_popup(validationMessage)
        else:
            self.logController.create_log(str(uuid.uuid4()), "Unsuccessfully created employee as " + validationMessage, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
    def validateDeleteEmployee(self, employeeId):
        validationMessage = ""
        found = False

        employeeObjects = self.employeeController.get_employee_objects()

        for employee in employeeObjects:
            if employee.get_employeeId() == employeeId:
                found = True

        if not found:
            validationMessage = "Employee not found with employeeId"
            self.uicontroller.create_popup(validationMessage)
            self.logController.create_log(str(uuid.uuid4()), "Unsuccessfully deleted employee as Employee not found with employeeId", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))

        if validationMessage == "":
            complete = self.employeeController.delete_employee(employeeId)
            if complete:
                validationMessage = "Successfully deleted employee"
                self.logController.create_log(str(uuid.uuid4()), "Successfully deleted employee", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
            else:
                validationMessage = "Error occurred while deleting employee"
                self.logController.create_log(str(uuid.uuid4()), "Unsuccessfully deleted employee as error occurred", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
            self.uicontroller.create_popup(validationMessage)
    def validateEditEmployee(self, oldemployeeId, newemployeeId, newusername, newpassword, newisManager):
        validationMessage = ""
        found = False
        doHashPassword = True

        employeeObjects = get_employee_objects()

        for employee in employeeObjects:
            if employee.get_employeeId() == oldemployeeId:
                found = True
                oldusername, oldpassword, oldisManager = employee.get_username(), employee.get_password(), employee.get_isManager()

        if not found:
            validationMessage = "Employee not found with oldemployeeId"
            self.uicontroller.create_popup(validationMessage)

        for employee in employeeObjects:
            if employee.get_employeeId() == newemployeeId:
                validationMessage = "newemployeeId already exists"
                self.uicontroller.create_popup(validationMessage)

        if newemployeeId is None or newemployeeId == "":
            newemployeeId = oldemployeeId
        elif not isinstance(newemployeeId, str):
            validationMessage = "newemployeeId must be correct type"
            self.uicontroller.create_popup(validationMessage)

        if newusername is None or newusername == "":
            newusername = oldusername
        elif not isinstance(newusername, str):
            validationMessage = "newusername must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif not (0 < len(newusername) <= 30):
            validationMessage = "newusername is not between 0 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        if newpassword is None or newpassword == "":
            newpassword = oldpassword
            doHashPassword = False
        elif not isinstance(newpassword, str):
            validationMessage = "newpassworde must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif not (6 < len(newpassword) <= 30):
            validationMessage = "newpassword is not between 6 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        if newisManager is None or newisManager == "":
            newisManager = oldisManager

        if validationMessage == "":
            complete = self.employeeController.edit_employee(oldemployeeId, newemployeeId, newusername, newpassword, newisManager, doHashPassword)

            if complete:
                validationMessage = "Successfully edited employee"
            else:
                validationMessage = "Error occurred while editing employee"
            self.logController.create_log(str(uuid.uuid4()), "Successfully edited employee with employeeId=" + oldemployeeId, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        else:
            self.logController.create_log(str(uuid.uuid4()), "Unsuccessfully edited employee as " + validationMessage, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        self.uicontroller.create_popup(validationMessage)
    def validateAddComponent(self, componentId, componentName, quantity, minQuantity, status):
        validationMessage = "" 
        componentObjects = self.componentController.get_component_objects() 
        for component in componentObjects: 
            if component.get_componentId() == componentId: 
                validationMessage = "componentId already exists" 
                create_popup(validationMessage) 
        if componentId is None or componentId == "": 
            validationMessage = "componentId must have a value" 
            self.uicontroller.create_popup(validationMessage) 
        elif not isinstance(componentId, str): 
            validationMessage = "componentId must be correct type" 
            self.uicontroller.create_popup(validationMessage) 

        if componentName is None or componentName == "": 
            validationMessage = "componentName must have a value" 
            self.uicontroller.create_popup(validationMessage) 
        elif not isinstance(componentName, str): 
            validationMessage = "componentName must be correct type" 
            self.uicontroller.create_popup(validationMessage) 
        elif not (0 < len(componentName) <= 30): 
            validationMessage = "componentName is not between 0 and 30 characters" 
            self.uicontroller.create_popup(validationMessage) 

        if quantity.isnumeric():
            quantity = int(quantity)
        if not isinstance(quantity, int): 
            validationMessage = "quantity must be correct type" 
            self.uicontroller.create_popup(validationMessage) 
        elif quantity < 0: 
            validationMessage = "quantity cannot be negative" 
            self.uicontroller.create_popup(validationMessage) 

        if minQuantity.isnumeric():
            minQuantity = int(minQuantity)
        if not isinstance(minQuantity, int): 
            validationMessage = "minQuantity must be correct type" 
            self.uicontroller.create_popup(validationMessage) 
        elif minQuantity < 0: 
            validationMessage = "minQuantity cannot be negative" 
            self.uicontroller.create_popup(validationMessage)

        if quantity == 0:
            status = "outOfStock"
        elif status == "outOfStock":
            status = "available"

        if validationMessage == "": 
            self.componentController.create_component(componentId, componentName, quantity, minQuantity, status) 
            validationMessage = "Successfully created component" 
            self.uicontroller.create_popup(validationMessage)
            self.logController.create_log(str(uuid.uuid4()), "Successfully created component with componentId=" + componentId, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        else:
            self.logController.create_log(str(uuid.uuid4()), "Unsuccessfully created component as " + validationMessage, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
    def validateDeleteComponent(self, componentId):
        validationMessage = "" 
        found = False 
        componentObjects = self.componentController.get_component_objects() 
        for component in componentObjects: 
            if component.get_componentId() == componentId: 
                found = True 
        if not found: 
            validationMessage = "Component not found with componentId" 
            self.uicontroller.create_popup(validationMessage) 
        if validationMessage == "": 
            complete = self.componentController.delete_component(componentId) 
            if complete: 
                validationMessage = "Successfully deleted component" 
            else: 
                validationMessage = "Error occurred while deleting component" 
            self.logController.create_log(str(uuid.uuid4()), "Successfully deleted component", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        else:
            self.logController.create_log(str(uuid.uuid4()), "Unsuccessfully deleted component as " + validationMessage, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        self.uicontroller.create_popup(validationMessage)
    def validateEditComponent(self, oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus):
        validationMessage = ""
        found = False

        componentObjects = get_component_objects()

        for component in componentObjects:
            if component.get_componentId() == oldcomponentId:
                found = True
                oldcomponentName, oldquantity, oldminQuantity, oldstatus = component.get_componentName(), component.get_quantity(), component.get_minQuantity(), component.get_status()

        if not found:
            validationMessage = "Component not found with oldcomponentId"
            self.uicontroller.create_popup(validationMessage)

        for component in componentObjects:
            if component.get_componentId() == newcomponentId:
                validationMessage = "newcomponentId already exists"
                self.uicontroller.create_popup(validationMessage)

        if newcomponentId is None or newcomponentId == "":
            newcomponentId = oldcomponentId
        elif not isinstance(newcomponentId, str):
            validationMessage = "newcomponentId must be correct type"
            self.uicontroller.create_popup(validationMessage)

        if newcomponentName is None or newcomponentName == "":
            newcomponentName = oldcomponentName
        elif not isinstance(newcomponentName, str):
            validationMessage = "newcomponentName must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif not (0 < len(newcomponentName) <= 30):
            validationMessage = "newcomponentName is not between 0 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        if newquantity is None or newquantity == "":
            newquantity = oldquantity
        elif newquantity.isnumeric():
            newquantity = int(newquantity)
        elif not isinstance(newquantity, int):
            validationMessage = "newquantity must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif newquantity < 0:
            validationMessage = "quantity cannot be negative"
            self.uicontroller.create_popup(validationMessage)

        if newminQuantity is None or newminQuantity == "":
            newminQuantity = oldminQuantity
        elif newminQuantity.isnumeric():
            newminQuantity = int(newminQuantity)
        elif not isinstance(newminQuantity, int):
            validationMessage = "newminQuantity must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif newminQuantity < 0:
            validationMessage = "newminQuantity cannot be negative"
            self.uicontroller.create_popup(validationMessage)

        if newstatus is None or newstatus == "":
            newstatus = oldstatus

        if validationMessage == "":
            complete = self.componentController.edit_component(oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus)

            if complete:
                validationMessage = "Successfully edited component"
            else:
                validationMessage = "Error occurred while editing component"
            self.logController.create_log(str(uuid.uuid4()), "Successfully edited component with componentId=" + oldcomponentId, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        else:
            self.logController.create_log(str(uuid.uuid4()), "Unsuccessfully edited employee as " + validationMessage, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
            self.uicontroller.create_popup(validationMessage)

