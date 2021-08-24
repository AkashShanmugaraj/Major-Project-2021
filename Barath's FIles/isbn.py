import urllib.request
import json
from valuecontrol import stringnavigation


def tryexception(dict,key):
    try:
        return dict[key]
    except KeyError:
        return 'N/A'


def get_isbn_details():
    isbn = stringnavigation('Enter ISBN: ')
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
        authors = tryexception(bookinfo, "authors")
        if authors == 'N/A':
            pass
        else:
            authors = ",".join(authors)
        category = tryexception(bookinfo, "categories")
        if category == 'N/A':
            pass
        else:
            category = ",".join(category)

        outlist = [tryexception(bookinfo, 'title'), authors, category, isbn,tryexception(bookinfo, 'publisher'),
                   tryexception(bookinfo, 'publishedDate')]
        return outlist
