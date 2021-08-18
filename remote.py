import mysql.connector as mysql

# enter your server IP address/domain name
HOST = "libmgmt.heliohost.us" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "information_schema"
# this is the user you create
USER = "libmgmt"
# user password
PASSWORD = "nevermindmf"
# connect to MySQL server
db = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db.get_server_info())
cur = db.cursor()
cur.execute("show databases;")
print(cur.fetchall())
print('hello')