
import json
import cryptocode


def savecred(username = "None", fullname = "None", email = "None"):
    savefile = open('credentials.dat', 'w')

    tempdict = {"username": username, "name": fullname, "email": email}
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
    except:
        return False
