
# -*- coding: utf-8 -*-
import psycopg2
# 数据库连接参数
conn = psycopg2.connect(database="school", user="postgres", password="123456", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
# insert one item
cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (1, 'aaa'))
cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (2, 'bbb'))
cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (3, 'ccc'))

cur.execute("SELECT * FROM test;")
rows = cur.fetchall()        # all rows in table
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()