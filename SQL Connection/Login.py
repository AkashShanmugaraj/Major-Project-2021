# This is the implementation of remote mysql and cmd_spin module
# An additional module names stdiomask must be installed. It helps us to give the **** effect while the password is entered
# The **** can be customised like XXXX or PPPP or anything

import mysql.connector as sql
import mysql.connector.errors
import stdiomask
from cmd_spin import spin

db = sql.connect(host='freedb.tech',database='freedbtech_mybookstorevnps',user='freedbtech_vnpsmajorproject', password='qwerty')
cur = db.cursor()

def login():
    uname = input("Enter Email: ")
    passwrd = stdiomask.getpass(prompt='Enter Password: ')
    cur.execute(f'select password, username from credentials where email = "{uname}"')
    d = cur.fetchall()
    if d != []:
        if d[0][0] == passwrd:
            print('Access gained')
            print(f"Hello {d[0][1]}")
    elif d == []:
        print("Email Not Found!")

def register():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    passwrd = stdiomask.getpass(prompt='Enter Password: ')
    try:
        cur.execute(f'''
        INSERT
        INTO
        credentials
        VALUES("{email}","{name}", "{passwrd}");''')
        db.commit()
        print("Now Try Logging in")
        login()
    except mysql.connector.errors.IntegrityError:
        print("Email/Username Already Exists")


ques = input("What would you like to do? \n\t1.Login\n\t2.Register\n")
if ques == '1':
    login()
elif ques == '2':
    register()
