import requests
from bs4 import BeautifulSoup

req= requests.get("https://www.amazon.in/gp/bestsellers/books/")

soup = BeautifulSoup(req.content, "html.parser")



for books in soup.find_all('a',class_="a-link-normal"):

    for lists in books.find_all(class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"):
        print ("  ", lists.get_text())



# for lists in soup.find_all('div',class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"):
    # print(lists.get_text())


























