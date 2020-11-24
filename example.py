'''import requests
from bs4 import BeautifulSoup
r_prog=requests.get("https://www.developer-tech.com/")
coverpage=r_prog.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all("h3")
links = []
for a in coverpage_news:
    x = a.find_all("a")
    for link in x:
        links.append("https://www.developer-tech.com/"+link.get("href"))
    if (len(links) >= 5):
        break
for i in links:
    print(i)'''#dev
# FOR ULTIMATE FUNCTION
'''
import requests 
from bs4 import BeautifulSoup

r_prog = requests.get("https://kiev.vgorode.ua/news/")
coverpage = r_prog.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all("div", class_="title")
links = []
for div in coverpage_news:
    a = div.find_all("a")
    for link in a:
        links.append(link.get("href"))
    if (len(links) >= 5):
        break
for i in links:
    print(i)'''
"""
import requests
from bs4 import BeautifulSoup

r_prog = requests.get("https://www.discovery.com/")
coverpage = r_prog.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all("h4")
links = []
for div in coverpage_news:
    a = div.find_all("a")
    for link in a:
        links.append(link.get("href"))
    if (len(links) >= 5):
        break
for i in links:
    print(i)"""
'''import requests
from bs4 import BeautifulSoup

r_prog = requests.get("https://www.bbc.com/news/topics/ce1qrvleleqt/artificial-intelligence")
coverpage = r_prog.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all("h3", class_="lx-stream-post__header-title gel-great-primer-bold")
links = []
for div in coverpage_news:
    a = div.find_all("a")
    for link in a:
        links.append("https://www.bbc.com/news/topics/ce1qrvleleqt/artificial-intelligence"+ link.get("href"))
    if (len(links) >= 5):
        break
for i in links:
    print(i)'''
'''
import requests
from bs4 import BeautifulSoup

r_prog = requests.get("http://art-news.com.ua/")
coverpage = r_prog.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all("h2")
links = []
for div in coverpage_news:
    a = div.find_all("a")
    for link in a:
        links.append(link.get("href"))
    if (len(links) >= 5):
        break
for i in links:
    print(i)'''
# FOR ULTIMATE FUNCTION

import requests
from bs4 import BeautifulSoup

r_prog = requests.get("https://www.internet-technologies.ru/articles/")
coverpage = r_prog.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all("div", class_="title")
links = []
for div in coverpage_news:
    a = div.find_all("a")
    for link in a:
        links.append(link.get("href"))
    if (len(links) >= 5):
        break
for i in links:
    print(i)


