#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=argv[1], passswd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.excecute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cur:
        print(row)