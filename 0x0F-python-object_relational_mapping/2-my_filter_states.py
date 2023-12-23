#!/usr/bin/python3
""" this module uses mysqldb  and filters """
import MySQLdb
import sys

if __name__ == "__main__":
    us = sys.argv[1]
    pas = sys.argv[2]
    data = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=us, passwd=pas, db=data)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states
                   WHERE name LIKE BINARY '{}'".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
