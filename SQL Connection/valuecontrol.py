#This custom module has some functions which are used for looping the input statements
#For example.....
#Consider that we need to get an input of the number of books required by the user
#CASE1 - If the user enters a non numerical character, then program will immediately quit.
#CASE2 - If he enters a number which is more than the books current stock, database will collapse
#There fore in order to prevent the above cases, we have two functions below
import os
#Function for controlling what goes into the bookquantity feild
#This function will act as a solution for both problem cases.
def bookquantloop(availablebooks):
    print(f"Note only {availablebooks} books are available")
    a = intsyntaxcheck("Enter Required Books: ")
    while a > availablebooks:
        print(f"Only {availablebooks} Books are available.")
        a = intsyntaxcheck("Enter Required Books: ")
    else:
        print(f"{a} book(s) were requested")
        return a

#Functions for Syntax Check
#This function acts only as a syntax checker for integer datatype
def intsyntaxcheck(inputstatement):

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