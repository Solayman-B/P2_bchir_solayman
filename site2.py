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

def category_list():
    category_url =[]
    a = soup.find("ul").find_next("ul").findAll("a")
    for i in range(1, 51):
        category_url.append("http://books.toscrape.com/" + a[i]["href"])
    return category_url

def number_of_page(soup):
    if soup.find("li", class_="current"):
        pages = (soup.find("li", class_="current").text[40:])
    else:
        pages = 1
    return int(pages)

def extract_next_page_url(url, pages):
    url_pages = []
    if pages > 1 :
        url_shortened = url.rstrip("index.html")
        for b in range(2, int(pages)+1):
            url_pages.append(url_shortened + "page-" + str(b) + ".html")
    return url_pages