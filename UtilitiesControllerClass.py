import tkinter as tk
from EmployeeControllerClass import validate_credentials, get_employee_objects, create_employee, edit_employee, delete_employee
from ComponentControllerClass import get_component_objects, create_component, edit_component, delete_component
from UIControllerClass import create_popup

class UtilitiesController:
    def __init__(self):
        pass
    def initialiseSystem(self):
        root = tk.Tk
    def validateLogin(self, username, password):
        return validate_credentials(username, password)
    def validateAddComponent(self, componentId, componentName, quantity, minQuantity, status):
        validationMessage = ""
        componentObjects = get_component_objects()
        for component in componentObjects:
            if component.get_componentId() == componentId:
                validationMessage = "componentId already exists"
                create_popup(validationMessage)
                return
        
        if componentId is None or componentId == "":
            validationMessage = "componentId must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(componentId, str):
            validationMessage = "componentId must be correct type"
            create_popup(validationMessage)
            return

        if componentName is None or componentName == "":
            validationMessage = "componentName must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(componentName, str):
            validationMessage = "componentName must be correct type"
            create_popup(validationMessage)
            return
        elif not (0 < len(componentName) <= 30):
            validationMessage = "componentName is not between 0 and 30 characters"
            create_popup(validationMessage)
            return

        if not isinstance(quantity, int):
            validationMessage = "quantity must be correct type"
            create_popup(validationMessage)
            return 
        elif quantity < 0: 
            validationMessage = "quantity cannot be negative"
            create_popup(validationMessage)
            return    

        if not isinstance(minQuantity, int):
            validationMessage = "minQuantity must be correct type"
            create_popup(validationMessage)
            return 
        elif minQuantity < 0: 
            validationMessage = "minQuantity cannot be negative"
            create_popup(validationMessage)
            return 

        if validationMessage == "":
            create_component(componentId, componentName, quantity, minQuantity, status)
            validationMessage = "Successfully created component"
            create_popup(validationMessage)

    def validateDeleteComponent(self, componentId):
        validationMessage = ""
        found = False
        componentObjects = get_component_objects()
        for component in componentObjects:
            if component.get_componentId() == componentId:
                found = True
        if not found:
            validationMessage = "Component not found with componentId"
            create_popup(validationMessage)
            return

        if validationMessage == "":
            complete = delete_component(componentId)
            if complete:
                validationMessage = "Successfully deleted component"
            else:
                validationMessage = "Error occurred while deleting component"
            create_popup(validationMessage)

    def validateEditComponent(self, oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus):
        validationMessage = ""
        found = False
        componentObjects = get_component_objects()
        for component in componentObjects:
            if component.get_componentId() == oldcomponentId:
                found = True
        if not found:
            validationMessage = "Component not found with oldcomponentId"
            create_popup(validationMessage)
            return

        for component in componentObjects:
            if component.get_componentId() == newcomponentId:
                validationMessage = "newcomponentId already exists"
                create_popup(validationMessage)
                return
        if newcomponentId is None or newcomponentId == "":
            validationMessage = "newcomponentId must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(newcomponentId, str):
            validationMessage = "newcomponentId must be correct type"
            create_popup(validationMessage)
            return

        if newcomponentName is None or newcomponentName == "":
            validationMessage = "newcomponentName must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(newcomponentName, str):
            validationMessage = "newcomponentName must be correct type"
            create_popup(validationMessage)
            return
        elif not (0 < len(newcomponentName) <= 30):
            validationMessage = "newcomponentName is not between 0 and 30 characters"
            create_popup(validationMessage)
            return

        if not isinstance(newquantity, int):
            validationMessage = "newquantity must be correct type"
            create_popup(validationMessage)
            return 
        elif quantity < 0: 
            validationMessage = "quantity cannot be negative"
            create_popup(validationMessage)
            return    

        if not isinstance(newminQuantity, int):
            validationMessage = "newminQuantity must be correct type"
            create_popup(validationMessage)
            return 
        elif newminQuantity < 0: 
            validationMessage = "newminQuantity cannot be negative"
            create_popup(validationMessage)
            return 

        if validationMessage == "":
            complete = edit_component(oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus)
            if complete:
                validationMessage = "Successfully edited component"
            else:
                validationMessage = "Error occurred while editing component"
            create_popup(validationMessage)

    def validateAddEmployee(self, employeeId, username, password, isManager):
        validationMessage = ""
        employeeObjects = get_employee_objects()
        for employee in employeeObjects:
            if employee.get_employeeId() == employeeId:
                validationMessage = "employeeId already exists"
                create_popup(validationMessage)
                return
        if employeeId is None or employeeId == "":
            validationMessage = "employeeId must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(employeeId, str):
            validationMessage = "employeeId must be correct type"
            create_popup(validationMessage)
            return

        if username is None or username == "":
            validationMessage = "username must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(username, str):
            validationMessage = "username must be correct type"
            create_popup(validationMessage)
            return
        elif not (0 < len(username) <= 30):
            validationMessage = "username is not between 0 and 30 characters"
            create_popup(validationMessage)
            return

        if password is None or password == "":
            validationMessage = "password must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(password, str):
            validationMessage = "passworde must be correct type"
            create_popup(validationMessage)
            return
        elif not (6 < len(password) <= 30):
            validationMessage = "password is not between 6 and 30 characters"
            create_popup(validationMessage)
            return    

        if validationMessage == "":
            create_employee(employeeId, username, password, isManager)
            validationMessage = "Successfully created employee"
            create_popup(validationMessage)

    def validateDeleteEmployee(self, employeeId):
        validationMessage = ""
        found = False
        employeeObjects = get_employee_objects()
        for employee in employeeObjects:
            if employee.get_employeeId() == employeeId:
                found = True
        if not found:
            validationMessage = "Employee not found with employeeId"
            create_popup(validationMessage)
            return

        if validationMessage == "":
            complete = delete_employee(employeeId)
            if complete:
                validationMessage = "Successfully deleted employee"
            else:
                validationMessage = "Error occurred while deleting employee"
            create_popup(validationMessage)

    def validateEditEmployee(self, oldemployeeId, newemployeeId, newusername, newpassword, newisManager):
        validationMessage = ""
        found = False
        employeeObjects = get_employee_objects()
        for employee in employeeObjects:
            if employee.get_employeeId() == oldemployeeId:
                found = True
        if not found:
            validationMessage = "Employee not found with oldemployeeId"
            create_popup(validationMessage)
            return

        for employee in employeeObjects:
            if employee.get_employeeId() == newemployeeId:
                validationMessage = "newemployeeId already exists"
                create_popup(validationMessage)
                return
        if newemployeeId is None or newemployeeId == "":
            validationMessage = "newemployeeId must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(newemployeeId, str):
            validationMessage = "newemployeeId must be correct type"
            create_popup(validationMessage)
            return

        if newusername is None or newusername == "":
            validationMessage = "newusername must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(newusername, str):
            validationMessage = "newusername must be correct type"
            create_popup(validationMessage)
            return
        elif not (0 < len(newusername) <= 30):
            validationMessage = "newusername is not between 0 and 30 characters"
            create_popup(validationMessage)
            return

        if newpassword is None or newpassword == "":
            validationMessage = "newpassword must have a value"
            create_popup(validationMessage)
            return
        elif not isinstance(newpassword, str):
            validationMessage = "newpassworde must be correct type"
            create_popup(validationMessage)
            return
        elif not (6 < len(newpassword) <= 30):
            validationMessage = "newpassword is not between 6 and 30 characters"
            create_popup(validationMessage)
            return

        if validationMessage == "":
            complete = edit_employee(oldemployeeId, newemployeeId, newusername, newpassword, newisManager)
            if complete:
                validationMessage = "Successfully edited employee"
            else:
                validationMessage = "Error occurred while editing employee"
            create_popup(validationMessage)