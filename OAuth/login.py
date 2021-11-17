
import time,random
import mysql.connector as mysql
from os import system, getcwd
import smtplib
from glogin_login import theoauth as glogin
from glogin_register import theoauth as gregister
import subprocess

# Database Connection
db = mysql.connect(host = 'localhost', username = 'root', password = 'nevermindmf', database = 'bstorev2')
cur = db.cursor()

menu = '''Hello There!
What do you want to do?
1. Login Normally
2. Login with Google
3. Register Normally
4. Register with Google
'''

def sendotp(tomail):

    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    otp = ''
    for i in range(6):
        otp += random.choice(chars)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("vnbookstoremgmtapp@gmail.com", "bookstore")
    message = f"""\
    Bookstore Management App


    Thankyou for Choosing our Appplication
    One-Time-Password to complete your registration process is: {otp}"""
    s.sendmail("vnbookstoremgmtapp@gmail.com", tomail, message)
    s.quit()

    return otp


def login():
    system('cls')
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    cur.execute(f'select password from credentials where password = "{password}"')
    out = cur.fetchall()
    if out == []:
        print('No Matching records found')
    else:
        print(out)
def register():
    system('cls')

    cur.execute('select username from credentials')
    usernames = cur.fetchall()

    cur.execute('select email from credentials')
    emails = cur.fetchall()

    email = input('Enter your mail address: ')
    while email in emails:
        print('Email Already exists. Try a new one/login')

    gen_otp = sendotp(email)
    verify_otp = input('Enter OTP sent to your mail: ')


    while verify_otp != gen_otp:
        print('OTP Incorrect. Please try again')
        verify_otp = input('Enter OTP sent to your mail: ')

    username = input('Enter username: ')
    while username in usernames:
        print('Username already exists!\nTry another.')
        username = input('Enter username: ')

    password = input('Enter Password: ')
    while password == '':
        print('Password cannot be left blank.')
        password = input('Enter Password: ')

    cur.execute(f"INSERT INTO credentials VALUES ('{email}','{username}','{password}','Normal');")
    db.commit()
    print('User was registered Sucessfully')


q = int(input(menu))
if q == 1:
    login()
elif q == 2:
    subprocess.call(['python', f"{getcwd()}\glogin_login.py"])
elif q == 3:
    register()
elif q == 4:
    gregister()

time.sleep(10)

