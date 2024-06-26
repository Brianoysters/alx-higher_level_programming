#!/usr/bin/python3
"""  code outputs all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    _input = db.cursor()
    _input.execute("SELECT * FROM states")
    rows = _input.fetchall()
    for row in rows:
        print(row)
    _input.close()
    db.close()
