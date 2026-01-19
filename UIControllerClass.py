import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class UIController:
    def __init__(self, root, utils):
        self.root = root
        self.utils = utils
        self.locked = True
    def initialiseUI(self):
        self.menubar = tk.Menu(self.root)

        self.create_login_page()
        self.create_component_menu()
        self.create_log_menu()
        self.create_alert_menu()

        componentmenu = tk.Menu(self.menubar, tearoff=0)
        componentmenu.add_command(label="View components", command=self.refresh_view_components)
        componentmenu.add_command(label="Add component", command=self.addcomponentpage.tkraise)
        componentmenu.add_command(label="Delete component", command=self.deletecomponentpage.tkraise)
        componentmenu.add_command(label="Edit component", command=self.editcomponentpage.tkraise)

        logmenu = tk.Menu(self.menubar, tearoff=0)
        logmenu.add_command(label="View logs", command=self.refresh_view_logs)

        alertmenu = tk.Menu(self.menubar, tearoff=0)
        alertmenu.add_command(label="View alerts", command=self.refresh_view_alerts)

        backupmenu = tk.Menu(self.menubar, tearoff=0)
        backupmenu.add_command(label="Create backup", command=self.utils.manageBackup)

        exportmenu = tk.Menu(self.menubar, tearoff=0)
        exportmenu.add_command(label="Export data", command=self.utils.manageExport)

        self.menubar.add_cascade(menu=componentmenu, label="Component Management")
        self.menubar.add_cascade(menu=logmenu, label="Log management")
        self.menubar.add_cascade(menu=alertmenu, label="Alert management")
        self.menubar.add_cascade(menu=backupmenu, label="Backup management")
        self.menubar.add_cascade(menu=exportmenu, label="Export management")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.loginpage.tkraise()


        self.root.geometry("1280x800")
        self.root.title("Inventory Management System")

    def create_login_page(self):

        #login page
        
        self.loginpage = Frame(self.root)
        self.loginpage.grid(row=0,column=0, sticky="nsew")
        
        centerframe = Frame(self.loginpage)
        centerframe.pack(side='top', fill='x', pady=60)

        titlelabel = Label(centerframe,text="Login", font=('Arial', 20))
        titlelabel.pack(pady=30)

        usernamelabel = Label(centerframe,text="Enter username", font=('Arial', 20))
        usernamelabel.pack(pady=20)

        usernametextbox = tk.Entry(centerframe, font=('Arial', 16))
        usernametextbox.pack()

        passwordlabel = Label(centerframe,text="Enter password", font=('Arial', 20))
        passwordlabel.pack(pady=20)

        passwordtextbox = tk.Entry(centerframe, font=('Arial', 16))
        passwordtextbox.pack()

        button = tk.Button(centerframe, text="Confirm", font=('Arial', 16), command=lambda: self.handle_login(usernametextbox.get(), passwordtextbox.get()))
        button.pack(pady=20)

    def create_component_menu(self):

        self.viewcomponentspage = Frame(self.root)
        self.addcomponentpage = Frame(self.root)
        self.deletecomponentpage = Frame(self.root)
        self.editcomponentpage = Frame(self.root)

        self.viewcomponentspage.grid(row=0,column=0, sticky="nsew")
        self.addcomponentpage.grid(row=0,column=0, sticky="nsew")
        self.deletecomponentpage.grid(row=0,column=0, sticky="nsew")
        self.editcomponentpage.grid(row=0,column=0, sticky="nsew")

        #view components page

        self.viewcomponentspage = Frame(self.root)
        self.viewcomponentspage.grid(row=0, column=0, sticky="nsew")

        centerframe = Frame(self.viewcomponentspage)
        centerframe.pack(side='top', fill='both', expand=True, pady=30)

        titlelabel = Label(centerframe, text="View Components", font=('Arial', 20))
        titlelabel.pack(pady=20)

        columns = ("Component ID", "Name", "Quantity", "Min Quantity", "Status")

        tree = ttk.Treeview(centerframe, columns=columns, show="headings", height=15)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        for row in self.utils.getComponentData():
            tree.insert("", "end", values=row)

        tree.pack(fill="both", expand=True, padx=20, pady=20)

        scrollbar = ttk.Scrollbar(centerframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.componentTree = tree

        #create add page
        
        centerframe = Frame(self.addcomponentpage)
        centerframe.pack(side='top', fill='x', pady=60)

        addtitlelabel = Label(centerframe,text="Add component", font=('Arial', 20))
        addtitlelabel.pack(pady=30)

        addcomponentIdlabel = Label(centerframe,text="Enter component Id", font=('Arial', 20))
        addcomponentIdlabel.pack(pady=10)

        addcomponentIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        addcomponentIdtextbox.pack()

        addcomponentNamelabel = Label(centerframe,text="Enter component name", font=('Arial', 20))
        addcomponentNamelabel.pack(pady=10)

        addcomponentNametextbox = tk.Entry(centerframe, font=('Arial', 16))
        addcomponentNametextbox.pack()

        addquantitylabel = Label(centerframe,text="Enter quantity", font=('Arial', 20))
        addquantitylabel.pack(pady=10)

        addquantitytextbox = tk.Entry(centerframe, font=('Arial', 16))
        addquantitytextbox.pack()

        addminQuantitylabel = Label(centerframe,text="Enter minimum quantity", font=('Arial', 20))
        addminQuantitylabel.pack(pady=10)

        addminQuantitytextbox = tk.Entry(centerframe, font=('Arial', 16))
        addminQuantitytextbox.pack()

        addstatuslabel = Label(centerframe,text="Enter status", font=('Arial', 20))
        addstatuslabel.pack(pady=10)

        status_options = ["outOfStock", "available", "inUse", "faulty", "maintenance"]
        addstatustextbox = ttk.Combobox(centerframe, values=status_options, font=('Arial', 16))
        addstatustextbox.current(1)
        addstatustextbox.pack()

        addbutton = tk.Button(centerframe, text="Confirm", font=('Arial', 16), command=lambda: self.utils.validateAddComponent(addcomponentIdtextbox.get(), addcomponentNametextbox.get(), addquantitytextbox.get(), addminQuantitytextbox.get(), addstatustextbox.get()))
        addbutton.pack(pady=10)

        #delete component page
        
        centerframe = Frame(self.deletecomponentpage)
        centerframe.pack(side='top', fill='x', pady=60)

        titlelabel = Label(centerframe,text="Delete component", font=('Arial', 20))
        titlelabel.pack(pady=30)

        deletecomponentIdlabel = Label(centerframe,text="Enter component Id to delete", font=('Arial', 20))
        deletecomponentIdlabel.pack(pady=20)

        deletecomponentIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        deletecomponentIdtextbox.pack()

        deletebutton = tk.Button(centerframe, text="Confirm", font=('Arial', 16), command=lambda: self.utils.validateDeleteComponent(deletecomponentIdtextbox.get()))
        deletebutton.pack(pady=20)

        #edit component page
        
        centerframe = Frame(self.editcomponentpage)
        centerframe.pack(side='top', fill='x', pady=60)

        edittitlelabel = Label(centerframe,text="Edit component", font=('Arial', 20))
        edittitlelabel.pack(pady=30)

        editoldcomponentIdlabel = Label(centerframe,text="Enter component Id to edit", font=('Arial', 20))
        editoldcomponentIdlabel.pack(pady=10)

        editoldcomponentIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editoldcomponentIdtextbox.pack()

        editnewcomponentIdlabel = Label(centerframe,text="Enter new component Id", font=('Arial', 20))
        editnewcomponentIdlabel.pack(pady=10)

        editnewcomponentIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewcomponentIdtextbox.pack()

        editnewcomponentNamelabel = Label(centerframe,text="Enter new component name", font=('Arial', 20))
        editnewcomponentNamelabel.pack(pady=10)

        editnewcomponentNametextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewcomponentNametextbox.pack()

        editnewquantitylabel = Label(centerframe,text="Enter new quantity", font=('Arial', 20))
        editnewquantitylabel.pack(pady=10)

        editnewquantitytextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewquantitytextbox.pack()

        editnewminQuantitylabel = Label(centerframe,text="Enter new minimum quantity", font=('Arial', 20))
        editnewminQuantitylabel.pack(pady=10)

        editnewminQuantitytextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewminQuantitytextbox.pack()

        editnewstatuslabel = Label(centerframe,text="Enter new status", font=('Arial', 20))
        editnewstatuslabel.pack(pady=10)

        editnewstatustextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewstatustextbox.pack()

        editbutton = tk.Button(centerframe, text="Confirm", font=('Arial', 16), command=lambda: self.utils.validateEditComponent(editoldcomponentIdtextbox.get(), editnewcomponentIdtextbox.get(), editnewcomponentNametextbox.get(), editnewquantitytextbox.get(), editnewminQuantitytextbox.get(), editnewstatustextbox.get()))
        editbutton.pack(pady=10)

    def create_employee_menu(self):

        self.viewemployeespage = Frame(self.root)
        self.addemployeepage = Frame(self.root)
        self.deleteemployeepage = Frame(self.root)
        self.editemployeepage = Frame(self.root)

        self.viewemployeespage.grid(row=0,column=0, sticky="nsew")
        self.addemployeepage.grid(row=0,column=0, sticky="nsew")
        self.deleteemployeepage.grid(row=0,column=0, sticky="nsew")
        self.editemployeepage.grid(row=0,column=0, sticky="nsew")

        #view employees page

        self.viewemployeespage = Frame(self.root)
        self.viewemployeespage.grid(row=0, column=0, sticky="nsew")

        centerframe = Frame(self.viewemployeespage)
        centerframe.pack(side='top', fill='both', expand=True, pady=30)

        titlelabel = Label(centerframe, text="View Employees", font=('Arial', 20))
        titlelabel.pack(pady=20)

        columns = ("Employee ID", "Username", "Password", "Is Manager")

        tree = ttk.Treeview(centerframe, columns=columns, show="headings", height=15)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        for row in self.utils.getEmployeeData():
            tree.insert("", "end", values=row)

        tree.pack(fill="both", expand=True, padx=20, pady=20)

        scrollbar = ttk.Scrollbar(centerframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.employeeTree = tree

        #add employee page
        
        centerframe = Frame(self.addemployeepage)
        centerframe.pack(side='top', fill='x', pady=60)

        addtitlelabel = Label(centerframe, text="Add employee", font=('Arial', 20))
        addtitlelabel.pack(pady=30)

        addemployeeIdlabel = Label(centerframe, text="Enter employee Id", font=('Arial', 20))
        addemployeeIdlabel.pack(pady=10)

        addemployeeIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        addemployeeIdtextbox.pack()

        addusernamelabel = Label(centerframe, text="Enter username", font=('Arial', 20))
        addusernamelabel.pack(pady=10)

        addusernametextbox = tk.Entry(centerframe, font=('Arial', 16))
        addusernametextbox.pack()

        addpasswordlabel = Label(centerframe, text="Enter password", font=('Arial', 20))
        addpasswordlabel.pack(pady=10)

        addpasswordtextbox = tk.Entry(centerframe, font=('Arial', 16))
        addpasswordtextbox.pack()

        addisManagerlabel = Label(centerframe, text="Enter if manager", font=('Arial', 20))
        addisManagerlabel.pack(pady=10)

        addisManagertextbox = tk.Entry(centerframe, font=('Arial', 16))
        addisManagerlabel.pack(pady=10)

        addisManagervar = tk.BooleanVar()
        addisManagercheckbox = tk.Checkbutton(centerframe, variable=addisManagervar)
        addisManagercheckbox.pack()

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

        centerframe = Frame(self.deleteemployeepage)
        centerframe.pack(side='top', fill='x', pady=60)

        titlelabel = Label(centerframe, text="Delete employee", font=('Arial', 20))
        titlelabel.pack(pady=30)

        deleteemployeeIdlabel = Label(centerframe, text="Enter employee Id to delete", font=('Arial', 20))
        deleteemployeeIdlabel.pack(pady=20)

        deleteemployeeIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        deleteemployeeIdtextbox.pack()

        deletebutton = tk.Button(
            centerframe,
            text="Confirm",
            font=('Arial', 16),
            command=lambda: self.utils.validateDeleteEmployee(deleteemployeeIdtextbox.get())
        )
        deletebutton.pack(pady=20)

        #edit employee page

        centerframe = Frame(self.editemployeepage)
        centerframe.pack(side='top', fill='x', pady=60)

        edittitlelabel = Label(centerframe, text="Edit employee", font=('Arial', 20))
        edittitlelabel.pack(pady=30)

        editoldemployeeIdlabel = Label(centerframe, text="Enter employee Id to edit", font=('Arial', 20))
        editoldemployeeIdlabel.pack(pady=10)

        editoldemployeeIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editoldemployeeIdtextbox.pack()

        editnewemployeeIdlabel = Label(centerframe, text="Enter new employee Id", font=('Arial', 20))
        editnewemployeeIdlabel.pack(pady=10)

        editnewemployeeIdtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewemployeeIdtextbox.pack()

        editnewusernamelabel = Label(centerframe, text="Enter new username", font=('Arial', 20))
        editnewusernamelabel.pack(pady=10)

        editnewusernametextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewusernametextbox.pack()

        editnewpasswordlabel = Label(centerframe, text="Enter new password", font=('Arial', 20))
        editnewpasswordlabel.pack(pady=10)

        editnewpasswordtextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewpasswordtextbox.pack()

        editnewisManagerlabel = Label(centerframe, text="Enter new isManager", font=('Arial', 20))
        editnewisManagerlabel.pack(pady=10)

        editnewisManagertextbox = tk.Entry(centerframe, font=('Arial', 16))
        editnewisManagerlabel.pack(pady=10)

        editnewisManagervar = tk.BooleanVar()
        editnewisManagercheckbox = tk.Checkbutton(centerframe, variable=editnewisManagervar)
        editnewisManagercheckbox.pack()

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

        self.viewlogspage = Frame(self.root)
        self.viewlogspage.grid(row=0, column=0, sticky="nsew")

        centerframe = Frame(self.viewlogspage)
        centerframe.pack(side='top', fill='both', expand=True, pady=30)

        titlelabel = Label(centerframe, text="View Logs", font=('Arial', 20))
        titlelabel.pack(pady=20)

        columns = ("Log ID", "Action", "Date", "Time")

        tree = ttk.Treeview(centerframe, columns=columns, show="headings", height=15)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        for row in self.utils.getLogData():
            tree.insert("", "end", values=row)

        tree.pack(fill="both", expand=True, padx=20, pady=20)

        scrollbar = ttk.Scrollbar(centerframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.logTree = tree

    def create_alert_menu(self):

        self.viewalertspage = Frame(self.root)
        self.viewalertspage.grid(row=0, column=0, sticky="nsew")

        centerframe = Frame(self.viewalertspage)
        centerframe.pack(side='top', fill='both', expand=True, pady=30)

        titlelabel = Label(centerframe, text="View Alerts", font=('Arial', 20))
        titlelabel.pack(pady=20)

        columns = ("Description",)

        tree = ttk.Treeview(centerframe, columns=columns, show="headings", height=15)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        for row in self.utils.getAlertData():
            tree.insert("", "end", values=row)

        tree.pack(fill="both", expand=True, padx=20, pady=20)

        scrollbar = ttk.Scrollbar(centerframe, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.alertTree = tree

    def create_popup(self, message):
        messagebox.showinfo(title="", message=message)
    def handle_login(self, username, password):
        valid, isManager = self.utils.validateLogin(username, password)
        if valid:
            self.locked = False
            self.root.config(menu=self.menubar)
            self.viewcomponentspage.tkraise()
            if isManager:
                self.add_manager_pages()
        else:
            self.create_popup("Incorrect login details")
    def add_manager_pages(self):

        self.create_employee_menu()

        employeemenu = tk.Menu(self.menubar, tearoff=0)
        employeemenu.add_command(label="View employees", command=self.refresh_view_employees)
        employeemenu.add_command(label="Add employee", command=self.addemployeepage.tkraise)
        employeemenu.add_command(label="Delete employee", command=self.deleteemployeepage.tkraise)
        employeemenu.add_command(label="Edit employee", command=self.editemployeepage.tkraise)

        self.menubar.add_cascade(menu=employeemenu, label="Employee Management")

    def refresh_view_components(self):
        for row in self.componentTree.get_children():
            self.componentTree.delete(row)
    
        for row in self.utils.getComponentData():
            self.componentTree.insert("", "end", values=row)

        self.viewcomponentspage.tkraise()

    def refresh_view_employees(self):

        for row in self.employeeTree.get_children():
            self.employeeTree.delete(row)

        for row in self.utils.getEmployeeData():
            self.employeeTree.insert("", "end", values=row)

        self.viewemployeespage.tkraise()

    def refresh_view_logs(self):

        for row in self.logTree.get_children():
            self.logTree.delete(row)

        for row in self.utils.getLogData():
            self.logTree.insert("", "end", values=row)

        self.viewlogspage.tkraise()

    def refresh_view_alerts(self):

        for row in self.alertTree.get_children():
            self.alertTree.delete(row)

        for row in self.utils.getAlertData():
            self.alertTree.insert("", "end", values=row)

        self.viewalertspage.tkraise()
