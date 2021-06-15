import mysql.connector as mysql
db = mysql.connect(host='localhost', database='bookstore', user='root', password='nevermindmf')
cur = db.cursor()

cur.execute("select BookID from books;")
data = cur.fetchall()
print(data)

def tupletolist(thetuple):
    newlist = []
    for i in thetuple:
        for ii in i:
            newlist.append(ii)
    return newlist

new = tupletolist(data)
print(new)