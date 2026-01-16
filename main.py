import tkinter as tk
from EmployeeControllerClass import EmployeeController
from ComponentControllerClass import ComponentController
from LogControllerClass import LogController
from UtilitiesControllerClass import UtilitiesController
from DatabaseReaderClass import DatabaseReader
from UIControllerClass import UIController
from BackupControllerClass import BackupController

employeeController = EmployeeController()
componentController = ComponentController()
logController = LogController()
backupController = BackupController()

utils = UtilitiesController(
    employeeController=employeeController,
    componentController=componentController,
    logController=logController,
    backupController=backupController
)

dbReader = DatabaseReader(
    employeeController=employeeController,
    componentController=componentController,
    logController=logController
)
utils.initialiseSystem(dbReader)

root = tk.Tk()
ui = UIController(root, utils)
utils.setUIController(ui)
ui.initialiseUI() 

root.mainloop()