# coding: utf-8
import os
from packages import site2, book

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
if os.path.isdir(book.path_jpg):
    pass
else:
    os.makedirs(book.path_jpg)

if os.path.isdir(book.path_csv):
    pass
else:
    os.makedirs(book.path_csv)
for i in range(0, len(book_url)):
    soup = site2.extract_html_content_from_url(book_url[i])
    info = book.find_data(soup, book_url, i)
    book.save_to_csv(info[0], info[1])
    book.save_image_to_jpg(info[2], info[3].replace(":", "")
                           .replace("/", "") + ".jpg")
