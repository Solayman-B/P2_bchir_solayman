from site2 import soup
import os
import csv
import urllib.request

def book_rating(soup):
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
def find_data(soup, book_url, i):
    tds = []

    # rechercher tous les td (balises de cellules de tableau html)
    tda = soup.findAll("td")
    # url page
    tds.append(book_url[i])
    # upc
    tds.append(tda[0].text)

    # title
    title = soup.find("h1").text
    tds.append(title)

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
    tds.append(book_rating(soup))

    # image
    image = soup.find("img")["src"]
    image = "http://books.toscrape.com" + image[5:]
    tds.append(image)
    return tds, category, image, title

path = os.getcwd()
def save_to_csv(data, category):
    file_name = category + ".csv"
    if os.path.isfile(path + "/csv_files/" + file_name):
        file = open(path + "/csv_files/" + file_name, "a", newline="")
        writer = csv.writer(file)
    else:
        file = open(path + "/csv_files/" + file_name, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["product_page_url; universal_ product_code (upc); title; price_including_tax; price_excluding_tax; number_available; product_description; category;review_rating; image_url"])
    writer.writerow(data)
    file.close()

def save_image_to_jpg(image, title):
    LocalDestinationPath = path + "/jpg_files"
    os.chdir(LocalDestinationPath)
    urllib.request.urlretrieve(image, title)