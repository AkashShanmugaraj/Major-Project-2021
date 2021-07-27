#Importing required Modules
import urllib.request
import json
import textwrap


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
    authors = bookinfo["authors"]
    authors = ",".join(authors)
    category = bookinfo["categories"]
    category = ",".join(category)

    textpreset = f"""
    Bookname : {bookinfo['title']}
    Author : {authors}
    Category : {category}
    Publisher : {bookinfo['publisher']}
    ISBN : {bookinfo['industryIdentifiers'][0]['identifier']}
    Date of Publication : {bookinfo['publishedDate']}\n
    Summary:
    {bookinfo['description']}\n
    Total Pages = {bookinfo['pageCount']}
    {bookinfo['averageRating']} out of 5 stars
    Reviewed by {bookinfo['ratingsCount']} people
    """
    print(textpreset)


get_isbn()