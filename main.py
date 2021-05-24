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
import site2
import book

# extract html content from the main page
site2.extract_html_content_from_url()

# extract category list urls
category_url = site2.category_list_url()
url_pages = site2.url_from_each_page(category_url)

# extract html content for each page
for i in range(0, len(url_pages)):
    soup = site2.extract_html_content_from_url(url_pages[i])
    # extract book url from the html
    book_url = site2.extract_book_url(soup)

# extract informations for each book
for i in range(0, len(book_url)):
    soup = site2.extract_html_content_from_url(book_url[i])
    info = book.find_data(soup, book_url, i)
    book.save_to_csv(info[0], info[1])





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