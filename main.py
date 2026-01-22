import tkinter as tk
from EmployeeControllerClass import EmployeeController
from ComponentControllerClass import ComponentController
from LogControllerClass import LogController
from UtilitiesControllerClass import UtilitiesController
from DatabaseReaderClass import DatabaseReader
from UIControllerClass import UIController
from BackupControllerClass import BackupController

#Create controller objects
employeeController = EmployeeController()
componentController = ComponentController()
logController = LogController()
backupController = BackupController()

#Create utility controller
utils = UtilitiesController(
    employeeController=employeeController,
    componentController=componentController,
    logController=logController,
    backupController=backupController
)
#Create database reader
dbReader = DatabaseReader(
    employeeController=employeeController,
    componentController=componentController,
    logController=logController
)
#Initialise the system
utils.initialiseSystem(dbReader)

#Create the UI window
root = tk.Tk()
#Initialise the UI
ui = UIController(root, utils)
utils.setUIController(ui)
ui.initialiseUI() 

#necessary for UI to execute
root.mainloop()
