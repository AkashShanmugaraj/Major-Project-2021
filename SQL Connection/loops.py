#This custom module has some functions which are used for looping the input statements
#For example.....
#Consider that we need to get an input of the number of books required by the user
#CASE1 - If the user enters a non numerical character, then program will immediately quit.
#CASE2 - If he enters a number which is more than the books current stock, database will collapse
#There fore in order to prevent the above cases, we have two functions below

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
        return int(input(inputstatement))

    except ValueError:
        print("Only integers (1,43,532) are allowed!")
        return intsyntaxcheck(inputstatement)

def stringvaluecontrol(listofpermitttedvalues, inputstatement, errormessage):
    inputval = input(inputstatement)
    while inputval not in listofpermitttedvalues:
        print(errormessage)
        inputval = input(inputstatement)
    return inputval

def integervaluecontrol(listofpermitttedvalues, inputstatement, errormessage):
    try:
        inputval = int(input(inputstatement))
        while inputval not in listofpermitttedvalues:
            print(errormessage)
            inputval = int(input(inputstatement))
    except ValueError:
        print("Only integral values are allowed!")
        inputval = integervaluecontrol(permitttedvalues,inputstatement,errormessage)
    return inputval
#FUNCTION CALLING
'''print("Now the bookquantloop function is being called....")
bookquantloop(availablebooks=100)
print("\n\n")
print("Now the intsyntaxcheck function is being called....")
print(intsyntaxcheck("Your Custom Text: "))
stringinput = stringvaluecontrol(["Akash", "VNPS"], "Enter a string Value: ", "Only Akash and VNPS are Available!")
integerintput = integervaluecontrol([1,2,4], "Enter an integral Value: ", "Only 1,2 and 4 are Available!")
print(stringinput, integerintput)'''