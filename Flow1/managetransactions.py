from tabulate import tabulate

from valuecontrol import *
from cmd_spin import spin
import random
from datetime import datetime
from time import sleep
from os import system
from plot import plottable


# Function for unpacking a tuple
def tupletolist(thetuple):
    newlist = []
    for i in thetuple:
        for ii in i:
            newlist.append(ii)
    return newlist

# Function to generate a unique transaction ID
def transidgen(cursor):
    cursor.execute('select TransactionID from transactions')
    data = cursor.fetchall()
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



def newtransaction(database, cursor,homef):
    # Fetching  Exisiting BookID's
    cursor.execute("select BookID from books2;")
    data = cursor.fetchall()
    # Unpacking data
    data = tupletolist(data)
    # Making sure the user only chooses a book from the existing list
    bid = stringvaluecontrol(data, "Enter Book ID: ", "Requested Book Not available in directory", homefunc=lambda: transhome(database, cursor, homef))
    cursor.execute(f'select BookName, ISBN, Price, Stocks from books2 where BookID = "{bid}"')
    # Fetching and Unpacking the new data
    booksdata = cursor.fetchall()
    # Using Indexing to extract the price, stocks, isbn
    bisbn = booksdata[0][1]
    bprice = booksdata[0][2]
    bstock = booksdata[0][3]
    # Printing Requested book
    print("The requested book is: ")
    print(tabulate(booksdata, headers=["Book Name", "ISBN","Price",'Available Stocks'],tablefmt='fancy_grid'))
    bnum = bookquantloop(bstock)
    print(f"Your total amount will be {bnum*bprice}")
    # Transaction confirmation block
    conf = stringvaluecontrol(["y", "n"], "Do you want to proceed with your order? [y/n]: ", "Only y and n are allowed!", homefunc=lambda: transhome(database, cursor, homef))
    if conf == 'y':
        # Getting Required Details
        custphnum = integernavigation("Enter the Phone number of the customer: ", homefunc=lambda: transhome(database, cursor, homef))

        spin('Processing Transaction.....')
        # Getting todays date
        today = datetime.now()
        # Generating Unique Trasaction ID
        id = int(transidgen(cursor))

        # Saving Data
        cursor.execute(f"INSERT INTO transactions VALUES ('{today}',{id}, '{bid}', {bisbn},{bnum},{custphnum}, {bnum*bprice});")
        cursor.execute(f"UPDATE books2 SET Stocks={bstock-bnum} WHERE BookID='{bid}';")
        database.commit()
        print("\nTransaction was Sucessful.\nYou will be redirected to home screen now")
        sleep(5)
        system('cls')
    elif conf == "n":
        print("The transaction was cancelled")
        print("\nTransaction was Unsucessful.\nYou will be redirected to home screen now")
        sleep(5)
        system('cls')

# Function for viewing all Transactions
def viewtransaction(database, cursor, homef):
    # Fetching all data
    cursor.execute('select * from transactions')
    transdata = cursor.fetchall()
    print("Existing Records are: ")
    #print(tabulate(transdata, headers=["Date and Time", "Transaction ID","Book ID", "ISBN", 'Purchased Quantity',"Customer Phone Number",'Total Cost'], tablefmt='fancy_grid'))
    plottable(transdata, ["Date and Time", "Transaction ID","Book ID", "ISBN", 'Purchased Quantity',"Customer Phone Number",'Total Cost'], tablehead = 'Existing Transactions')
    conf = stringvaluecontrol(['y'],"Press y when you are ready to be redirected to the home screen", "Please give in a valid response",homefunc=lambda: transhome(database, cursor, homef))
    system('cls')
    transhome(database, cursor, homef)
# Function for Local Home
def transhome(database, cursor, hfunc = None):

    menu = '''What do you want to do?
    1. Perform New Transaction
    2. View All Transactions
    3. Go Back to the Main Menu of the whole program
'''
    q = integervaluecontrol([1,2,3], menu, 'Uhuh. Choose only from the menu', homefunc=hfunc)
    if q == 1:
        import os
        os.system('cls')
        newtransaction(database, cursor,hfunc)
    elif q == 2:
        viewtransaction(database, cursor, hfunc)
    elif q == 3:
        hfunc()