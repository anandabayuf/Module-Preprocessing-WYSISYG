# membuat modul preprocessing text untuk luaran WYSIWYG
# dengan menggunakan library bs4 atau BeautifulSoup4
# BeautifulSoup doc : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# sumber : https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string

# prerequisite :
# install bs4 to your python library using pip command 'pip install bs4' 'pip install lxml'

from bs4 import BeautifulSoup

def cleanHTMLTag(raw_html):
    cleantext = BeautifulSoup(raw_html, "lxml").text
    return cleantext
