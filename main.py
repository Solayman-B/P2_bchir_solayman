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

tds = ["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]

#url de la categorie de livres
url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

#effectuer une requette get html
response = requests.get(url)
#si la réponse est valide (code 200)
if response.ok:
#affecter le texte html de la page dans la variable soup et analysé en utilisant lxml
    soup = BeautifulSoup(response.text, "lxml")

#extraire les urls des livres de la 1ere page de la catégorie
url_books = []
for url_book in soup.findAll("h3"):
    url_books.append("http://books.toscrape.com/catalogue" + str(url_book.a["href"])[8:])

#effectuer une requette get html
for i in range (0,len(url_books)-1):
    response = requests.get(url_books[i])

    #si la réponse est valide (code 200)
    if response.ok:

        #affecter le texte html de la page dans la variable soup et analysé en utilisant lxml
        soup = BeautifulSoup(response.text, "lxml")

        #rechercher tous les td (balises de cellules de tableau html)
        tda = soup.findAll("td")

        tds.append(url_books[i])

        tds.append(tda[0].text)

        # recherche de la balise h1 contenant le titre du livre
        tds.append(soup.find("h1").text)

        price_including_tax = tda[2].text
        tds.append(price_including_tax[1:])

        price_excluding_tax = tda[3].text
        tds.append(price_excluding_tax[1:])

        number_available = tda[5].text
        tds.append(int(number_available[10:12]))

        #description obtenue à partir de la balise id précédente
        tds.append(soup.find("div", id="product_description").find_next("p").text)

        #catégorie du livre
        tds.append(soup.find("li", class_="active").find_previous("a").text)

        #recherche de la balise qui précède la notation (stock)
        #stock = soup.find("p", class_="instock availability")

        #extraction de la note
        rating = soup.find("p", class_="star-rating")

        if "One" in str(rating):
            rating = "one star"
        elif "Two" in str(rating):
            rating = "two stars"
        elif "Three" in str(rating):
            rating = "three stars"
        elif "Four" in str(rating):
            rating = "four stars"
        elif "Five" in str(rating):
            rating = "five stars"

        tds.append(rating)

        #image
        image = soup.find("img")["src"]
        tds.append("http://books.toscrape.com" + image[5:])



        #création du fichier csv avec les éléments du tableau
        #with open("books_to_scrape.csv", "w", newline="") as f:
            #writer = csv.writer(f)
            #writer.writerows(tableau)

print(tds)


#extraire l'url de la page suivante s'il y en a une
#url_shortened = url.rstrip("index.html")
#if soup.find("li", attrs={'class': "next"}) != None:
    #next_page = url_shortened + soup.find("li", attrs={'class': "next"}).a["href"]