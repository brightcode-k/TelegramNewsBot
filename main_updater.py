import Class as parser
import SQL as db_handler


def update_discovery(topic, urls_number):
    db_handler.delete(topic)
    articles_discovery = parser.discovery(urls_number)
    for article in articles_discovery:
        db_handler.insert(article, topic)


def update_programing(topic, urls_number):
    db_handler.delete(topic)
    link = list()
    for rows1 in parser.developer_tech(urls_number):
        link.append("https://www.developer-tech.com/" + rows1)
    for rows2 in link:
        db_handler.insert(rows2, topic)


def update_artificial_intellegence(topic, urls_number):
    db_handler.delete(topic)
    articles_ai = parser.BBC(urls_number)
    for article in articles_ai:
        db_handler.insert(article, topic)


def update_art_news(topic, urls_number):
    db_handler.delete(topic)
    articles_art = parser.art_news(urls_number)
    for links in articles_art:
        db_handler.insert(links, topic)


def update_music_news(topic, urls_number):
    db_handler.delete(topic)
    articles_music = parser.music_news(urls_number)
    for links in articles_music:
        db_handler.insert(links, topic)


def update_Kyiv_news(topic, urls_number):
    db_handler.delete(topic)
    articles_Kyiv_news = parser.Kyiv_news(urls_number)
    for links in articles_Kyiv_news:
        db_handler.insert(links, topic)


def update_internet_article(topic, urls_number):
    db_handler.delete(topic)
    articles_internet = parser.internet_article(urls_number)
    for links in articles_internet:
        db_handler.insert(links, topic)




def get_sites(topic):
    sites = db_handler.get_sites_by_topic(topic)
    links = list()
    for site in sites:
        links.append(site.link)
    return links



update_discovery("discovery", 7)
update_programing("programing", 7)
update_artificial_intellegence("ai", 7)
update_art_news("art", 7)
update_music_news("music", 7)
update_Kyiv_news("Kyiv news", 7)
update_internet_article("some_articles_programming", 7)
