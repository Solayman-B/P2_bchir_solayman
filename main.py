"""
-----------------------
virtualenv

source env/bin/activate

deactivate

----------------------

commandes git

git add fichier.extension

git commit -m "modification apportée"

git push origin main

"""
#importer les paquets nécessaires
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import csv
import os

#url de la categorie de livres
url_cat = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"

#effectuer une requette get html
response_cat = requests.get(url_cat)

#si la réponse est valide (code 200)
if response_cat.ok:
    #affecter le texte html de la page dans la variable soup_cat et analysé en utilisant lxml
    soup_books = BeautifulSoup(response_cat.text, "lxml")

    #extraire les urls des livres de la 1ere page de la catégorie
    url_books_tableau = []
    for url_books in soup_books.findAll("h3"):
        url_books = str(url_books)[21:]
        url_books = url_books.split('"', 1)
        for elem in [0,len(url_books)-1]:
            if elem % 2 == 0:
                url_books_tableau.append("http://books.toscrape.com/catalogue" + url_books[elem])

    print(url_books_tableau)


    """
    for i in (2,52):
        if i in url de category_list2:
            response_cati = request.get(url_cati)
            fonction scrap_thid_category 
            fonction scrap this book (en modifiant l'url de la page à scraper)
            
    """



    def scrap_this_book ():

        #url du site à scrapper
        url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

        #effectuer une requette get html
        response = requests.get(url)


        #si la réponse est valide (code 200)
        if response.ok:

            #affecter le texte html de la page dans la variable soup et analysé en utilisant lxml
            soup = BeautifulSoup(response.text, "lxml")

            #rechercher tous les td (balises de cellules de tableau html)
            tds = soup.findAll("td")

            upc = tds[0].text

            price_including_tax = tds[2].text
            price_including_tax = price_including_tax[1:]

            price_excluding_tax = tds[3].text
            price_excluding_tax = price_excluding_tax[1:]

            number_available = tds[5].text
            number_available = int(number_available[10:12])

            #recherche de la balise h1 contenant le titre du livre
            title = soup.find("h1")


            #recherche de la balise qui précède la notation (stock)
            stock = soup.find("p", class_="instock availability")

            #
            #extraction de la note
            rating = soup.find("p", class_="star-rating")

            if "One" in str(rating):
                rating = "one star"
            elif "Two" in str(rating):
                rating = "two stars"
            elif "Three" in str(rating):
                rating = "three stars"
            elif "For" in str(rating):
                rating = "for stars"
            elif "Five" in str(rating):
                rating = "five stars"

            #description obtenue à partir de la balise id précédente
            description = soup.find("div", id="product_description").find_next("p").text

            #image
            image = soup.find("img")["src"]
            image = "http://books.toscrape.com" + image[5:]

            #catégorie du livre
            category = soup.find("li", class_="active").find_previous("a").text

            #création du tableau avec les en-tetes
            tableau =[["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax",
                                                                    "price_excluding_tax", "number_available",
                                                                    "product_description", "category",
                                                                    "review_rating", "image_url"],
                      [url, upc, title.text, price_including_tax, price_excluding_tax, number_available,
                                                                    description, category, rating, image]]

            #création du fichier csv avec les éléments du tableau
            with open('books_to_scrape.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(tableau)

