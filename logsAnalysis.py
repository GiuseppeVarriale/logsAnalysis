#!/usr/bin/env python3

import psycopg2

# "Database code" for the DB news
DBNAME = "news"


def get_popular_articles():
    """Return the most popular three articles of all time,
    the most popular article at the top."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "select title, count(b.status) as views from articles as a, log as b\
        where b.path like '/article/' || a.slug and b.status = '200 OK'\
        group by title order by views desc limit 3"
    )
    popularArticles = c.fetchall()
    db.close()
    return popularArticles


def get_popular_authors():
    """Return the most popular article authors of all time, the most popular
     author at the top."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "select name, count(b.status) as views from articles as a, log as b, \
        authors as c where b.path like '/article/' || a.slug and \
        b.status = '200 OK' and c.id = a.author group by name \
        order by views desc"
    )
    popularAuthors = c.fetchall()
    db.close()
    return popularAuthors


if __name__ == "__main__":
    print(get_popular_articles())
    print(get_popular_authors())
