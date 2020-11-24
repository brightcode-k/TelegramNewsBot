import sqlite3
import Class


def insert(link, topic):
    connection = sqlite3.connect("Sites.db")
    courser = connection.cursor()
    courser.execute("INSERT INTO Websites (Id, Url, Topic) VALUES(NULL, '" + link + "','" + topic + "')")
    connection.commit()
    connection.close()


def delete(topic):
    connection = sqlite3.connect("Sites.db")
    courser = connection.cursor()
    courser.execute("DELETE FROM Websites WHERE Topic = '" + topic + "'")
    connection.commit()
    connection.close()


def get_sites():
    connection = sqlite3.connect("Sites.db")
    courser = connection.cursor()
    courser.execute("SELECT * FROM Websites")
    raw_sites = courser.fetchall()
    articles = []
    for raw_site in raw_sites:
        site = Class.Article(raw_site[0], raw_site[1], raw_sites[2])
        articles.append(site)
    connection.commit()
    return articles


def get_sites_by_topic(topic):
    connection = sqlite3.connect("Sites.db")
    courser = connection.cursor()
    courser.execute("SELECT * FROM Websites WHERE Topic = '" + topic + "'")
    raw_sites = courser.fetchall()
    articles = []
    for raw_site in raw_sites:
        site = Class.Article(raw_site[0], raw_site[1], raw_sites[2])
        articles.append(site)
    connection.commit()
    return articles