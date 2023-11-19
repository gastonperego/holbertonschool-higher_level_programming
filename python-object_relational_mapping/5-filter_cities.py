#!/usr/bin/python3
"""
     takes in the name of a state as an argument and lists all cities of that
     state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    query = """
                SELECT cities.name
                FROM cities
                WHERE cities.state_id =
                (SELECT id FROM states WHERE name=%s)
                ORDER BY cities.id ASC"""
    cur.execute(query, (argv[4],))
    table = cur.fetchall()

    prints = []
    for row in table:
        prints.append(row[0])

    print(*prints, sep=", ")
    cur.close()
    db.close()
