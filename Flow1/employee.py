import mysql.connector as mysql
from tabulate import tabulate
from valuecontrol import stringvaluecontrol, integervaluecontrol, stringnavigation, integernavigation
from os import system
from time import sleep
from plot import plottable

def listcov(inlist):
    sl = []
    for i in range(0,len(inlist)):
        sl.append(inlist[i][0])
    return sl

def add_emp(database, cursor, homef):
    # Getting list of all Existing Employee ID's
    cursor.execute('select EmpID from employees')
    # Unpacking the tuple
    existing_empid = listcov(cursor.fetchall())

    # Getting Input of all required Fields
    empname = stringnavigation('Enter employee name: ', homefunc= lambda: emphome(database,cursor,homef))
    empID = stringnavigation('Enter an UNIQUE ID for the employee: ', homefunc= lambda: emphome(database,cursor,homef))
    # Using While Loop to get only a unique Employee ID
    while empID in existing_empid:
        print('Oh No. There is already an Employee with that ID. Try another one')
        empID = stringnavigation('Enter an UNIQUE ID for the employee: ')

    contact = stringnavigation('Enter Phone Number of the employee (without country code): ')
    sal = integernavigation('Enter salary of the employee (without currency notation): ', homefunc= lambda: emphome(database,cursor,homef))
    address = stringnavigation('Enter address of the employee: ', homefunc= lambda: emphome(database,cursor,homef))
    cursor.execute(f"INSERT INTO employees VALUES ('{empID}','{empname}','{address}','{contact}',{sal});")

    # Saving Data
    database.commit()
    print('Record Added Sucessfully')
    print('Redirecting you to home screen........')
    sleep(3)
    system('cls')
    emphome(database, cursor, homef)

def edit_emp(database, cursor, homef):
    # Fetching all Employee ID's
    cursor.execute('select empid from employees')
    existing_empID = listcov(cursor.fetchall())
    # Making sure the user only chooses (inputs) an Existing Employee ID for Editing
    emp_ID = stringvaluecontrol(existing_empID,'Enter Employee ID: ', 'Employee not found. Try again', homefunc= lambda: emphome(database,cursor,homef))

    # Printing the existing data for confirmation
    cursor.execute(f"select * from employees where EmpID = '{emp_ID}'")
    data = cursor.fetchall()
    print("The Existing Record is:")
    print(tabulate(data, headers=["Employee ID", "Employee Name", "Phone Number", "Salary"],tablefmt='fancy_grid'))

    # Asking new data
    print('Enter details below')
    empname = stringnavigation('Enter employee name: ', homefunc= lambda: emphome(database,cursor,homef))
    contact = stringnavigation('Enter Phone Number of the employee (without country code): ', homefunc= lambda: emphome(database,cursor,homef))
    sal = integernavigation('Enter salary of the employee (without currency notation): ', homefunc= lambda: emphome(database,cursor,homef))
    address = stringnavigation('Enter address of the employee: ', homefunc= lambda: emphome(database,cursor,homef))


    # Saving Data
    cursor.execute(f"UPDATE employees SET salary={sal},EmpPhone='{contact}',EmpName='{empname}' WHERE EmpID='{emp_ID}';")
    database.commit()
    print('Record Updated Sucessfully')
    print('Redirecting you to home screen.....')
    sleep(3)
    system('cls')
    emphome(database, cursor, homef)


def del_emp(database, cursor,homef):
    # Selecting Existing Employee ID's
    cursor.execute('select empid from employees')
    existing_empID = listcov(cursor.fetchall())
    # Making sure the user only chooses (inputs) an Existing Employee ID for Deletion
    emp_ID = stringvaluecontrol(existing_empID, 'Enter Employee ID: ', 'Employee not found. Try again', homefunc= lambda: emphome(database,cursor,homef))
    # Fetching and Printing data for confirmation
    cursor.execute(f"select * from employees where EmpID = '{emp_ID}'")
    data = (cursor.fetchall())
    print("The Existing Record is:")
    print(tabulate(data, headers=["Employee ID", "Employee Name", "Phone Number", "Salary"], tablefmt='fancy_grid'))
    conf = stringvaluecontrol(['y','n'], 'Are you sure? [y/n] ', "Oops! 'y' and 'n' are only valid responses. Try again", homefunc= lambda: emphome(database,cursor,homef))
    if conf == 'y':
        # Deleting Data
        cursor.execute(f"DELETE FROM employees WHERE EmpID='{emp_ID}';")
        database.commit()
    else:
        # Redirecting
        print('Okay. That Guy was saved.')
    print('Redirecting you to Home screen.....')
    sleep(3)
    system('cls')
    emphome(database, cursor,homef)

def view_emp(database, cursor, homef):
    # Printing all info about employees
    cursor.execute(f"select * from employees")
    data = (cursor.fetchall())
    print("The Existing Record are:")
    plottable(data, ["Employee ID", "Employee Name", "Phone Number", "Address","Salary"], tablehead="List of all employees")
    system('cls')
    emphome(database, cursor, homef)

def emphome(database,cursor, hfunc = None):

    menu = '''What would you like to do with your employee data?
    1. Add a new Employee
    2. Edit data of an Existing employee
    3. Delete an Employee
    4. View all Employees
'''

    q = integervaluecontrol([1,2,3,4], menu, 'Oops! Only choose from the menu!', homefunc=hfunc)
    system('cls')
    if q == 1:
        add_emp(database, cursor, hfunc)
    elif q == 2:
        edit_emp(database, cursor,hfunc)
    elif q == 3:
        del_emp(database, cursor, hfunc)
    elif q == 4:
        view_emp(database,cursor, hfunc)
