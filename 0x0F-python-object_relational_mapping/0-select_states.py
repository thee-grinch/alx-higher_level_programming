#!/usr/bin/python3
""" this module uses mysqldb """
import MySQLdb
import sys

if __name__ == "__main__":
    us = sys.argv[1]
    pas = sys.argv[2]
    data = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=us, passwd=pas, db=data)
    cursor = db.cursor()
    sql_query = "SELECT * FROM states"
    cursor.execute(sql_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
