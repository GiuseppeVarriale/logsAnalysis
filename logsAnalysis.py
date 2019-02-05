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


if __name__ == "__main__":
    print(get_popular_articles())
    print(get_popular_authors())
