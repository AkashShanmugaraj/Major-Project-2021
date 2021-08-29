import mysql.connector as mysql
import os
from valuecontrol import *


def notiview():
    db = mysql.connect(host='34.136.39.136', user='root', password='cN2zEh4g2PBxwiK7', database='bstore21')
    cur = db.cursor()
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
