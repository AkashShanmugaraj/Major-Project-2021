import os
import time

from encrypt import readcred
from login import loginhome
import mysql.connector as mysql
from valuecontrol import *
from noti import notiview
from managebooks import booksmenu
from managetransactions import transhome
from employee import emphome
import pyfiglet
from art import printart

# Establishing Connection
db = mysql.connect(host = '34.136.39.136', user = 'root', password = 'cN2zEh4g2PBxwiK7', database = 'bstore21')
cur = db.cursor()


# To find unread notifications
cur.execute('select * from notification where seenvar is not null')
unseendata = cur.fetchall()
totalunseen = len(unseendata)

def menuf():
    fname = readcred()['name']
    os.system('cls')
    print(pyfiglet.figlet_format(f"Welcome {fname}", font = "smscript" ))
    menu = f'''What do you want to do?
1. Manage Books
2. Manage Transactions
3. Manage Employees
4. View Notifications ({totalunseen} new notifications)
5. Logout of {fname}'s Account
6. Exit Application
'''

    q = integervaluecontrol([1,2,3,4,5,6],menu, 'Uhuh. Only Choose from the menu', homefunc=menuf)
    if q == 1:
        os.system('cls')
        booksmenu(db, cur,hfunc=menuf)
    elif q == 2:
        os.system('cls')
        transhome(db, cur, hfunc=menuf)
    elif q == 3:
        os.system('cls')
        emphome(db, cur,hfunc = menuf)
    elif q == 4:
        os.system('cls')
        notiview()
        menuf()
    elif q == 5:
        os.system('cls')
        os.remove('credentials.dat')
        print('You were sucessfully logged out!')
        loginhome(redirectfunc=menuf)
    elif q == 6:
        quitprint()
os.system('cls')
printart()
if readcred() == False:
    print('You have not logged in yet.')
    loginhome(menuf)

else:
    os.system('cls')
    print(pyfiglet.figlet_format(f"Book Store Management App", font="taxi____"))
    time.sleep(3)
    menuf()