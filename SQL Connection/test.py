from tabulate import tabulate

def tabulating():
    rawdata = cursor.fetchall()
    listeddata = []
    for data in rawdata:
        listeddata.append(list(data))
    return listeddata


rawdata = cur.fetchall()
newdata = []
for data in rawdata:
    newdata.append(list(data))

print("The requested book is: ")
print(tabulate(booksdata, headers=["Book Name", "Price", 'Available Stocks'], tablefmt='fancy_grid'))
