#This custom module has some functions which are used for looping the input statements
import os


def stringvaluecontrol(listofpermitttedvalues, inputstatement, errormessage, homefunc = None):
    inputval = input(inputstatement)

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
            quit()
        else:
            inputval = int(inputval)
            return inputval

    except ValueError:
        print("Only integers (1,43,532) are allowed!")
        inputval = integernavigation(inputstatement, homefunc)
        return inputval