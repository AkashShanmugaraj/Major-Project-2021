#This module has some SQL Functions.
#NOTE: Kindly define every sub_utilities (adding a book, deleting a book, new tansaction etc) as a seperate function.
#It helps us prevent complex if loops , long line of code and also it helps us for recursion

#Importing required modules
import mysql.connector as mysql
from tabulate import tabulate #For tabulating data
from loops import intsyntaxcheck, bookquantloop #Userdefined....found in same folder
from cmd_spin import spin #Userdefined
db = mysql.connect(host='localhost', database='bookstore', user='root', password='nevermindmf')
cur = db.cursor()


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
    bstatus = input("Enter Status of book (InStock, OutofStock, Preorder): ")
    print(bpubyear,"\n\n")
    cur.execute(f"insert into books values('{bid}','{bname}','{bgenre}','{bauthor}',{bpubyear}, {bstock},{bprice},'{bstatus}');")
    db.commit()
    cur.execute(f"select * from books where BookID =  '{bid}'")
    rawdata = cur.fetchall()
    newdata = []
    for data in rawdata:
        newdata.append(list(data))
    print("The Following record was added: ")
    print(tabulate(newdata, headers=["BookID", "Book Name", "Genre", "Author", 'Published Year', 'Stocks Available','Price', 'Status of Book'],
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
    bid = input("Enter BookID: ")
    cur.execute(f'select BookName, Price, Stocks from books where BookID = "{bid}"')
    rawdata = cur.fetchall()
    newdata = []
    for data in rawdata:
        newdata.append(list(data))
    bprice = newdata[0][1]
    bstock = newdata[0][2]
    print("The requested book is: ")
    print(tabulate(newdata, headers=["Book Name", "Price",'Available Stocks'],tablefmt='fancy_grid'))
    bnum = bookquantloop(bstock)
    print(f"Your total amount will be {bnum*bprice}")
    spin("Processing Transaction.......")
    cur.execute(f"UPDATE books SET Stocks={bstock+bnum} WHERE BookID='{bid}';")
    db.commit()
q = input("Do you want to \n\t1. add a book?\n\t2. edit a book? \n......")
if q == "2":
    edit_book()
elif q == "1":
    newtransaction()
db.close()
