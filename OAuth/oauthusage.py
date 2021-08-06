from oauth import theoauth
import threading
import time
mydict = {}

def dictcheck():
    while mydict == {}:
        pass
    else:
        print("Google Login Sucessfull")
        print(f'Username: {mydict["name"]}\nEmail: {mydict["email"]}')

oauthprocess = threading.Thread(target=theoauth, args=(mydict,))
dictcheckprocess = threading.Thread(target=dictcheck)
dictcheckprocess.start()
oauthprocess.start()
