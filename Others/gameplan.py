# This file was made with a total misconception. You may refer this but still every data might not e considered into the
# main program

'''
NOTE:
    >>> is an input line
There will be two versions of this software, Admin and Client

CLIENT~
==============PRESPECTIVE1START==============
In perspective of a new user,

A. He logins in using username-password or Google Login
B. He see's the following screen:

================SCREENSTART================
Welcome {name}!!
What would you like to do today?

1. Buy membership
2. Account Details
#TODO Think of adding Viewbooks here
>>>1

Showing you membership plans:
    1.------------
    2.------------
    3.------------

What plan are you interested in?
>>> 2
Great! You have opted for {planname} at {planprice}
Choose Checkout method:
    1. Online Transaction
    2. Pay-in-Store

<Despite having 2 methods of transaction, we will only code for Pay-in-Store>
<now assume that the customer has completed the transaction process>

Nice! Now you are redirected to mainscreen!

What would you like to do today?

1. Buy membership
2. Account Details
<Here until the Admin verfies Transaction, normal screen wont appear>

>>>2

Choose an Option:
    1.Name
    2.Address
    3.Phonenumber
    4.LibID

<Here, whichever option the user chooses (except 4)leads to the following screen>
>>>1

Your Registered name is {theirname}
Do you want to modify it? [y/n]
>>> y
Enter Newname: ________________
Change of name requested!

==============SCREENENDS==============

<The name changes only after Admin verifies>
<This applies even to options 2 and 3 (at line 46)>

==============PERSPECTIVE1ENDS==============

Now, in perspective of already registed , subscribed user

==============PERSPECTIVE2STARTS==============
Hello {username}!!
What would you like to do today?

1. Rent a book
2. Reserve a book
3. Return a book
4. Search for a book
5. View Membership
6. Account Details

'''