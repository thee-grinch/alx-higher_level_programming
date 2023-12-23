import MySQLdb
import sys


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

db = MySQLdb.connect(host="127.0.0.1", port=3306, user=username, passwd=password, db=database)

cursor = db.cursor()

sql_query = "SELECT * FROM states"

cursor.execute(sql_query)
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.close()
db.close()
