# Importing required modules
import time,random
import mysql.connector as mysql
from os import system, getcwd
import smtplib
from encrypt import *
import subprocess
from valuecontrol import *

# Database Connection
db = mysql.connect(host = 'localhost', user = 'root', password = 'nevermindmf', database = 'bstorev2')

cur = db.cursor()

cur.execute('select email from credentials')
def tupletolist(thetuple):
    newlist = []
    for i in thetuple:
        for ii in i:
            newlist.append(ii)
    return newlist
allemails = tupletolist(cur.fetchall())



# Function to send OTP
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


def login(hfunc):
    system('cls')
    print('Here')
    username = stringnavigation('Enter Username: ', homefunc= lambda: loginhome(hfunc))
    password = stringnavigation('Enter Password: ', homefunc= lambda: loginhome(hfunc))
    #username = input('Enter username: ')
    #password = input('Enter password: ')
    cur.execute(f'select password from credentials where username = "{username}"')
    out = cur.fetchall()
    if out == []:
        print('No Matching records found')
        login(hfunc)
    elif out[0][0] == password:
        print('Logged in')
        cur.execute(f'select name,email from credentials where username = "{username}"')
        data = cur.fetchall()
        savecred(username, data[0][0], data[0][1])

def login2(hfunc):
    system('cls')
def register(hfunc):
    system('cls')

    cur.execute('select username from credentials')
    usernames = cur.fetchall()

    cur.execute('select email from credentials')
    emails = cur.fetchall()

    email = stringnavigation('Enter your mail address: ', homefunc= lambda: loginhome(hfunc))
    while email in emails:
        print('Email Already exists. Try a new one/login')
        email = stringnavigation('Enter your mail address: ', homefunc= lambda: loginhome(hfunc))

    gen_otp = sendotp(email)
    verify_otp = stringnavigation('Enter OTP sent to your mail: ', homefunc= lambda: loginhome(hfunc))


    while verify_otp != gen_otp:
        print('OTP Incorrect. Please try again')
        verify_otp = stringnavigation('Enter OTP sent to your mail: ',homefunc= lambda: loginhome(hfunc))

    username = stringnavigation('Enter username: ', homefunc= lambda: loginhome(hfunc))
    while username in usernames:
        print('Username already exists!\nTry another.')
        username = stringnavigation('Enter username: ', homefunc= lambda: loginhome(hfunc))

    password = stringnavigation('Enter Password: ', homefunc= lambda: loginhome(hfunc))
    while password == '':
        print('Password cannot be left blank.')
        password = stringnavigation('Enter Password: ', homefunc= lambda: loginhome(hfunc))

    cur.execute(f"INSERT INTO credentials VALUES ('{email}','{username}','{password}','Normal');")
    db.commit()
    print('User was registered Sucessfully')


def loginhome(redirectfunc = None):
    menu = '''How would you want to login?
1. Login Normally
2. Login with Google
3. Register Normally
4. Register with Google
'''


    q = integervaluecontrol([1,2,3,4], menu, 'Uhuh. Only choose from the menu!')
    if q == 1:
        login(redirectfunc)
    elif q == 2:
        print('Please Give me a few seconds and check your browser')
        subprocess.call(['python', f"{getcwd()}\glogin_login.py"])
        cred = readcred()
        cur.execute(f'select medium from credentials where email = "{cred["email"]}"')
        out = cur.fetchall()

        if out == []:
            system('cls')
            print('Oops. Account not found')
            loginhome(redirectfunc)
        elif out[0][0] == 'Normal':
            system('cls')
            print('Oops. Seems like you have signed up with this account normally. Try logging in normally')
            loginhome(redirectfunc)
        elif out[0][0]:
            cur.execute(f'select username from credentials where email = "{cred["email"]}"')
            uname = cur.fetchall()
            existingcred = readcred()
            savecred(uname[0][0], existingcred['name'], existingcred['email'])

    elif q == 3:
        register(redirectfunc)
    elif q == 4:
        print('Please Give me a few seconds and check your browser')
        subprocess.call(['python', f"{getcwd()}\glogin_register.py"])
        cred = readcred()
        print(cred)
        if cred['email'] in allemails:
            system('cls')
            print('Oops. Already an Account is registered with that mail\nTry Logging in.')
            loginhome(redirectfunc)

        # Saving credentials to server
        cur.execute(f"INSERT INTO credentials(email, name, username, medium) VALUES('{cred['email']}', '{cred['name']}', '{cred['username']}', 'Google');")
        db.commit()

    redirectfunc()

