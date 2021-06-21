#This module has some SQL Functions.
#NOTE: Kindly define every sub_utilities (adding a book, deleting a book, new tansaction etc) as a seperate function.
#It helps us prevent complex if loops , long line of code and also it helps us for recursion
#Navigation Systems are currently under development
#Importing required modules
import mysql.connector as mysql
#Userdefined....found in same folder
from tabulate import tabulate #For tabulating data
from loops import *
from cmd_spin import spin
#Python Modules
from datetime import datetime
from os import system
from time import sleep
import random
import keyboard as kb
import pyfiglet

#Userdefined
db = mysql.connect(host='localhost', database='bookstore', user='root', password='nevermindmf')
cur = db.cursor()

#Non SQl Funcitons
def tupletolist(thetuple):
    newlist = []
    for i in thetuple:
        for ii in i:
            newlist.append(ii)
    return newlist

def transidgen():
    cur.execute('select TransactionID from transactions')
    data = cur.fetchall()
    def tid_gen():
        numid = ''
        for i in range(6):
            numid += str(random.randint(0, 9))
        return numid
    num = tid_gen()
    existingids = tupletolist(data)

    while num in existingids:
        num = tid_gen()
    return num

def tabulating():
    rawdata = cur.fetchall()
    newdata = []
    for data in rawdata:
        newdata.append(list(data))
    return newdata
# Function for adding a book
def add_book():
    databool = True
    bid = (input("Enter Book ID: "))
    bname = input("Enter Book Name: ")
    bgenre = input("Enter Book Genre: ")
    bauthor = input("Enter Book Author: ")
    bpubyear = intsyntaxcheck('Enter the Year of Publication: ')
    #bstock = (input("Enter available stock: "))
    bstock = intsyntaxcheck("Enter available stock: ")
    #bprice = (input("Enter Price (without currency notation): "))
    bprice = intsyntaxcheck('Enter Price (without currency notation): ')
    print(bpubyear,"\n\n")
    cur.execute(f"insert into books values('{bid}','{bname}','{bgenre}','{bauthor}',{bpubyear}, {bstock},{bprice});")
    db.commit()
    cur.execute(f"select * from books where BookID =  '{bid}'")
    rawdata = cur.fetchall()
    newdata = []
    for data in rawdata:
        newdata.append(list(data))
    print("The Following record was added: ")
    print(tabulate(newdata, headers=["BookID", "Book Name", "Genre", "Author", 'Published Year', 'Stocks Available','Price'],
                   tablefmt='fancy_grid'))


def edit_book():
    bid = int(input("Enter Book ID: "))
    cur.execute(f"select * from books where BookID = {bid}")
    rawdata = cur.fetchall()
    newdata = []
    for data in rawdata:
        newdata.append(list(data))

    newdata[0].pop(5)

    print("The Existing Record is:")
    print(tabulate(newdata, headers=["BookID", "Book Name", "Genre", "Author", 'Published Year', 'Price'], tablefmt='fancy_grid'))
    print("Choose which one you would like to change\n\t1.Book Name\n\t2.Book Genre\n\t3.Book Author\n\t4.Published Year\n\t5.Book Price")
    ch = int(input(""))
    factor = ""
    if ch == 1:
        factor = "BookName"
        value = input("Enter the correct Name: ")
        cur.execute(f"update books set {factor} = '{value}' where BookID = {bid};")
        db.commit()
    elif ch == 2:
        factor = "BookGenre"
        value = input("Enter the correct Book Genre: ")
        cur.execute(f"update books set {factor} = '{value}' where BookID = {bid};")
        db.commit()
    elif ch == 3:
        factor = "Author"
        value = input("Enter the correct Author: ")
        cur.execute(f"update books set {factor} = '{value}' where BookID = {bid};")
        db.commit()
    elif ch == 4:
        factor = "PubYear"
        value = int(input("Enter the correct Published Year: "))
        cur.execute(f"update books set {factor} = {value} where BookID = {bid};")
        db.commit()
    elif ch == 5:
        factor = "Price"
        value = int(input("Enter the Correct Price: "))
        cur.execute(f"update books set {factor} = {value} where BookID = {bid};")
        db.commit()
    cur.execute(f"select * from books where BookID = {bid}")
    rawdata = cur.fetchall()
    newdata = []
    for data in rawdata:
        newdata.append(list(data))
    newdata[0].pop(5)
    print("Changed record is: ")
    print(tabulate(newdata, headers=["BookID", "Book Name", "Genre", "Author", 'Published Year', 'Price'],
                   tablefmt='fancy_grid'))

