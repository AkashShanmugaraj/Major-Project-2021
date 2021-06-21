import mysql.connector as mysql
import random
db = mysql.connect(host='localhost', database='bookstore', user='root', password='nevermindmf')
cur = db.cursor()
def tupletolist(thetuple):
    newlist = []
    for i in thetuple:
        for ii in i:
            newlist.append(ii)
    return newlist

def transidgen():
    cur.execute('select TransactionID from transactions')
    data = cur.fetchall()
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
print(transidgen())
