# P2_bchir_solayman

Summaries
---------

General description
Requirements
Installation
Run the script

General description
-------------

This script extract all the informations of each book from [books.toscrape.com](http://books.toscrape.com/index.html) and save them in csv files by category of book and the jpeg files in a folder.

Requirements
---------

This script uses the following paquets:

* beautifulsoup4==4.9.3
* bs4==0.0.1
* certifi==2020.12.5
* chardet==4.0.0
* idna==2.10
* lxml==4.6.3
* Pillow==8.2.0
* requests==2.25.1
* soupsieve==2.2.1
* urllib3==1.26.4


Installation
------------

First you can download this project by :

clicking on « code » then « download ZIP »
or [click here to download it directly](https://github.com/Solayman-B/P2_bchir_solayman.git)

Unzip the file when the download is completed

You can also install Git via this link and use :

    gh repo clone Solayman-B/P2_bchir_solayman


To use this script properly you need to use [python3](https://www.python.org/downloads/)

Then you can create a virtual environment:

    python3 -m venv env # env is the name of the directory but you can choose another one if you want

On Windows, run:

    env\Scripts\activate.bat

On Unix or MacOS, run:

    source env/bin/activate

You can install all the require paquets with:

    pip install -r requirements.txt

Run
---

Go to the root of the file with python3 and use `python3 main.py` to run the code
