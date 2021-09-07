# encrypt.py

# Importing required Modules
import cryptocode

# Function to save given credentials to credentials.dat file after encryption
def savecred(username = "None", fullname = "None", email = "None"):
    savefile = open('credentials.dat', 'w')

    tempdict = {"username": username, "name": fullname, "email": email}
    tempstring = str(tempdict)
    encoded = cryptocode.encrypt(tempstring,'lez')
    savefile.write(encoded)


# Function to read and decrypt data
def readcred():
    try:
        credfile = open('credentials.dat','r')
        data = credfile.read()
        decoded = cryptocode.decrypt(data, "lez")
        decodeddict = eval(decoded)
        return decodeddict
    except:
        return False
