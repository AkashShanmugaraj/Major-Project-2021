# isbn.py

# Importing required modules
import urllib.request
import json
from valuecontrol import stringnavigation

# Function to fetch book details from Google Books Directory using API
def get_isbn_details(isbn):
    api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn
    with urllib.request.urlopen(api_link) as f:
        text = f.read()
    decoded_text = text.decode(
        "utf-8")
    bookdict = json.loads(decoded_text)
    while bookdict == {'kind': 'books#volumes', 'totalItems': 0}:
        print('\nOops. We couldnt find the book associated with that ISBN number. Try again')
        isbn = stringnavigation('Enter ISBN: ')
        api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn
        with urllib.request.urlopen(api_link) as f:
            text = f.read()
        decoded_text = text.decode(
            "utf-8")
        bookdict = json.loads(decoded_text)
    else:
        # print(bookdict)
        bookinfo = bookdict['items'][0]['volumeInfo']
        # print(volume_info)
        print("\n\n")
        authors = bookinfo.get('authors', 'N/A')
        if authors == 'N/A':
            pass
        else:
            authors = ",".join(authors)
        category = bookinfo.get('categories', 'N/A')
        if category == 'N/A':
            pass
        else:
            category = ",".join(category)

        outlist = [bookinfo.get('title', 'N/A'), authors, category, isbn,bookinfo.get('publisher', 'N/A'),
                   bookinfo.get('publishedDate', 'N/A')]
        return outlist
