# Importing required Modules
import os
import time
from isbn import get_isbn_details
import mysql.connector as mysql

from valuecontrol import *
from plot import plottable

# Connecting to the database
def listconv(inlist):
    sl = []
    for i in range(0,len(inlist)):
        sl.append(inlist[i][0])
    return sl

def add_book(database, cursor, homef):
    print('Adding a Book')
    # Getting details from Google Books API
    details = get_isbn_details()

    # Getting existing ISBN's in the database,
    cursor.execute('select ISBN from books2')
    existingIBSN = listconv(cursor.fetchall())

    # A while loop to ensure no Duplicate ISBN's are present

    while int(details[3]) in existingIBSN:
        os.system('cls')
        print('That ISBN is already there in your store. Try another one')
        details = get_isbn_details()

    # Converting it to a list
    tabulatingdetails = [details]
    # Printing it Tabulated
    plottable(tabulatingdetails,["Title", "Authors", "Category", "ISBN","Publisher", 'Published Date'], tablehead = 'Book Details from ISBN')

    q = stringvaluecontrol(['y','n'],'Are the above details correct? ', "Uhuh. Only choose from 'y' or 'n'", homefunc = lambda: booksmenu(database, cursor,homef))

    if q == 'y':
        cursor.execute('select BookID from books2')
        # Fetching Existing BookID's
        existing_BID = (listconv(cursor.fetchall()))
        bid = stringnavigation('Enter BookID: ', homefunc= lambda: booksmenu(database, cursor,homef))
        # Book ID is a Unique Key. Duplicates are not allowed. So we use the below while loop
        while bid in existing_BID:
            print('Oops! There is already a Book in your store with this Book ID. Try a Different one')
            bid = stringnavigation('Enter BookID: ', homefunc= lambda: booksmenu(database, cursor,homef))
        bstock = integernavigation('Enter Total Stocks of the Book: ', homefunc= lambda: booksmenu(database, cursor,homef))
        bprice = integernavigation('Name your price for the book: ', homefunc= lambda: booksmenu(database, cursor,homef))

        # Iserting Details
        cursor.execute(f"insert into books2 values('{bid}','{details[0]}',{details[3]},'{details[1]}','{details[2]}','{details[4]}', '{details[5]}', {bstock},{bprice},'True');")
        database.commit()

    elif q == 'n':
        print('Okay.')
        cursor.execute('select BookID from books2')
        existing_BID = (listconv(cursor.fetchall()))
        bid = stringnavigation('Enter BookID: ', homefunc= lambda: booksmenu(database, cursor,homef))
        # The same process
        while bid in existing_BID:
            print('Oops! There is already a Book in your store with this Book ID. Try a Different one')
            bid = stringnavigation('Enter BookID: ', homefunc= lambda: booksmenu(database, cursor,homef))
        # Getting Other details manually
        bname = stringnavigation('Enter Book Name: ', homefunc= lambda: booksmenu(database, cursor,homef))
        isbn = integernavigation('Enter ISBN: ', homefunc= lambda: booksmenu(database, cursor,homef))
        author = stringnavigation("Enter Author(s): ", homefunc= lambda: booksmenu(database, cursor,homef))
        category = stringnavigation('Enter Category: ', homefunc= lambda: booksmenu(database, cursor,homef))
        publisher = stringnavigation('Enter name of Publisher: ', homefunc= lambda: booksmenu(database, cursor,homef))
        pubdate = stringnavigation('Enter Date of Publication: ', homefunc= lambda: booksmenu(database, cursor,homef))
        bstock = integernavigation('Enter Total Stocks of the Book: ', homefunc= lambda: booksmenu(database, cursor,homef))
        bprice = integernavigation('Name your price for the book: ', homefunc= lambda: booksmenu(database, cursor,homef))
        cursor.execute(f"insert into books2 values('{bid}','{bname}',{isbn},'{author}','{category}','{publisher}', '{pubdate}', {bstock},{bprice},'False');")
        database.commit()
    print('Book was Added Sucessfully')
    print('Redirecting you to local menu')
    time.sleep(3)
    os.system('cls')
    booksmenu(database, cursor, homef)

