#noti.py

# Importing necessary modules
import mysql.connector as mysql
from valuecontrol import *

# Function to display existing notifications
def notiview(db,cur):
    cur.execute('select * from notification where seenvar is not null')
    unseendata = cur.fetchall()
    for i in unseendata:
        print(i[0] + '   (NEW!)')
    cur.execute('select * from notification where seenvar is null')
    seendata = cur.fetchall()
    for i in seendata:
        print(i[0])

    cur.execute('UPDATE notification SET seenvar = null;')
    db.commit()
    print()
    conf = stringvaluecontrol(['y'], "Press 'y' when you are ready to go back to menu\n", "Uhuh. Only 'y' is allowed")
