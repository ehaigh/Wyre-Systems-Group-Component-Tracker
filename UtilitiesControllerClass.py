import uuid
import datetime
import os
import csv

class UtilitiesController:
    def __init__(self, employeeController, componentController, logController, backupController):
        #Establishes controllers to use
        self.employeeController = employeeController
        self.componentController = componentController
        self.logController = logController
        self.backupController = backupController
    def initialiseSystem(self, dbReader):
        #If has access to databasereader, load all objects.
        if dbReader:
            dbReader.load_all()
    def setUIController(self, uicontroller):
        #Sets access to User Interface controller
        self.uicontroller = uicontroller
    def manageBackup(self):
        #Execute backup
        self.backupController.create_backup()
        #Creates popup about successfully backup
        self.uicontroller.create_popup("Successfully created backup")
        #Creates log entry about successful backup
        self.logController.create_log(str(uuid.uuid4()), "Successfully created backup", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
    def manageExport(self):
        #Check Exports folder exists, if not, make it.
        exports_folder = os.path.join(os.getcwd(), "Exports")
        if not os.path.exists(exports_folder):
            os.makedirs(exports_folder)
        #Set filepath using current date and time
        filepath = os.path.join(exports_folder, "export_" + str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".csv")
        try:
            #Opens new exports file in write mode
            with open(filepath, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                #Creates title and columns for component entries
                writer.writerow(["Components:"])
                writer.writerow(["Component ID", "Name", "Quantity", "Minimum Quantity", "Status"])
                #Writes each component entry into file
                for row in self.getComponentData():
                    writer.writerow(row)
                #Empty line between components and logs
                writer.writerow([])
                #Creates title and columns for log entries
                writer.writerow(["Logs:"])
                writer.writerow(["Log ID", "Action", "Date", "Time"])
                #Writes each log entry into file
                for row in self.getLogData():
                    writer.writerow(row)
            #Create popup and log about successful export
            self.uicontroller.create_popup("Successfully exported data\nFile saved at:" + filepath)
            self.logController.create_log(str(uuid.uuid4()), "Successfully exported data", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        #If export failed,
        except Exception as e:
            #Create popup and log about unsuccessful export
            self.uicontroller.create_popup("Failed to export data with error:" + str(e))
            self.logController.create_log(str(uuid.uuid4()), "Failed to export data", datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
    def getComponentData(self):
        #Retrieve component objects
        componentObjects = self.componentController.get_component_objects()
        #Create empty data array
        data = []
        #Add each object to array
        for component in componentObjects:
            row = [component.get_componentId(),component.get_componentName(),component.get_quantity(),component.get_minQuantity(),component.get_status()]
            data.append(row)
        #Return array
        return data
    def getEmployeeData(self):
        #Retrieve employee objects
        employeeObjects = self.employeeController.get_employee_objects()
        #Create empty data array
        data = []
        #Add each object to array
        for emp in employeeObjects:
            data.append([emp.get_employeeId(),emp.get_username(),emp.get_password(),"Yes" if emp.get_isManager() else "No"])
        #Return array
        return data
    def getLogData(self):
        #Retrieve log objects
        logObjects = self.logController.get_log_objects()
        #Create empty data array
        data = []
        #Add each object to array
        for log in logObjects:
            row = [log.get_logId(),log.get_action(),log.get_date(),log.get_time()]
            data.append(row)
        #Return array
        return data
    def getAlertData(self):
        #Retrieve component objects
        componentObjects = self.componentController.get_component_objects()
        #Create empty data array
        data = []
        for component in componentObjects:
            #If component is out of stock, add it to array.
            if component.get_status() == "outOfStock":
                data.append(["Component with componentId=" + component.get_componentId() + " is out of stock"])
            #If component is faulty, add it to array.
            if component.get_status() == "faulty":
                data.append(["Component with componentId=" + component.get_componentId() + " is faulty"])
            #If component's quantity is below minimum quantity, add it to array.
            if component.get_quantity() < component.get_minQuantity():
                data.append(["Component with componentId=" + component.get_componentId() + " has quantity below minimum quantity"])
        #Return array
        return data
    def validateLogin(self, username, password):
        #Validate login credentials
        valid, isManager = self.employeeController.validate_credentials(username, password)
        if valid:
            #Create log for successful login
            self.logController.create_log(str(uuid.uuid4()),("Successful login by username=" + username),datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))
        else:
            #Create log for unsuccessful login
            self.logController.create_log(
                str(uuid.uuid4()),
                "Unsuccessful login",
                datetime.datetime.now().strftime("%d/%m/%Y"),
                datetime.datetime.now().strftime("%X")
            )
        #Return login result and manager status
        return valid, isManager

    def validateAddEmployee(self, employeeId, username, password, isManager):
        #Initialise validation message
        validationMessage = ""
        #Retrieve employee objects
        employeeObjects = self.employeeController.get_employee_objects()

        #Check if employeeId already exists
        for employee in employeeObjects:
            if employee.get_employeeId() == employeeId:
                validationMessage = "employeeId already exists"
                self.uicontroller.create_popup(validationMessage)

        #Validate employeeId
        if employeeId is None or employeeId == "":
            validationMessage = "employeeId must have a value"
            self.uicontroller.create_popup(validationMessage)
        elif not isinstance(employeeId, str):
            validationMessage = "employeeId must be correct type"
            self.uicontroller.create_popup(validationMessage)

        #Validate username
        if username is None or username == "":
            validationMessage = "username must have a value"
            self.uicontroller.create_popup(validationMessage)
        elif not isinstance(username, str):
            validationMessage = "username must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif not (0 < len(username) <= 30):
            validationMessage = "username is not between 0 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        #Validate password
        if password is None or password == "":
            validationMessage = "password must have a value"
            self.uicontroller.create_popup(validationMessage)
        elif not isinstance(password, str):
            validationMessage = "password must be correct type"
            create_popup(validationMessage)
        elif not (6 < len(password) <= 30):
            validationMessage = "password is not between 6 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        #If no validation errors, create employee
        if validationMessage == "":
            self.employeeController.create_employee(employeeId, username, password, isManager)
            validationMessage = "Successfully created employee"
            #Create log for successful employee creation
            self.logController.create_log(str(uuid.uuid4()),"Successfully created employee with employeeId=" + employeeId,datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))
            self.uicontroller.create_popup(validationMessage)
        else:
            #Create log for unsuccessful employee creation
            self.logController.create_log(str(uuid.uuid4()),"Unsuccessfully created employee as " + validationMessage,datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))

    def validateDeleteEmployee(self, employeeId):
        #Initialise validation message and found flag
        validationMessage = ""
        found = False

        #Retrieve employee objects
        employeeObjects = self.employeeController.get_employee_objects()

        #Check if employee exists
        for employee in employeeObjects:
            if employee.get_employeeId() == employeeId:
                found = True

        #If employee not found
        if not found:
            validationMessage = "Employee not found with employeeId"
            self.uicontroller.create_popup(validationMessage)
            self.logController.create_log(str(uuid.uuid4()),"Unsuccessfully deleted employee as Employee not found with employeeId",datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))

        #If employee found, delete employee
        if validationMessage == "":
            complete = self.employeeController.delete_employee(employeeId)
            if complete:
                validationMessage = "Successfully deleted employee"
                self.logController.create_log(str(uuid.uuid4()),"Successfully deleted employee",datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))
            else:
                validationMessage = "Error occurred while deleting employee"
                self.logController.create_log(str(uuid.uuid4()),"Unsuccessfully deleted employee as error occurred",datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))
            self.uicontroller.create_popup(validationMessage)

    def validateEditEmployee(self, oldemployeeId, newemployeeId, newusername, newpassword, newisManager):
        #Initialise validation message and flags
        validationMessage = ""
        found = False
        doHashPassword = True

        #Retrieve employee objects
        employeeObjects = self.employeeController.get_employee_objects()

        #Find employee to edit
        for employee in employeeObjects:
            if employee.get_employeeId() == oldemployeeId:
                found = True
                oldusername, oldpassword, oldisManager = (employee.get_username(),employee.get_password(),employee.get_isManager())

        #If employee not found
        if not found:
            validationMessage = "Employee not found with oldemployeeId"
            self.uicontroller.create_popup(validationMessage)

        #Check if new employeeId already exists
        for employee in employeeObjects:
            if employee.get_employeeId() == newemployeeId:
                validationMessage = "newemployeeId already exists"
                self.uicontroller.create_popup(validationMessage)

        #Validate new employeeId
        if newemployeeId is None or newemployeeId == "":
            newemployeeId = oldemployeeId
        elif not isinstance(newemployeeId, str):
            validationMessage = "newemployeeId must be correct type"
            self.uicontroller.create_popup(validationMessage)

        #Validate new username
        if newusername is None or newusername == "":
            newusername = oldusername
        elif not isinstance(newusername, str):
            validationMessage = "newusername must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif not (0 < len(newusername) <= 30):
            validationMessage = "newusername is not between 0 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        #Validate new password
        if newpassword is None or newpassword == "":
            newpassword = oldpassword
            doHashPassword = False
        elif not isinstance(newpassword, str):
            validationMessage = "newpassworde must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif not (6 < len(newpassword) <= 30):
            validationMessage = "newpassword is not between 6 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        #Validate new isManager value
        if newisManager is None or newisManager == "":
            newisManager = oldisManager

        #If no validation errors, edit employee
        if validationMessage == "":
            complete = self.employeeController.edit_employee(oldemployeeId, newemployeeId, newusername, newisManager, doHashPassword)

            if complete:
                validationMessage = "Successfully edited employee"
            else:
                validationMessage = "Error occurred while editing employee"

            self.logController.create_log(str(uuid.uuid4()), "Successfully edited employee with employeeId=" + oldemployeeId, datetime.datetime.now().strftime("%d/%m/%Y"), datetime.datetime.now().strftime("%X"))
        else:
            #Create log for unsuccessful edit
            self.logController.create_log(str(uuid.uuid4()),"Unsuccessfully edited employee as " + validationMessage,datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))

        self.uicontroller.create_popup(validationMessage)
    def validateAddComponent(self, componentId, componentName, quantity, minQuantity, status):
        #Initialise validation message
        validationMessage = "" 
        #Retrieve component objects
        componentObjects = self.componentController.get_component_objects() 

        #Check if componentId already exists
        for component in componentObjects: 
            if component.get_componentId() == componentId: 
                validationMessage = "componentId already exists" 
                self.uicontroller.create_popup(validationMessage) 

        #Validate componentId
        if componentId is None or componentId == "": 
            validationMessage = "componentId must have a value" 
            self.uicontroller.create_popup(validationMessage) 
        elif not isinstance(componentId, str): 
            validationMessage = "componentId must be correct type" 
            self.uicontroller.create_popup(validationMessage) 

        #Validate component name
        if componentName is None or componentName == "": 
            validationMessage = "componentName must have a value" 
            self.uicontroller.create_popup(validationMessage) 
        elif not isinstance(componentName, str): 
            validationMessage = "componentName must be correct type" 
            self.uicontroller.create_popup(validationMessage) 
        elif not (0 < len(componentName) <= 30): 
            validationMessage = "componentName is not between 0 and 30 characters" 
            self.uicontroller.create_popup(validationMessage) 

        #Validate quantity
        if quantity.isnumeric():
            quantity = int(quantity)
        if not isinstance(quantity, int): 
            validationMessage = "quantity must be correct type" 
            self.uicontroller.create_popup(validationMessage) 
        elif quantity < 0: 
            validationMessage = "quantity cannot be negative" 
            self.uicontroller.create_popup(validationMessage) 

        #Validate minimum quantity
        if minQuantity.isnumeric():
            minQuantity = int(minQuantity)
        if not isinstance(minQuantity, int): 
            validationMessage = "minQuantity must be correct type" 
            self.uicontroller.create_popup(validationMessage) 
        elif minQuantity < 0: 
            validationMessage = "minQuantity cannot be negative" 
            self.uicontroller.create_popup(validationMessage)

        #Automatically update status based on quantity
        if quantity == 0:
            status = "outOfStock"
        elif status == "outOfStock":
            status = "available"

        #If validation passed, create component
        if validationMessage == "": 
            self.componentController.create_component(componentId, componentName, quantity, minQuantity, status) 
            validationMessage = "Successfully created component" 
            self.uicontroller.create_popup(validationMessage)
            self.logController.create_log(str(uuid.uuid4()),"Successfully created component with componentId=" + componentId,datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))
        else:
            #Create log for unsuccessful creation
            self.logController.create_log(str(uuid.uuid4()),"Unsuccessfully created component as " + validationMessage,datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))

    def validateDeleteComponent(self, componentId):
        #Initialise validation message and found flag
        validationMessage = "" 
        found = False 

        #Retrieve component objects
        componentObjects = self.componentController.get_component_objects() 

        #Check if component exists
        for component in componentObjects: 
            if component.get_componentId() == componentId: 
                found = True 

        #If component not found
        if not found: 
            validationMessage = "Component not found with componentId" 
            self.uicontroller.create_popup(validationMessage) 

        #If found, delete component
        if validationMessage == "": 
            complete = self.componentController.delete_component(componentId) 
            if complete: 
                validationMessage = "Successfully deleted component" 
            else: 
                validationMessage = "Error occurred while deleting component" 
            self.logController.create_log(str(uuid.uuid4()),"Successfully deleted component",datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))
        else:
            #Create log for unsuccessful deletion
            self.logController.create_log(str(uuid.uuid4()),"Unsuccessfully deleted component as " + validationMessage,datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))
        self.uicontroller.create_popup(validationMessage)

    def validateEditComponent(self, oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus):
        #Initialise validation message and found flag
        validationMessage = ""
        found = False

        #Retrieve component objects
        componentObjects = self.componentController.get_component_objects()

        #Find component to edit
        for component in componentObjects:
            if component.get_componentId() == oldcomponentId:
                found = True
                oldcomponentName, oldquantity, oldminQuantity, oldstatus = (component.get_componentName(),component.get_quantity(),component.get_minQuantity(),component.get_status())

        #If component not found
        if not found:
            validationMessage = "Component not found with oldcomponentId"
            self.uicontroller.create_popup(validationMessage)

        #Check if new componentId already exists
        for component in componentObjects:
            if component.get_componentId() == newcomponentId:
                validationMessage = "newcomponentId already exists"
                self.uicontroller.create_popup(validationMessage)

        #Validate new componentId
        if newcomponentId is None or newcomponentId == "":
            newcomponentId = oldcomponentId
        elif not isinstance(newcomponentId, str):
            validationMessage = "newcomponentId must be correct type"
            self.uicontroller.create_popup(validationMessage)

        #Validate new component name
        if newcomponentName is None or newcomponentName == "":
            newcomponentName = oldcomponentName
        elif not isinstance(newcomponentName, str):
            validationMessage = "newcomponentName must be correct type"
            self.uicontroller.create_popup(validationMessage)
        elif not (0 < len(newcomponentName) <= 30):
            validationMessage = "newcomponentName is not between 0 and 30 characters"
            self.uicontroller.create_popup(validationMessage)

        #Validate new quantity
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

        #Validate new minimum quantity
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

        #Validate new status
        if newstatus is None or newstatus == "":
            newstatus = oldstatus

        #If validation passed, edit component
        if validationMessage == "":
            complete = self.componentController.edit_component(oldcomponentId,newcomponentId,newcomponentName,newquantity,newminQuantity,newstatus)
            if complete: 
                validationMessage = "Successfully edited component"
            else:
                validationMessage = "Error occurred while editing component"

            self.logController.create_log(str(uuid.uuid4()),"Successfully edited component with componentId=" + oldcomponentId,datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))
        else:
            #Create log for unsuccessful edit
            self.logController.create_log(str(uuid.uuid4()),"Unsuccessfully edited employee as " + validationMessage,datetime.datetime.now().strftime("%d/%m/%Y"),datetime.datetime.now().strftime("%X"))

        self.uicontroller.create_popup(validationMessage)
