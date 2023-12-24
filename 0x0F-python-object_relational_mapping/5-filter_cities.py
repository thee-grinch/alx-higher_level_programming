#!/usr/bin/python3

""" Lists all cities """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                   cities INNER JOIN states on states.id=cities.state_id
                   WHERE states.name = %s ORDER BY cities.id""", (sys.argv[4],))
    rows = cursor.fetchall()
    output = ""
    for row in rows:
        output += ", ".join(map(str, row[1]))
    print(output)
    cursor.close()
    db.close()
