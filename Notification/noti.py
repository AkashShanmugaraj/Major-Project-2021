import mysql.connector as mysql
import os
db = mysql.connect(host='localhost', user = 'root', passwd = 'nevermindmf', database = 'bookstore')
cur = db.cursor()


def notiview():
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



cur.execute('select * from notification where seenvar is not null')
unseendata = cur.fetchall()
totalunseen = len(unseendata)

menu = f'''What do you want to do?
1. Manage Books
2. Manage Employees
3. Manage Transactions
4. View Notifications ({totalunseen} new notifications)
5. View Profile
'''

q = int(input(menu))

if q == 4:
    os.system('cls')
    notiview()