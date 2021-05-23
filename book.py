from site2 import soup

def extract_urls():
    url_books = []
    for url_book in soup.findAll("h3"):
        url_books.append("http://books.toscrape.com/catalogue" + str(url_book.a["href"])[8:])
    return url_books