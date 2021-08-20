import mysql.connector as mysql

db = mysql.connect(host = 'libmgmt.heliohost.us', user = 'libmgmt', password = 'nevermindmf', database = 'libmgmt_bookstore')
cur = db.cursor()
#cur.execute('')

def add_emp():
    # Emp ID, Emp Name, EMp Phnum, Emp Address, EMP Salary
    # str, str, str, str, int
    #empid, empname, empphnum
    cur.execute(f"INSERT INTO employees (EmpID,EmpName,EmpPhone,Address,salary) VALUES ('{empid}','{empname}','{empphnum}', '{add}', {sal});")
    print('Done')

def edit_emp():
    # get input EMPID
    empid = input()
    # input Emp Name, EMp Phnum, Emp Address, EMP Salary
    cur.execute(f"UPDATE employees SET EmpName='{empname}',Salary={sal},Address='{add}',EmpPhone='{empphnum}' WHERE EmpID='{empid}';")

    return

def delete_emp():
    # get empid input

    cur.execute(f"DELETE FROM employees WHERE EmpID='{empid}';")

    return

menu = '''
What do you want do?
1. Add
2. Edit 
3. Delete
'''
q = int(input(menu))

if q == 1:
    add_emp()

elif q == 2:
    edit_emp()

elif q == 3:
    delete_emp()