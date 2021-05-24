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
import site2
import book

# extract html content from the main page
soup = site2.extract_html_content_from_url()

# extract category list urls
category_url = site2.category_list()

# for each category
for i in range(0, len(category_url)):
    soup = site2.extract_html_content_from_url(category_url[i])
    # how many pages on this category
    pages = site2.number_of_page(soup)
    # extract url of each
    url_pages = site2.extract_next_page_url(category_url[i], pages)
    url_pages.append(category_url[i])
    print(url_pages)






url_books = book.extract_urls()

def book_rating():
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
    return rating

# analyse data and save to tds
def find_data(soup, i):
    tds = []

    # rechercher tous les td (balises de cellules de tableau html)
    tda = soup.findAll("td")
    # url page
    url_books = book.extract_urls()
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
    tds.append(book_rating())

    # image
    image = soup.find("img")["src"]
    tds.append("http://books.toscrape.com" + image[5:])
    return tds, category

def save_to_csv(data, i, category):
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





def extract_category_data():
    url_books = book.extract_urls()

    # html request of the extracted urls
    for i in range (0,len(url_books)):
        # get html request
        response = requests.get(url_books[i])
        # if request is valid (code 200)
        if response.ok:
            # save html in soup and analyse it with lxml
            soup = BeautifulSoup(response.text, "lxml")
            tds, category = find_data(soup, i)
            save_to_csv(tds, i, category)


#number_of_page = number_of_page()

#if int(number_of_page) < 2:
 #   extract_category_data()

#else:
 #   for i in range(int(number_of_page)):
  #      print(i)
   #     url = extract_next_page_url().pop()
        # get html request
    #    response = requests.get(url)
        # if request is valid (code 200)
     #   if response.ok:
            # save html in soup and analyse it with lxml
      #      soup = BeautifulSoup(response.text, "lxml")
       #     extract_category_data()