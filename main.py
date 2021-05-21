"""
-----------------------
virtualenv

source env/bin/activate

deactivate

----------------------

commandes git

git add fichier.extension

git status

git commit -m "modification apportée"

git push origin main

"""
#importer les paquets nécessaires
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import csv
import os

url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
while url != 0:
    def extract_html(url=url):
        # get html request
        response = requests.get(url)
        # if request is valid (code 200)
        if response.ok:
        # save html in soup and analyse it with lxml
            soup = BeautifulSoup(response.text, "lxml")
            return soup

    soup = extract_html()

    def extract_url_page():
        url_books = []
        for url_book in soup.findAll("h3"):
            url_books.append("http://books.toscrape.com/catalogue" + str(url_book.a["href"])[8:])
        return url_books

    url_books = extract_url_page()

    # analyse data and save to tds
    def find_data():

        tds = []

        # rechercher tous les td (balises de cellules de tableau html)
        tda = soup.findAll("td")

        # url page
        tds.append(url_books[i])
        # upc
        tds.append(tda[0].text)

        # title
        tds.append(soup.find("h1").text)

        price_including_tax = tda[2].text
        tds.append(price_including_tax[1:])

        price_excluding_tax = tda[3].text
        tds.append(price_excluding_tax[1:])

        number_available = tda[5].text
        tds.append(number_available[10:12])

        # description obtenue à partir de la balise id précédente
        if soup.find("div", id="product_description") == None:
            description = ""
        else:
            description = soup.find("div", id="product_description").find_next("p").text
        # remplacer ; par ";"
        tds.append(description.replace(";", ","))

        # catégorie du livre
        category = soup.find("li", class_="active").find_previous("a").text
        tds.append(category)

        # extraction de la note
        rating = soup.find("p", class_="star-rating")

        if "One" in str(rating):
            rating = "1/5"
        elif "Two" in str(rating):
            rating = "2/5"
        elif "Three" in str(rating):
            rating = "3/5"
        elif "Four" in str(rating):
            rating = "4/5"
        elif "Five" in str(rating):
            rating = "5/5"

        tds.append(rating)

        # image
        image = soup.find("img")["src"]
        tds.append("http://books.toscrape.com" + image[5:])
        return tds, category

    def save_to_csv(data, i):
        file_name = category + ".csv"
        if os.path.isfile(file_name):
            file = open(file_name, "a", newline="")
            writer = csv.writer(file)
        else:
            file = open(file_name, "w", newline="")
            writer = csv.writer(file)
            writer.writerow(["product_page_url; universal_ product_code (upc); title ; price_including_tax ; price_excluding_tax ; number_available ; product_description ; category ;review_rating ; image_url"])
        writer.writerow(data)
        file.close()

    # html request of the extracted urls
    for i in range (0,len(url_books)):
        soup = extract_html(url_books[i])
        tds, category = find_data()
        save_to_csv(tds, i)

    def extract_next_page_url(url):
    #extraire l'url de la page suivante s'il y en a une
        soup = extract_html()
        url_shortened = url.rstrip("index.html")
        if soup.find("li", class_="next"):
            url = url_shortened + soup.find("li", class_="next").a["href"]
        else:
            url = 0
        return url

    url = extract_next_page_url(url)