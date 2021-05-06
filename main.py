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
    [print(str(td) + "\n\n") for td in tds]

    #recherche de la balise h1 contenant le titre du livre
    title = soup.find("h1")

    #recherche de la balise p avec l'attribut de class star rating correspondant à la notation du livre
    rating = soup.find("p", class_="star-rating")

    image = soup.find("img")

    #description = soup.find("article")
    #print(description)
    print(title.text, rating, image)



#       python3 main.py
