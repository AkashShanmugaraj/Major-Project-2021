# Importing required Modules
import os
import time
from isbn import get_isbn_details
import mysql.connector as mysql
from tabulate import tabulate
from valuecontrol import *

# Connecting to the database
db = mysql.connect(host='localhost', database='bstorev2', user='root', password='nevermindmf')
cur = db.cursor()
def listcov(inlist):
    sl = []
    for i in range(0,len(inlist)):
        sl.append(inlist[i][0])
    return sl

def add_book():
    print('Adding a Book')
    # Getting details from Google Books API
    details = get_isbn_details()
    # Converting it to a list
    tabulatingdetails = [details]
    # Printing it Tabulated
    print(tabulate(tabulatingdetails, headers=["Title", "Authors", "Category", "ISBN","Publisher", 'Published Date'],
                       tablefmt='fancy_grid'))
    q = stringvaluecontrol(['y','n'],'Are the above details correct? ', "Uhuh. Only choose from 'y' or 'n'")

    if q == 'y':
        cur.execute('select BookID from books2')
        # Fetching Existing BookID's
        existing_BID = (listcov(cur.fetchall()))
        bid = stringnavigation('Enter BookID: ')
        # Book ID is a Unique Key. Duplicates are not allowed. So we use the below while loop
        while bid in existing_BID:
            print('Oops! There is already a Book in your store with this Book ID. Try a Different one')
            bid = stringnavigation('Enter BookID: ')
        bstock = integernavigation('Enter Total Stocks of the Book: ')
        bprice = integernavigation('Name your price for the book: ')

        # Iserting Details
        cur.execute(f"insert into books2 values('{bid}','{details[0]}',{details[3]},'{details[1]}','{details[2]}','{details[4]}', '{details[5]}', {bstock},{bprice},'True');")
        db.commit()

    elif q == 'n':
        print('Okay.')
        cur.execute('select BookID from books2')
        existing_BID = (listcov(cur.fetchall()))
        # The same process
        while bid in existing_BID:
            print('Oops! There is already a Book in your store with this Book ID. Try a Different one')
            bid = stringnavigation('Enter BookID: ')
        # Getting Other details manually
        bname = stringnavigation('Enter Book Name: ')
        isbn = integernavigation('Enter ISBN: ')
        author = stringnavigation("Enter Author(s): ")
        category = stringnavigation('Enter Category: ')
        publisher = stringnavigation('Enter name of Publisher: ')
        pubdate = stringnavigation('Enter Date of Publication: ')
        bstock = integernavigation('Enter Total Stocks of the Book: ')
        bprice = integernavigation('Name your price for the book: ')
        cur.execute(f"insert into books2 values('{bid}','{bname}',{isbn},'{author}','{category}','{publisher}', '{pubdate}', {bstock},{bprice},'True');")
        db.commit()
    print('Book was Added Sucessfully')
    print('Redirecting you to local menu')
    time.sleep(3)
    os.system('cls')
    booksmenu()

def edit_book():
    menu = '''What do you want to do?
    1. Edit only Book ID, Stocks and Price
    2. Edit every details
'''
    q = integervaluecontrol([1,2], menu, "Uhuh. Choose only from the menu")
    if q == 1:
        cur.execute('select BookID from books2')
        existing_BID = (listcov(cur.fetchall()))
        bid = stringvaluecontrol(existing_BID,'Enter BookID: ', 'Book not found. Try another one.')
        cur.execute(f"select BookID,BookName,Stocks,Price from books2 where BookID = '{bid}'")
        data = (cur.fetchall())
        print("The Existing Record is:")
        print(data)
        print(tabulate(data, headers=["BookID", 'Book Name',"Stocks", "Price"], tablefmt='fancy_grid'))
        bstock = integernavigation('Enter Total Stocks of the Book: ')
        bprice = integernavigation('Name your price for the book: ')

        cur.execute(f"UPDATE books2 SET Price={bprice},Stocks={bstock} WHERE BookID='{bid}';")
        db.commit()

    if q == 2:
        cur.execute('select BookID from books2')
        existing_BID = (listcov(cur.fetchall()))
        bid = stringvaluecontrol(existing_BID, 'Enter BookID: ', 'Book not found. Try another one.')
        bname = stringnavigation('Enter Book Name: ')
        isbn = integernavigation('Enter ISBN: ')
        author = stringnavigation("Enter Author(s): ")
        category = stringnavigation('Enter Category: ')
        publisher = stringnavigation('Enter name of Publisher: ')
        pubdate = stringnavigation('Enter Date of Publication: ')
        bstock = integernavigation('Enter Total Stocks of the Book: ')
        bprice = integernavigation('Name your price for the book: ')
        cur.execute(f"UPDATE books2 SET Publisher='{publisher}',ISBN_ver='False',ISBN={isbn},BookName='{bname}',Author='{author}',Price={bprice},Category='{category}',Stocks={bstock},PubDate='{pubdate}' WHERE BookID = '{bid}';")
        db.commit()
    print('Okay. The Data was updated')
    print('Redirecting you to Home screen.....')
    time.sleep(3)
    os.system('cls')
    booksmenu()

def delete_book():
    cur.execute('select BookID from books2')
    existing_BID = (listcov(cur.fetchall()))
    bid = stringvaluecontrol(existing_BID, 'Enter BookID: ', 'Book not found. Try another one.')

    cur.execute(f"select BookID, BookName, ISBN, Author, Category, Publisher, PubDate, Stocks, Price from books2 where BookID = '{bid}'")
    bookDetails = cur.fetchall()

    print('Existing Record is: ')
    print(tabulate(bookDetails, headers=["BookID", "Book Name", "ISBN", "Author", 'Category', 'Publisher','Published Date', 'Stocks', 'Price'],
                   tablefmt='fancy_grid'))
    conf = stringvaluecontrol(['y', 'n'], 'Are you sure you want to delete that book? [y/n] ',"Oops! 'y' and 'n' are only valid responses. Try again")
    if conf == 'y':
        cur.execute(f"DELETE FROM books2 WHERE BookID='{bid}';")
        print('The Book was sucessfully deleted')
    else:
        print('Okay. That Guy was saved.')
    print('Redirecting you to Home screen.....')
    os.system('cls')
    booksmenu()

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
        cur.execute('select * from books2')
    elif selection == 2:
        cur.execute('select * from books2 order by Bookname')
    elif selection == 3:
        cur.execute('select * from books2 order by Bookname desc')
    elif selection == 4:
        cur.execute('select * from books2 order by Author')
    elif selection == 5:
        cur.execute('select * from books2 order by Author desc')
    data = cur.fetchall()
    print(tabulate(data, headers=["BookID", "Book Name", "ISBN", "Author", 'Published Year', 'Stocks', 'Price'], tablefmt='fancy_grid'))
    redirect = stringvaluecontrol(['y'], "Press y when you are ready to be redirected to the home screen: ","Only permitted value is 'y'!!")
    os.system('cls')
    booksmenu()


def booksmenu():
    print('What do you want to do with your books?')
    menustring = '''
    1. Add a book to the database
    2. Edit a Book in the Database
    3. Delete a Book in the database
    4. View your Books
    5. Go Back to the Main Menu of the whole program
'''
    q = integervaluecontrol([1,2,3,4], menustring, "Oops! Only choose from the menu!!")
    if q == 1:
        os.system('cls')
        add_book()
    elif q == 2:
        os.system('cls')
        edit_book()
    elif q == 3:
        os.system('cls')
        delete_book()
    elif q == 4:
        viewbooks()
    elif q == 5:
        from mainmenu import home
        home()
booksmenu()