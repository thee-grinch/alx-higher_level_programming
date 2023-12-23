#!/usr/bin/python3

import MySQLdb
import sys
"""this module uses mysqldb"""


us = sys.argv[1]
pas = sys.argv[2]
data = sys.argv[3]

db = MySQLdb.connect(host="127.0.0.1", port=3306, user=us, passwd=pas, db=data)

cursor = db.cursor()

sql_query = "SELECT * FROM states"

cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()
db.close()
