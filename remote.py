import mysql.connector as mysql

# enter your server IP address/domain name
HOST = "freedb.tech" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "freedbtech_mybookstorevnps"
# this is the user you create
USER = "freedbtech_vnpsmajorproject"
# user password
PASSWORD = "qwerty"
# connect to MySQL server
db = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db.get_server_info())
cur = db.cursor()
cur.execute("desc books;")
print(cur.fetchall())