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
        where b.path like '/article/' || a.slug and b.status similar to '2__%'\
        group by title order by views desc limit 3"
    )
    popular_articles = c.fetchall()
    db.close()
    return popular_articles


def get_popular_authors():
    """Return the most popular article authors of all time, the most popular
     author at the top."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "select name, count(b.status) as views from articles as a, log as b, \
        authors as c where b.path like '/article/' || a.slug and \
        b.status  similar to '2__%' and c.id = a.author group by name \
        order by views desc"
    )
    popular_authors = c.fetchall()
    db.close()
    return popular_authors


def get_high_errors_rate():
    """Return the days did more than 1% of requests lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        "select * from (select date(time),\
        round(100.0*sum(case log.status when '200 OK'\
        then 0 else 1 end)/count(log.status),2) as Error_Ratio from log\
        group by date(time) order by Error_Ratio desc) as ratios\
        where Error_Ratio > 1;"
    )
    high_errors_rate = c.fetchall()
    db.close()
    return high_errors_rate


if __name__ == "__main__":

    popular_articles = get_popular_articles()

    popular_authors = get_popular_authors()

    high_errors_rate = get_high_errors_rate()