def edit_book(database, cursor, homef):
    menu = '''What do you want to do?
    1. Edit only Book ID, Stocks and Price
    2. Edit every details
'''
    q = integervaluecontrol([1,2], menu, "Uhuh. Choose only from the menu", homefunc= lambda: booksmenu(database, cursor,homef))
    if q == 1:
        cursor.execute('select BookID from books2')
        existing_BID = (listconv(cursor.fetchall()))
        bid = stringvaluecontrol(existing_BID,'Enter BookID: ', 'Book not found. Try another one.', homefunc= lambda: booksmenu(database, cursor,homef))
        cursor.execute(f"select BookID,BookName,Stocks,Price from books2 where BookID = '{bid}'")
        data = (cursor.fetchall())
        print("The Existing Record is:")
        print(data)
        plottable(data, ["BookID", 'Book Name',"Stocks", "Price"], tablehead = 'Existing Book Detail from ISBN (for Modification of Details)')
        bstock = integernavigation('Enter Total Stocks of the Book: ', homefunc= lambda: booksmenu(database, cursor,homef))
        bprice = integernavigation('Name your price for the book: ', homefunc= lambda: booksmenu(database, cursor,homef))

        cursor.execute(f"UPDATE books2 SET Price={bprice},Stocks={bstock} WHERE BookID='{bid}';")
        database.commit()

    elif q == 2:
        cursor.execute('select BookID from books2')
        existing_BID = (listconv(cursor.fetchall()))
        bid = stringvaluecontrol(existing_BID, 'Enter BookID: ', 'Book not found. Try another one.', homefunc= lambda: booksmenu(database, cursor,homef))
        bname = stringnavigation('Enter Book Name: ', homefunc= lambda: booksmenu(database, cursor,homef))
        isbn = integernavigation('Enter ISBN: ', homefunc= lambda: booksmenu(database, cursor,homef))
        author = stringnavigation("Enter Author(s): ", homefunc= lambda: booksmenu(database, cursor,homef))
        category = stringnavigation('Enter Category: ', homefunc= lambda: booksmenu(database, cursor,homef))
        publisher = stringnavigation('Enter name of Publisher: ', homefunc= lambda: booksmenu(database, cursor,homef))
        pubdate = stringnavigation('Enter Date of Publication: ', homefunc= lambda: booksmenu(database, cursor,homef))
        bstock = integernavigation('Enter Total Stocks of the Book: ', homefunc= lambda: booksmenu(database, cursor,homef))
        bprice = integernavigation('Name your price for the book: ', homefunc= lambda: booksmenu(database, cursor,homef))
        cursor.execute(f"UPDATE books2 SET Publisher='{publisher}',ISBN_ver='False',ISBN={isbn},BookName='{bname}',Author='{author}',Price={bprice},Category='{category}',Stocks={bstock},PubDate='{pubdate}' WHERE BookID = '{bid}';")
        database.commit()
    print('Okay. The Data was updated')
    print('Redirecting you to Home screen.....')
    time.sleep(3)
    os.system('cls')
    booksmenu(database, cursor, homef)

def delete_book(database, cursor, homef):
    cursor.execute('select BookID from books2')
    existing_BID = (listconv(cursor.fetchall()))
    bid = stringvaluecontrol(existing_BID, 'Enter BookID: ', 'Book not found. Try another one.', homefunc= lambda: booksmenu(database, cursor,homef))

    cursor.execute(f"select BookID, BookName, ISBN, Author, Category, Publisher, PubDate, Stocks, Price from books2 where BookID = '{bid}'")
    bookDetails = cursor.fetchall()

    print('Existing Record is: ')

    plottable(bookDetails, ["BookID", "Book Name", "ISBN", "Author", 'Category', 'Publisher','Published Date', 'Stocks', 'Price'], tablehead='Existing Book Detail from ISBN (for Deletion of Details)')
    conf = stringvaluecontrol(['y', 'n'], 'Are you sure you want to delete that book? [y/n] ',"Oops! 'y' and 'n' are only valid responses. Try again")
    if conf == 'y':
        cursor.execute(f"DELETE FROM books2 WHERE BookID='{bid}';")
        database.commit()
        print('The Book was sucessfully deleted')
    else:
        print('Okay. That Guy was saved.')
    print('Redirecting you to Home screen.....')
    time.sleep(3)
    os.system('cls')
    booksmenu(database, cursor,homef)

def viewbooks(database, cursor, homef):
    menu2 = '''How do you want to have the data displayed?
    1. Just as it is
    2. Ordering Books Name in Ascending Order
    3. Ordering Books Name in Descending Order
    4. Ordering Author Name in Ascending Order
    5. Ordering Author Name in Descending Order
'''
    selection = integervaluecontrol([1,2,3,4,5], menu2, 'Choose only anyone of the following (1,2,3)!!', homefunc= lambda: booksmenu(database, cursor,homef))
    if selection == 1:
        cursor.execute('select * from books2')
    elif selection == 2:
        cursor.execute('select * from books2 order by Bookname')
    elif selection == 3:
        cursor.execute('select * from books2 order by Bookname desc')
    elif selection == 4:
        cursor.execute('select * from books2 order by Author')
    elif selection == 5:
        cursor.execute('select * from books2 order by Author desc')
    data = cursor.fetchall()
    plottable(data, ["BookID", "Book Name", "ISBN", "Author", "Category","Publisher",'Published Date', 'Stocks', 'Price', 'ISBN Verified'], tablehead = 'Existing List of Books')
    redirect = stringvaluecontrol(['y'], "Press y when you are ready to be redirected to the home screen: ","Only permitted value is 'y'!!", homefunc= lambda: booksmenu(database, cursor,homef))
    os.system('cls')
    booksmenu(database, cursor, homef)


def booksmenu(database, cursor, hfunc = None):

    print('The home function now is', hfunc)
    print('What do you want to do with your books?')
    menustring = '''
    1. Add a book to the database
    2. Edit a Book in the Database
    3. Delete a Book in the database
    4. View your Books
    5. Go Back to the Main Menu of the whole program
'''
    q = integervaluecontrol([1,2,3,4,5], menustring, "Oops! Only choose from the menu!!",homefunc=hfunc)
    if q == 1:
        os.system('cls')
        add_book(database, cursor, hfunc)
    elif q == 2:
        os.system('cls')
        edit_book(database, cursor, hfunc)
    elif q == 3:
        os.system('cls')
        delete_book(database, cursor,hfunc)
    elif q == 4:
        viewbooks(database, cursor, hfunc)
    elif q == 5:
        hfunc()
