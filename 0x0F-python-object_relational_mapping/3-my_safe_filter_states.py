#!/usr/bin/python3

"""  Here, we lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dev_conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    dev_cur = dev_conn.cursor()
    match = sys.argv[4]
    dev_cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = dev_cur.fetchall()
    for row in rows:
        print(row)
    dev_cur.close()
    dev_conn.close()
