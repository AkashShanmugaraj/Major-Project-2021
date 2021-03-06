#Importing required Modules
import urllib.request
import json

def tryexception(dict,key):
    try:
        return dict[key]
    except KeyError:
        return 'N/A'

def get_isbn():
    # The base api link is the link where everydata about a book will be present in a plain, dictionary like format
    # It will give details if we provide isbn number
    user_input = input("Enter ISBN: ").strip()
    api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+user_input

    # The urllib module is used to open the link and read those lines.
    with urllib.request.urlopen(api_link) as f:
        text = f.read() # Now, the lines read from the website will be in a binary form

    decoded_text = text.decode("utf-8") # for futher usage of the text, we need to convert it to normal file. The encoding type is called utf-8
    #json is a nested dictionary type file.
    bookdict = json.loads(decoded_text) # the json file is converted to python dictionary here
    #print(bookdict)
    bookinfo = bookdict['items'][0]['volumeInfo']
    #print(volume_info)
    print("\n\n")
    authors = tryexception(bookinfo,"authors")
    if authors != 'N/A':
        authors = ", ".join(authors)
    category = tryexception(bookinfo,"categories")
    if category != 'N/A':
        category = ", ".join(category)


    textpreset = f"""
    Bookname : {tryexception(bookinfo, 'title')}
    Author : {authors}
    Category : {category}
    Publisher : {tryexception(bookinfo,'publisher')}
    ISBN : {user_input}
    Date of Publication : {tryexception(bookinfo,'publishedDate')}\n
    Summary:
    {tryexception(bookinfo,'description')}\n
    Total Pages = {tryexception(bookinfo,'pageCount')}
    {tryexception(bookinfo,'averageRating')} out of 5 stars
    Reviewed by {tryexception(bookinfo,'ratingsCount')} people
    """

    print(textpreset)

def get_isbn_details(isbn):
    # The base api link is the link where everydata about a book will be present in a plain, dictionary like format
    # It will give details if we provide isbn number
    isbn = str(isbn)
    api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn

    # The urllib module is used to open the link and read those lines.
    with urllib.request.urlopen(api_link) as f:
        text = f.read() # Now, the lines read from the website will be in a binary form

    decoded_text = text.decode("utf-8") # for futher usage of the text, we need to convert it to normal file. The encoding type is called utf-8
    #json is a nested dictionary type file.
    bookdict = json.loads(decoded_text) # the json file is converted to python dictionary here
    #print(bookdict)
    bookinfo = bookdict['items'][0]['volumeInfo']
    #print(volume_info)
    print("\n\n")
    authors = tryexception(bookinfo,"authors")
    authors = ",".join(authors)
    category = tryexception(bookinfo,"categories")
    category = ",".join(category)


    outlist = [tryexception(bookinfo, 'title'),authors,category,tryexception(bookinfo,'publisher'),isbn,tryexception(bookinfo,'publishedDate'),tryexception(bookinfo,'description'),tryexception(bookinfo,'pageCount'),tryexception(bookinfo,'averageRating'),tryexception(bookinfo,'ratingsCount')]
    return outlist

get_isbn()