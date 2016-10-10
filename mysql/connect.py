# -*- coding: utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    passwd = "root",
    db = "",
    charset = "utf8"
)

def Insert(data):
    cur = conn.cursor()
    cur.execute(" insert into YouTu_Data (%s,%s,%s) ",(1,2,3))
    cur.close()
    conn.commit()
    conn.close()
