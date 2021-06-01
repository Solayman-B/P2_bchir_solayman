import requests
from bs4 import BeautifulSoup


def extract_html_content_from_url(url="http://books.toscrape.com/index.html"):
    # get html request
    response = requests.get(url)
    # if request is valid (code 200)
    if response.ok:
        # save html in soup and analyse it with lxml
        soup = BeautifulSoup(response.text, "lxml")
    return soup


soup = extract_html_content_from_url()


def category_list_url():
    category_url = []
    a = soup.find("ul").find_next("ul").findAll("a")
    for i in range(1, 51):
        category_url.append("http://books.toscrape.com/" + a[i]["href"])
    return category_url


def number_of_page(soup):
    if soup.find("li", class_="current"):
        pages = soup.find("li", class_="current").text[40:]
    else:
        pages = 1
    return int(pages)


def url_from_each_page(url):
    url_pages = []
    url_page = []
    # for each category
    for i in range(0, len(url)):
        soup = extract_html_content_from_url(url[i])
        # how many pages on this category
        pages = number_of_page(soup)
        # extract url of each page
        url_page.append(url[i])
        if pages > 1:
            url_shortened = url[i].rstrip("index.html")
            for b in range(2, int(pages) + 1):
                url_pages.append(url_shortened + "page-" + str(b) + ".html")
    url_pages += url_page
    return url_pages


book_url = []


def extract_book_url(soup):
    for book in soup.findAll("h3"):
        book_url.append("http://books.toscrape.com/catalogue"
                        + str(book.a["href"])[8:])
    return book_url
