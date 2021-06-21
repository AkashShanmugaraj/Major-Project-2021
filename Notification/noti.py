import mysql.connector as mysql
db = mysql.connect(host='localhost', user = 'root', passwd = 'nevermindmf', database = 'bookstore')
cur = db.cursor()


def notiview():
    cur.execute('select * from notification where seenvar is not null')
    unseendata = cur.fetchall()
    print("Unseen Data: ")
    print(unseendata)
    cur.execute('select * from notification where seenvar is null')
    seendata = cur.fetchall()
    print("Seen Data: ")
    print(seendata)

    cur.execute('UPDATE notification SET seenvar = null;')
    db.commit()

q = int(input("Enter 1 to view notifications\n"))
if q == 1:
    notiview()