def newtransaction():
    cur.execute("select BookID from books;")
    data = cur.fetchall()
    data = tupletolist(data)
    bid = stringvaluecontrol(data, "Enter Book ID: ", "Requested Book Not available in directory")
    cur.execute(f'select BookName, Price, Stocks from books where BookID = "{bid}"')
    booksdata = tabulating()
    bprice = booksdata[0][1]
    bstock = booksdata[0][2]
    print("The requested book is: ")
    print(tabulate(booksdata, headers=["Book Name", "Price",'Available Stocks'],tablefmt='fancy_grid'))
    bnum = bookquantloop(bstock)
    print(f"Your total amount will be {bnum*bprice}")


    conf = stringvaluecontrol(["y", "n"], "Do you want to proceed with your order? [y/n]: ", "Only y and n are allowed!")
    if conf == 'y':
        custphnum = int(input("Enter the Phone number of the customer: "))
        custphnum = int(input("Reconfirm the Phone number of the customer: "))
        spin('Processing Transaction.....')
        today = datetime.now()
        id = int(transidgen())
        cur.execute(f"INSERT INTO transactions VALUES ('{today}',{id}, '{bid}',{bnum},{custphnum});")
        cur.execute(f"UPDATE books SET Stocks={bstock-bnum} WHERE BookID='{bid}';")
        db.commit()
        print("\nTransaction was Sucessful.\nYou will be redirected to home screen now")
        sleep(5)
        system('cls')
        home()
    elif conf == "n":
        print("The transaction was cancelled")
        print("\nTransaction was Unsucessful.\nYou will be redirected to home screen now")
        sleep(5)
        system('cls')
        home()
def viewtransaction():
    cur.execute('select * from transactions')
    transdata = tabulating()
    print("Existing Records are: ")
    print(tabulate(transdata, headers=["Date", "Customer Phone Number", 'BookID', 'Purchased Quantity'], tablefmt='fancy_grid'))

def viewbooks():
    menu2 = '''How do you want to have the data displayed?
        1. Just as it is
        2. Ordering Books Name in Ascending Order
        3. Ordering Books Name in Descending Order
        4. Ordering Author Name in Ascending Order
        5. Ordering Author Name in Descending Order
    .....'''
    selection = integervaluecontrol([1,2,3], menu2, 'Choose only anyone of the following (1,2,3)!!')
    if selection == 1:
        cur.execute('select * from books')
    elif selection == 2:
        cur.execute('select * from books order by Bookname')
    elif selection == 3:
        cur.execute('select * from books order by Bookname desc')
    elif selection == 4:
        cur.execute('select * from books order by Author')
    elif selection == 5:
        cur.execute('select * from books order by Author desc')
    data = tabulating()
    print(tabulate(data, headers=['Book ID','Book Name', 'Book Genre', 'Author', 'Year of Publication', 'Available Stocks', 'Price'], tablefmt='fancy_grid'))
    redirect = stringvaluecontrol(['y'], "Press y when you are ready to be redirected to the home screen: ","Only permitted value is 'y'!!")
    system('cls')
    redirect_home()

def home():
    print(pyfiglet.figlet_format("Welcome Akash Shanmugaraj", font = "digital" ))
    menu = '''Do you want to \n\t1. add a book?\n\t2. edit a book? \n\t3. create a new transaction\n\t4.view transactions?\n\t5.view books?\n\t7. Exit App\n...... '''
    q = integervaluecontrol([1,2,3,4,5,6,7], menu, '\nChoose one only from the following [1,2,3,4,5,6,7]!!')
    if q == 1:
        system('cls')
        add_book()
    elif q == 2:
        system('cls')
        edit_book()
    elif q == 3:
        system('cls')
        newtransaction()
    elif q == 4:
        system('cls')
        viewtransaction()
    elif q == 5:
        system('cls')
        viewbooks()
    elif q == 7:
        exit()

def redirect_home():
    system('cls')
    home()

print(pyfiglet.figlet_format("Book store Management App", font="slant"))
home()
db.close()
