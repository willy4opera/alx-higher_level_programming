#!/usr/bin/python3

""" Here, we listed all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    dev_conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3], port=3306)
    dev_cur = dev_conn.cursor()
    dev_cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = dev_cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    dev_cur.close()
    dev_conn.close()
