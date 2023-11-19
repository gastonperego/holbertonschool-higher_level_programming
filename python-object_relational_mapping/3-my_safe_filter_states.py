#!/usr/bin/python3
"""
    lists all states with a name starting with N (upper N) from the database
    hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (argv[4],))
    table = cur.fetchall()
    for row in table:
        print(row)
    cur.close()
    db.close()