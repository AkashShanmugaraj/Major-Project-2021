#This custom module has some functions which are used for looping the input statements
import os
import time
import pyfiglet

def quitprint():
    os.system('cls')
    print('Sorry to see you go...')
    print('This Application was developed by')
    print(pyfiglet.figlet_format("Someone", font = "taxi____" ))
    time.sleep(3)

def intsyntaxcheck(inputstatement, homefunc = None):

    try:
        a = input(inputstatement)
        if a in ['\\back', '\\home']:
            print('Exceptions Called')
        else:
            a = int(a)
            return a

    except ValueError:
        print("Only integers (1,43,532) are allowed!")
        a = intsyntaxcheck(inputstatement)
        return a
    
def bookquantloop(availablebooks):
    print(f"Note only {availablebooks} books are available")
    a = intsyntaxcheck("Enter Required Books: ")
    while a > availablebooks:
        print(f"Only {availablebooks} Books are available.")
        a = intsyntaxcheck("Enter Required Books: ")
    else:
        print(f"{a} book(s) were requested")
        return a


def stringvaluecontrol(listofpermitttedvalues, inputstatement, errormessage, homefunc = None):
    inputval = input(inputstatement)

    listofpermitttedvalues.extend(['\\home', '\\quit'])

    while inputval not in listofpermitttedvalues:
        print(errormessage)
        inputval = input(inputstatement)

    if inputval == '\\home':
        if homefunc == None:
            print('Navigation Commands are not permitted here.')
            val2 = stringvaluecontrol(listofpermitttedvalues, inputstatement, errormessage, homefunc)
            return val2
        else:
            os.system('cls')
            homefunc()
    elif inputval == '\\quit':
        quitprint()
        quit()
    else:
        return inputval

def integervaluecontrol(listofpermitttedvalues, inputstatement, errormessage, homefunc = None):
    strlist = []
    for i in listofpermitttedvalues:
        strlist.append(str(i))
    try:
        inputval = (input(inputstatement))
        if inputval == '\\home':
            if homefunc == None:
                print('Navigation Commands are not permitted here.')
                val2 = integervaluecontrol(listofpermitttedvalues, inputstatement, errormessage,homefunc)
                return val2
            else:
                os.system('cls')
                homefunc()

        elif inputval == '\\quit':
            quitprint()
            quit()
        else:
            inputval = int(inputval)
            while inputval not in listofpermitttedvalues:
                print(errormessage)
                inputval = integervaluecontrol(listofpermitttedvalues, inputstatement,errormessage)


    except ValueError:
        print("Only integral values are allowed!")
        inputval = integervaluecontrol(listofpermitttedvalues,inputstatement,errormessage)
    return inputval

def stringnavigation(inputstatement,homefunc = None):
    val = input(inputstatement)
    if val == '\\home':
        if homefunc == None:
            print('Navigation Commands are not permitted here.')
            val2 = stringnavigation(inputstatement, homefunc)
            return val2
        else:
            os.system('cls')
            homefunc()

    elif val == '\\quit':
        quitprint()
        quit()
    else:
        return val

def integernavigation(inputstatement,homefunc = None):
    try:
        inputval = input(inputstatement)
        if inputval == '\\home':
            if homefunc == None:
                print('Navigation Commands are not permitted here.')
                val2 = integernavigation(inputstatement, homefunc)
                return val2
            else:
                os.system('cls')
                homefunc()

        elif inputval == '\\quit':
            quitprint()
            quit()
        else:
            inputval = int(inputval)
            return inputval

    except ValueError:
        print("Only integers (1,43,532) are allowed!")
        inputval = integernavigation(inputstatement, homefunc)
        return inputval

