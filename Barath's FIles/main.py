import mysql.connector as mysql
from script import get_isbn_details
db = mysql.connect(host = 'libmgmt.heliohost.us', user = 'libmgmt', password = 'nevermindmf', database = 'libmgmt_bookstore')
cur = db.cursor()

def add_book():
    # Get ISBN
    # Print exisiting details from ISBN
    # Details from ISBN Author PubYear
    
    return

def edit_book():
    return

def delete_book():
    return
