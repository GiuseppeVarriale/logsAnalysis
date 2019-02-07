#!/usr/bin/env python3

import psycopg2
# import only system from os
from os import system, name

# "Database code" for the DB news
DBNAME = "news"


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


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
    clear()
    print('------------------------------------------------------\n\n')
    print('The most popular three articles of all time are:\n')
    popular_articles = get_popular_articles()
    for article, views in popular_articles:
        print('"{} -> {} views"\n'.format(article, views))

    print('------------------------------------------------------\n\n')
    print('The most popular article authors of all time are:\n')
    popular_authors = get_popular_authors()
    for author, views in popular_authors:
        print('"{} -> {} views"\n'.format(author, views))

    print('------------------------------------------------------\n\n')
    print('The days did more than 1% of requests lead to errors are:\n ')
    high_errors_rate = get_high_errors_rate()
    if high_errors_rate:
        for day, percent in high_errors_rate:
            print('{} -> {} %\n'.format(day, percent))
    else:
        print('No day with more than 1% requests lead to errors')
    print('---------------------------END------------------------\n\n')
