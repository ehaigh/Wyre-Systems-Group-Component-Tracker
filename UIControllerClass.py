import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class UIController:
    def __init__(self, root, utils):
        #Store root window
        self.root = root
        #Store utils controller
        self.utils = utils
        #Lock UI until login
        self.locked = True

    def initialiseUI(self):
        #Create menu bar
        self.menubar = tk.Menu(self.root)

        #Create all UI pages
        self.create_login_page()
        self.create_component_menu()
        self.create_log_menu()
        self.create_alert_menu()

        #Create component menu
        componentmenu = tk.Menu(self.menubar, tearoff=0)
        componentmenu.add_command(label="View components", command=self.refresh_view_components)
        componentmenu.add_command(label="Add component", command=self.addcomponentpage.tkraise)
        componentmenu.add_command(label="Delete component", command=self.deletecomponentpage.tkraise)
        componentmenu.add_command(label="Edit component", command=self.editcomponentpage.tkraise)

        #Create log menu
        logmenu = tk.Menu(self.menubar, tearoff=0)
        logmenu.add_command(label="View logs", command=self.refresh_view_logs)

        #Create alert menu
        alertmenu = tk.Menu(self.menubar, tearoff=0)
        alertmenu.add_command(label="View alerts", command=self.refresh_view_alerts)

        #Create backup menu
        backupmenu = tk.Menu(self.menubar, tearoff=0)
        backupmenu.add_command(label="Create backup", command=self.utils.manageBackup)

        #Create export menu
        exportmenu = tk.Menu(self.menubar, tearoff=0)
        exportmenu.add_command(label="Export data", command=self.utils.manageExport)

        #Add menus to menu bar
        self.menubar.add_cascade(menu=componentmenu, label="Component Management")
        self.menubar.add_cascade(menu=logmenu, label="Log management")
        self.menubar.add_cascade(menu=alertmenu, label="Alert management")
        self.menubar.add_cascade(menu=backupmenu, label="Backup management")
        self.menubar.add_cascade(menu=exportmenu, label="Export management")

        #Configure root grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        #Show login page
        self.loginpage.tkraise()

        #Set window size
        self.root.geometry("1280x800")
        #Set window title
        self.root.title("Inventory Management System")

    def create_login_page(self):

        #login page
        
        #Create login page frame
        self.loginpage = Frame(self.root)
        self.loginpage.grid(row=0,column=0, sticky="nsew")
        
        #Center content
        centerframe = Frame(self.loginpage)
        centerframe.pack(side='top', fill='x', pady=60)

        #Login title
        titlelabel = Label(centerframe,text="Login", font=('Arial', 20))
        titlelabel.pack(pady=30)

        #Username label
        usernamelabel = Label(centerframe,text="Enter username", font=('Arial', 20))
        usernamelabel.pack(pady=20)

        #Username input
        usernametextbox = tk.Entry(centerframe, font=('Arial', 16))
        usernametextbox.pack()

        #Password label
        passwordlabel = Label(centerframe,text="Enter password", font=('Arial', 20))
        passwordlabel.pack(pady=20)

        #Password input
        passwordtextbox = tk.Entry(centerframe, font=('Arial', 16))
        passwordtextbox.pack()

        #Confirm login button
        button = tk.Button(centerframe, text="Confirm", font=('Arial', 16), command=lambda: self.handle_login(usernametextbox.get(), passwordtextbox.get()))
        button.pack(pady=20)

    def create_component_menu(self):

        #Create component pages
        self.viewcomponentspage = Frame(self.root)
        self.addcomponentpage = Frame(self.root)
        self.deletecomponentpage = Frame(self.root)
        self.editcomponentpage = Frame(self.root)

        #Grid component pages
        self.viewcomponentspage.grid(row=0,column=0, sticky="nsew")
        self.addcomponentpage.grid(row=0,column=0, sticky="nsew")
        self.deletecomponentpage.grid(row=0,column=0, sticky="nsew")
        self.editcomponentpage.grid(row=0,column=0, sticky="nsew")

        #view components page

        #Create view components page
        self.viewcomponentspage = Frame(self.root)
        self.viewcomponentspage.grid(row=0, column=0, sticky="nsew")

        #Center content
        centerframe = Frame(self.viewcomponentspage)
        centerframe.pack(side='top', fill='both', expand=True, pady=30)

        #Page title
        titlelabel = Label(centerframe, text="View Components", font=('Arial', 20))
        titlelabel.pack(pady=20)

        #Table columns
        columns = ("Component ID", "Name", "Quantity", "Min Quantity", "Status")

        #Create table
        tree = ttk.Treeview(centerframe, columns=columns, show="headings", height=15)

        #Configure table columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        #Insert component data
        for row in self.utils.getComponentData():
            tree.insert("", "end", values=row)

        #Pack table
        tree.pack(fill="both", expand=True, padx=20, pady=20)

        #Add scrollbar
        scrollbar = ttk.Scrollbar(centerframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        #Store component tree
        self.componentTree = tree

        #create add page
        
        #Center add component page
        centerframe = Frame(self.addcomponentpage)
        centerframe.pack(side='top', fill='x', pady=60)

        #Add page title
        addtitlelabel = Label(centerframe,text="Add component", font=('Arial', 20))
        addtitlelabel.pack(pady=30)

        #Component Id label
        addcomponentIdlabel = Label(centerframe,text="Enter component Id", font=('Arial', 20))
        addcomponentIdlabel.pack(pady=10)

        #Component Id input
        addcomponentIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        addcomponentIdtextbox.pack()

        #Component name label
        addcomponentNamelabel = Label(centerframe,text="Enter component name", font=('Arial', 20))
        addcomponentNamelabel.pack(pady=10)

        #Component name input
        addcomponentNametextbox = tk.Entry(centerframe, font=('Arial', 16))
        addcomponentNametextbox.pack()

        #Quantity label
        addquantitylabel = Label(centerframe,text="Enter quantity", font=('Arial', 20))
        addquantitylabel.pack(pady=10)

        #Quantity input
        addquantitytextbox = tk.Entry(centerframe, font=('Arial', 16))
        addquantitytextbox.pack()

        #Minimum quantity label
        addminQuantitylabel = Label(centerframe,text="Enter minimum quantity", font=('Arial', 20))
        addminQuantitylabel.pack(pady=10)

        #Minimum quantity input
        addminQuantitytextbox = tk.Entry(centerframe, font=('Arial', 16))
        addminQuantitytextbox.pack()

        #Status label
        addstatuslabel = Label(centerframe,text="Enter status", font=('Arial', 20))
        addstatuslabel.pack(pady=10)

        #Status options
        status_options = ["outOfStock", "available", "inUse", "faulty", "maintenance"]
        #Status dropdown
        addstatustextbox = ttk.Combobox(centerframe, values=status_options, font=('Arial', 16))
        addstatustextbox.current(1)
        addstatustextbox.pack()

        #Confirm add component button
        addbutton = tk.Button(centerframe, text="Confirm", font=('Arial', 16), command=lambda: self.utils.validateAddComponent(addcomponentIdtextbox.get(), addcomponentNametextbox.get(), addquantitytextbox.get(), addminQuantitytextbox.get(), addstatustextbox.get()))
        addbutton.pack(pady=10)

        #delete component page
        
        #Center delete page
        centerframe = Frame(self.deletecomponentpage)
        centerframe.pack(side='top', fill='x', pady=60)

        #Delete page title
        titlelabel = Label(centerframe,text="Delete component", font=('Arial', 20))
        titlelabel.pack(pady=30)

        #Delete component Id label
        deletecomponentIdlabel = Label(centerframe,text="Enter component Id to delete", font=('Arial', 20))
        deletecomponentIdlabel.pack(pady=20)

        #Delete component Id input
        deletecomponentIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        deletecomponentIdtextbox.pack()

        #Confirm delete button
        deletebutton = tk.Button(centerframe, text="Confirm", font=('Arial', 16), command=lambda: self.utils.validateDeleteComponent(deletecomponentIdtextbox.get()))
        deletebutton.pack(pady=20)

        #edit component page
        
        #Center edit page
        centerframe = Frame(self.editcomponentpage)
        centerframe.pack(side='top', fill='x', pady=60)

        #Edit page title
        edittitlelabel = Label(centerframe,text="Edit component", font=('Arial', 20))
        edittitlelabel.pack(pady=30)

        #Old component Id label
        editoldcomponentIdlabel = Label(centerframe,text="Enter component Id to edit", font=('Arial', 20))
        editoldcomponentIdlabel.pack(pady=10)

        #Old component Id input
        editoldcomponentIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editoldcomponentIdtextbox.pack()

        #New component Id label
        editnewcomponentIdlabel = Label(centerframe,text="Enter new component Id", font=('Arial', 20))
        editnewcomponentIdlabel.pack(pady=10)

        #New component Id input
        editnewcomponentIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewcomponentIdtextbox.pack()

        #New component name label
        editnewcomponentNamelabel = Label(centerframe,text="Enter new component name", font=('Arial', 20))
        editnewcomponentNamelabel.pack(pady=10)

        #New component name input
        editnewcomponentNametextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewcomponentNametextbox.pack()

        #New quantity label
        editnewquantitylabel = Label(centerframe,text="Enter new quantity", font=('Arial', 20))
        editnewquantitylabel.pack(pady=10)

        #New quantity input
        editnewquantitytextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewquantitytextbox.pack()

        #New minimum quantity label
        editnewminQuantitylabel = Label(centerframe,text="Enter new minimum quantity", font=('Arial', 20))
        editnewminQuantitylabel.pack(pady=10)

        #New minimum quantity input
        editnewminQuantitytextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewminQuantitytextbox.pack()

        #New status label
        editnewstatuslabel = Label(centerframe,text="Enter new status", font=('Arial', 20))
        editnewstatuslabel.pack(pady=10)

        #New status dropdown
        editnewstatustextbox = ttk.Combobox(centerframe, values=status_options, font=('Arial', 16))
        editnewstatustextbox.current(1)
        editnewstatustextbox.pack()

        #Confirm edit component button
        editbutton = tk.Button(centerframe, text="Confirm", font=('Arial', 16), command=lambda: self.utils.validateEditComponent(editoldcomponentIdtextbox.get(), editnewcomponentIdtextbox.get(), editnewcomponentNametextbox.get(), editnewquantitytextbox.get(), editnewminQuantitytextbox.get(), editnewstatustextbox.get()))
        editbutton.pack(pady=10)

    def create_employee_menu(self):

        #Create employee pages
        self.viewemployeespage = Frame(self.root)
        self.addemployeepage = Frame(self.root)
        self.deleteemployeepage = Frame(self.root)
        self.editemployeepage = Frame(self.root)

        #Grid employee pages
        self.viewemployeespage.grid(row=0,column=0, sticky="nsew")
        self.addemployeepage.grid(row=0,column=0, sticky="nsew")
        self.deleteemployeepage.grid(row=0,column=0, sticky="nsew")
        self.editemployeepage.grid(row=0,column=0, sticky="nsew")

        #view employees page

        #Create view employees page
        self.viewemployeespage = Frame(self.root)
        self.viewemployeespage.grid(row=0, column=0, sticky="nsew")

        #Center content
        centerframe = Frame(self.viewemployeespage)
        centerframe.pack(side='top', fill='both', expand=True, pady=30)

        #Page title
        titlelabel = Label(centerframe, text="View Employees", font=('Arial', 20))
        titlelabel.pack(pady=20)

        #Table columns
        columns = ("Employee ID", "Username", "Password", "Is Manager")

        #Create table
        tree = ttk.Treeview(centerframe, columns=columns, show="headings", height=15)

        #Configure table columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        #Insert employee data
        for row in self.utils.getEmployeeData():
            tree.insert("", "end", values=row)

        #Pack table
        tree.pack(fill="both", expand=True, padx=20, pady=20)

        #Add scrollbar
        scrollbar = ttk.Scrollbar(centerframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        #Store employee tree
        self.employeeTree = tree

        #add employee page
        
        #Center add employee page
        centerframe = Frame(self.addemployeepage)
        centerframe.pack(side='top', fill='x', pady=60)

        #Add employee title
        addtitlelabel = Label(centerframe, text="Add employee", font=('Arial', 20))
        addtitlelabel.pack(pady=30)

        #Employee Id label
        addemployeeIdlabel = Label(centerframe, text="Enter employee Id", font=('Arial', 20))
        addemployeeIdlabel.pack(pady=10)

        #Employee Id input
        addemployeeIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        addemployeeIdtextbox.pack()

        #Username label
        addusernamelabel = Label(centerframe, text="Enter username", font=('Arial', 20))
        addusernamelabel.pack(pady=10)

        #Username input
        addusernametextbox = tk.Entry(centerframe, font=('Arial', 16))
        addusernametextbox.pack()

        #Password label
        addpasswordlabel = Label(centerframe, text="Enter password", font=('Arial', 20))
        addpasswordlabel.pack(pady=10)

        #Password input
        addpasswordtextbox = tk.Entry(centerframe, font=('Arial', 16))
        addpasswordtextbox.pack()

        #Is manager label
        addisManagerlabel = Label(centerframe, text="Enter if manager", font=('Arial', 20))
        addisManagerlabel.pack(pady=10)

        #Manager checkbox variable
        addisManagervar = tk.BooleanVar()
        #Manager checkbox
        addisManagercheckbox = tk.Checkbutton(centerframe, variable=addisManagervar)
        addisManagercheckbox.pack()

        #Confirm add employee button
        addbutton = tk.Button(
            centerframe,
            text="Confirm",
            font=('Arial', 16),
            command=lambda: self.utils.validateAddEmployee(
                addemployeeIdtextbox.get(),
                addusernametextbox.get(),
                addpasswordtextbox.get(),
                addisManagervar.get()
            )
        )
        addbutton.pack(pady=20)

        #delete employee page

        #Center delete page
        centerframe = Frame(self.deleteemployeepage)
        centerframe.pack(side='top', fill='x', pady=60)

        #Delete employee title
        titlelabel = Label(centerframe, text="Delete employee", font=('Arial', 20))
        titlelabel.pack(pady=30)

        #Delete employee Id label
        deleteemployeeIdlabel = Label(centerframe, text="Enter employee Id to delete", font=('Arial', 20))
        deleteemployeeIdlabel.pack(pady=20)

        #Delete employee Id input
        deleteemployeeIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        deleteemployeeIdtextbox.pack()

        #Confirm delete employee button
        deletebutton = tk.Button(
            centerframe,
            text="Confirm",
            font=('Arial', 16),
            command=lambda: self.utils.validateDeleteEmployee(deleteemployeeIdtextbox.get())
        )
        deletebutton.pack(pady=20)

        #edit employee page

        #Center edit page
        centerframe = Frame(self.editemployeepage)
        centerframe.pack(side='top', fill='x', pady=60)

        #Edit employee title
        edittitlelabel = Label(centerframe, text="Edit employee", font=('Arial', 20))
        edittitlelabel.pack(pady=30)

        #Old employee Id label
        editoldemployeeIdlabel = Label(centerframe, text="Enter employee Id to edit", font=('Arial', 20))
        editoldemployeeIdlabel.pack(pady=10)

        #Old employee Id input
        editoldemployeeIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editoldemployeeIdtextbox.pack()

        #New employee Id label
        editnewemployeeIdlabel = Label(centerframe, text="Enter new employee Id", font=('Arial', 20))
        editnewemployeeIdlabel.pack(pady=10)

        #New employee Id input
        editnewemployeeIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewemployeeIdtextbox.pack()

        #New username label
        editnewusernamelabel = Label(centerframe, text="Enter new username", font=('Arial', 20))
        editnewusernamelabel.pack(pady=10)

        #New username input
        editnewusernametextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewusernametextbox.pack()

        #New password label
        editnewpasswordlabel = Label(centerframe, text="Enter new password", font=('Arial', 20))
        editnewpasswordlabel.pack(pady=10)

        #New password input
        editnewpasswordtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewpasswordtextbox.pack()

        #New isManager label
        editnewisManagerlabel = Label(centerframe, text="Enter new isManager", font=('Arial', 20))
        editnewisManagerlabel.pack(pady=10)

        #Manager checkbox variable
        editnewisManagervar = tk.BooleanVar()
        #Manager checkbox
        editnewisManagercheckbox = tk.Checkbutton(centerframe, variable=editnewisManagervar)
        editnewisManagercheckbox.pack()

        #Confirm edit employee button
        editbutton = tk.Button(
            centerframe,
            text="Confirm",
            font=('Arial', 16),
            command=lambda: self.utils.validateEditEmployee(
                editoldemployeeIdtextbox.get(),
                editnewemployeeIdtextbox.get(),
                editnewusernametextbox.get(),
                editnewpasswordtextbox.get(),
                editnewisManagervar.get()
            )
        )
        editbutton.pack(pady=10)


    def create_log_menu(self):

        #Create view logs page
        self.viewlogspage = Frame(self.root)
        self.viewlogspage.grid(row=0, column=0, sticky="nsew")

        #Center content
        centerframe = Frame(self.viewlogspage)
        centerframe.pack(side='top', fill='both', expand=True, pady=30)

        #Page title
        titlelabel = Label(centerframe, text="View Logs", font=('Arial', 20))
        titlelabel.pack(pady=20)

        #Table columns
        columns = ("Log ID", "Action", "Date", "Time")

        #Create table
        tree = ttk.Treeview(centerframe, columns=columns, show="headings", height=15)

        #Configure table columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        #Insert log data
        for row in self.utils.getLogData():
            tree.insert("", "end", values=row)

        #Pack table
        tree.pack(fill="both", expand=True, padx=20, pady=20)

        #Add scrollbar
        scrollbar = ttk.Scrollbar(centerframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        #Store log tree
        self.logTree = tree

    def create_alert_menu(self):

        #Create view alerts page
        self.viewalertspage = Frame(self.root)
        self.viewalertspage.grid(row=0, column=0, sticky="nsew")

        #Center content
        centerframe = Frame(self.viewalertspage)
        centerframe.pack(side='top', fill='both', expand=True, pady=30)

        #Page title
        titlelabel = Label(centerframe, text="View Alerts", font=('Arial', 20))
        titlelabel.pack(pady=20)

        #Table columns
        columns = ("Description",)

        #Create table
        tree = ttk.Treeview(centerframe, columns=columns, show="headings", height=15)

        #Configure table columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        #Insert alert data
        for row in self.utils.getAlertData():
            tree.insert("", "end", values=row)

        #Pack table
        tree.pack(fill="both", expand=True, padx=20, pady=20)

        #Add scrollbar
        scrollbar = ttk.Scrollbar(centerframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        #Store alert tree
        self.alertTree = tree

    def create_popup(self, message):
        #Show popup message
        messagebox.showinfo(title="", message=message)

    def handle_login(self, username, password):
        #Validate login details
        valid, isManager = self.utils.validateLogin(username, password)
        if valid:
            #Unlock UI
            self.locked = False
            #Enable menu bar
            self.root.config(menu=self.menubar)
            #Show components page
            self.viewcomponentspage.tkraise()
            if isManager:
                #Add manager pages
                self.add_manager_pages()
        else:
            #Show error message
            self.create_popup("Incorrect login details")

    def add_manager_pages(self):

        #Create employee pages
        self.create_employee_menu()

        #Create employee menu
        employeemenu = tk.Menu(self.menubar, tearoff=0)
        employeemenu.add_command(label="View employees", command=self.refresh_view_employees)
        employeemenu.add_command(label="Add employee", command=self.addemployeepage.tkraise)
        employeemenu.add_command(label="Delete employee", command=self.deleteemployeepage.tkraise)
        employeemenu.add_command(label="Edit employee", command=self.editemployeepage.tkraise)

        #Add employee menu to menu bar
        self.menubar.add_cascade(menu=employeemenu, label="Employee Management")

    def refresh_view_components(self):
        #Clear component table
        for row in self.componentTree.get_children():
            self.componentTree.delete(row)
    
        #Reload component data
        for row in self.utils.getComponentData():
            self.componentTree.insert("", "end", values=row)

        #Show components page
        self.viewcomponentspage.tkraise()

    def refresh_view_employees(self):

        #Clear employee table
        for row in self.employeeTree.get_children():
            self.employeeTree.delete(row)

        #Reload employee data
        for row in self.utils.getEmployeeData():
            self.employeeTree.insert("", "end", values=row)

        #Show employees page
        self.viewemployeespage.tkraise()

    def refresh_view_logs(self):

        #Clear log table
        for row in self.logTree.get_children():
            self.logTree.delete(row)

        #Reload log data
        for row in self.utils.getLogData():
            self.logTree.insert("", "end", values=row)

        #Show logs page
        self.viewlogspage.tkraise()

    def refresh_view_alerts(self):

        #Clear alert table
        for row in self.alertTree.get_children():
            self.alertTree.delete(row)

        #Reload alert data
        for row in self.utils.getAlertData():
            self.alertTree.insert("", "end", values=row)

        #Show alerts page
        self.viewalertspage.tkraise()

