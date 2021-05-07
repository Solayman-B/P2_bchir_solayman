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
   # [print(str(td) + "\n\n") for td in tds]

    #recherche de la balise h1 contenant le titre du livre
    title = soup.find("h1")

    #recherche de la balise qui précède la notation (stock)
    stock = soup.find("p", class_="instock availability")

    #
    #extraction de la note
    rating = soup.find("p", class_="star-rating")

    if "One" in str(rating):
        print("one")
    elif "Two" in str(rating):
        print("two")
    elif "Three" in str(rating):
        print("three")
    elif "For" in str(rating):
        print("for")
    elif "Five" in str(rating):
        print("five")

    #description
    description = soup.find("div", id="product_description").find_next("p")

    print("\n \n" + title.text + "\n \n", description.text + "\n \n")



"""       python3 main.py

one     3 E
two     3 W
three   5 5
for     3 O
five    4 4

"""