from cryptography.fernet import Fernet
import json
import cryptocode

key = Fernet.generate_key()
fernet = Fernet(key)


def savecred(username, fullname):
    savefile = open('credentials.dat', 'w')

    tempdict = {"username": username, "name": fullname}
    tempstring = str(tempdict)
    encoded = cryptocode.encrypt(tempstring,'lez')
    savefile.write(encoded)



def readcred():
    try:
        credfile = open('credentials.dat','r')
        data = credfile.read()
        decoded = cryptocode.decrypt(data, "lez")
        decoded = decoded.replace("'", "\"")

        decodeddict = json.loads(decoded)
        return decodeddict
    except FileNotFoundError:
        return False
print(readcred())