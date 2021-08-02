# Barath Giri's Workspace

## Hello Barath Giri!

This file is the medium of communication between us for the Major Project

You will find important work assigned to you and your TODO's below.

I will however post a message after a new work is assigned. 

This might be hard but this makes our work uniform and systematic.

## This week TODO's

#### Last Updated for August 2
You have to refer the _Google Books API_ folder in the root directory and from that you have to do some research on what and how a JSON works (it will be kindof easy for you since I have added some comments and created a base program) 

Go to the _.sql files_ folder. There take books database file, copy the text and paste it in the SQL commandline app.

With that set, go to the _SQL Connection_ floder in the root directory. There will be a file called _sqlcommands.py_. 
There take the editbooks() fuction as your refrence and create a new funciton for adding books such that:
- ISBN is obtained thru user input, and relevant details are extracted using google books API. So you should only get the BookID, Stocks and Price
- BookID is something which is for internal circulation (internally in the book store). So it is also inputted from the user
- Give a option to user like:
  - If ISBN number Available, enter ISBN and then enter BookID, Stocks, Price, set Status to Verified
  - If ISBN number not Available, get all details, put ISBN as 0 and Status as Not Verified

There maybe instances where every information might not be available in Google Books. 
In that case, use [try and except] (https://www.geeksforgeeks.org/python-try-except/) method and get the missing details from User
