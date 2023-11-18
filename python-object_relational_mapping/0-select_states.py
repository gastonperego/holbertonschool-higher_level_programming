#!/usr/bin/python3
"""
    lists all states from the database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    table = cur.fetchall()
    for row in table:
        print(row)

