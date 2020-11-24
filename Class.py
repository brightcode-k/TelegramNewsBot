import requests
from bs4 import BeautifulSoup
class User():
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self. user_id = user_id
    def User(self, message):
        import telebot
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        id = message.from_user.id
        return first_name,last_name,id
class Site():
    def __init__(self, link, topic_programming, topic_art, topic_interesting, topic_music, topic_news):
        self.link = link
        self.topic_programming = topic_programming
        self.topic_art=topic_art
        self.topic_interesting=topic_interesting
        self.topic_music=topic_music
        self.topic_news=topic_news

class Article():
    def __init__(self, id, link, topic):
        self.id = id
        self.link = link
        self.topic = topic

def find_links_ultimate(site_url, site_valid, site_class, number_of_links):
    """
    This function parses site (finds particular amount of links) with current parameters
    :param site_url: url of site you want to parse
    :param site_valid: in html code 1 param
    :param site_class: in html code param class
    :param number_of_links: number of output links from particular sire
    :return: current number of links
    """
    r_prog = requests.get(site_url)
    coverpage = r_prog.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all(site_valid, class_=site_class)
    links = list()
    for div in coverpage_news:
        a = div.find_all("a")
        for link in a:
            links.append(link.get("href"))
        if (len(links) >= number_of_links):
            break
    return links

def developer_tech(number_of_urls):
    #programming
    r_prog = requests.get("https://www.developer-tech.com/")
    coverpage = r_prog.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all("h3")
    links = list()
    for a in coverpage_news:
        x = a.find_all("a")
        for link in x:
            links.append(link.get("href"))
        if (len(links) >= number_of_urls):
            break
    return links

def discovery(number_of_urls):
    #interesting
    r_prog = requests.get("https://www.discovery.com/")
    coverpage = r_prog.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all("h4")
    links = list()
    for div in coverpage_news:
        a = div.find_all("a")
        for link in a:
            links.append(link.get("href")[2:])
        if (len(links) >= number_of_urls):
            break
    return links

def BBC(number_of_urls):
    #ai
    r_prog = requests.get("https://www.bbc.com/news/topics/ce1qrvleleqt/artificial-intelligence")
    coverpage = r_prog.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all("h3", class_="lx-stream-post__header-title gel-great-primer-bold")
    links = list()
    for div in coverpage_news:
        a = div.find_all("a")
        for link in a:
            links.append("https://www.bbc.com/news/topics/ce1qrvleleqt/artificial-intelligence" + link.get("href"))
        if (len(links) >= number_of_urls):
            break
    return links

def art_news(number_of_urls):
    #art_news
    r_prog = requests.get("http://art-news.com.ua/")
    coverpage = r_prog.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all("h2")
    links = list()
    for div in coverpage_news:
        a = div.find_all("a")
        for link in a:
            links.append(link.get("href"))
        if (len(links) >= number_of_urls):
            break
    return links

def music_news(number_of_urls):
    r_prog = requests.get("http://rockmania.com.ua/novosti-rok-mira")
    coverpage = r_prog.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all("h3", class_="catItemTitle")
    links = list()
    for div in coverpage_news:
        a = div.find_all("a")
        for link in a:
            links.append("http://rockmania.com.ua/" + link.get("href"))
        if (len(links) >= number_of_urls):
            break
    return links

def Kyiv_news(number_of_urls):
    r_prog = requests.get("https://kiev.vgorode.ua/news/")
    coverpage = r_prog.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all("div", class_="title")
    links = list()
    for div in coverpage_news:
        a = div.find_all("a")
        for link in a:
            links.append(link.get("href"))
        if (len(links) >= number_of_urls):
            break
    return links
def internet_article(number_of_urls):
    r_prog = requests.get("https://www.internet-technologies.ru/articles/")
    coverpage = r_prog.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')
    coverpage_news = soup1.find_all("div", class_="title")
    links = []
    for div in coverpage_news:
        a = div.find_all("a")
        for link in a:
            links.append(link.get("href"))
        if (len(links) >= number_of_urls):
            break
    return links



