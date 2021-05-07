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

    #imprimer les td
    [print("\n" + td.text + "\n") for td in tds]

    #recherche de la balise h1 contenant le titre du livre
    title = soup.find("h1")

    #recherche de la balise qui précède la notation (stock)
    stock = soup.find("p", class_="instock availability")

    #
    #extraction de la note
    rating = soup.find("p", class_="star-rating")

    if "One" in str(rating):
        rating = "one"
    elif "Two" in str(rating):
        rating = "two"
    elif "Three" in str(rating):
        rating = "three"
    elif "For" in str(rating):
        rating = "for"
    elif "Five" in str(rating):
        rating = "five"

    #description obtenue à partir de la balise id précédente
    description = soup.find("div", id="product_description").find_next("p")

    #image
    image = soup.find("img")

    #url de la page
    #http: // books.toscrape.com + href - review/

    #url = soup.find("a", id="write_review").p
    #print(soup)

    #catégorie du livre

    category = soup.find("li", class_="active").find_previous("a").text


    print("\n \n" + title.text + "\n \n", description.text + "\n \n", image, "\n \n" + rating + "\n \n", category)



"""       python3 main.py


"""