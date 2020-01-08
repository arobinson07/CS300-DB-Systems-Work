from tkinter import*                                #TKinter Import for GUI
import pyodbc                                         #Pyodbc import for database connection


#Server Connection
connection=pyodbc.connect("DSN=SQLServer", autocommit=True)

if connection:
    print("Established Connection to SQL Server successfully.")

def branchAssets():
    cursor = connection.execute("{call Branch_Assets_List}")
    for c in cursor:
        print(c[0], c[1])

def employeeAssets():
    cursor = connection.execute("{call Employee_Assets_List}")
    for c in cursor:
        print(c[0], c[1], c[2])

def employeeBranch():
    cursor = connection.execute("{call Branch_Employee_List}")
    for c in cursor:
        print(c[0], c[1], c[2])

def assetModel():
    cursor = connection.execute("{call Asset_Model_List}")
    for c in cursor:
        print(c[0], c[1], c[2])

def branchAssetCount():
    cursor = connection.execute("{call Branch_Assets}")
    for c in cursor:
        print(c[0], c[1])

def assetUpdate():
    params = (int(e3.get()), e5.get(), int(e2.get()), int(e1.get()), int(e4.get()))
    cursor = connection.cusor()
    cursor.execute("EXEC Update_Asset", *params)

def assetInsert():
    params = (int(e3.get()), e5.get(), int(e2.get()), int(e1.get()), int(e4.get()))
    connection.execute("{CALL Insert_Asset, (?,?,?,?,?}", *params)


window = Tk()

#Labels
l1 = Label(window, text="Employee ID")      #Label for ID for search
l1.grid(row=0, column=0, sticky=E)

l2 = Label(window, text="Model ID")       #Label for model ID for search
l2.grid(row=1, column=0, sticky=E)

l3 = Label(window, text="AssetID")       #Label for Last name of employee for search
l3.grid(row=2, column=0, sticky=E)

l4 = Label(window, text="BranchID")       #Label for Last name of employee for search
l4.grid(row=3, column=0, sticky=E)

l5 = Label(window, text="Serial Number")      #Label for ID for search
l5.grid(row=4, column=0, sticky=E)

#Entries

e1 = Entry(window)
e1.grid(row=0, column=1)

e2 = Entry(window)
e2.grid(row=1, column=1)

e3 = Entry(window)
e3.grid(row=2, column=1)

e4 = Entry(window)
e4.grid(row=3, column=1)

e5 = Entry(window)
e5.grid(row=4, column=1)


#Buttons
b1 = Button(window, text="View By Branch Number", width=25, command = branchAssets)        #Creates button to be used for pulling all assets as a single list with branchID
b1.grid(row=2, column=3)

b2 = Button(window, text="View By Employee name", width=25, command = employeeAssets)        #Creates button to be used for pulling all assets as a single list with employee's name
b2.grid(row=3, column=3)

b3 = Button(window, text="View By Employee By Branch", width=25, command = employeeBranch)        #Creates button to be used for pulling all employee names and branchIDs
b3.grid(row=4, column=3)

b4 = Button(window, text="View By Model and Type", width=25, command = assetModel)        #Creates button to be used for pulling all employee names and branchIDs
b4.grid(row=5, column=3)

b4 = Button(window, text="View branch and total Assets", width=25, command = branchAssetCount)        #Creates button to be used for pulling all employee names and branchIDs
b4.grid(row=2, column=2)

b6 = Button(window, text="Add an Asset", width=25, command = assetInsert)        #Creates button to be used for pulling all assets as a single list
b6.grid(row=3, column=2)

b7 = Button(window, text="Remove an Asset", width=25)        #Creates button to be used for pulling all assets as a single list
b7.grid(row=4, column=2)

b8 = Button(window, text="Update an Asset", width=25)        #Creates button to be used for pulling all assets as a single list
b8.grid(row=5, column=2)

window.mainloop()
