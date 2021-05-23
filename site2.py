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
    category =[]
    a = soup.find("ul").find_next("ul").findAll("a")
    for i in range(1, 51):
        category.append("http://books.toscrape.com/" + a[i]["href"])
    return category

def number_of_page(soup):
    soup = soup
    if soup.find("li", class_="current"):
        number_of_page = (soup.find("li", class_="current").text[40:])
    else:
        number_of_page = 1

    return number_of_page