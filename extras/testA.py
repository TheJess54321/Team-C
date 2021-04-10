import requests
from bs4 import BeautifulSoup

URL1 = "http://127.0.0.1:5000/"
URL2 = "http://127.0.0.1:1111/"

page1 = requests.get(URL1)
page2 = requests.get(URL2)

soup1 = BeautifulSoup(page1.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')