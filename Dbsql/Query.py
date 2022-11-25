from datetime import datetime
import math
import codecs
import threading
import os
import asyncio
from databricks import sql



def send_query():
    query1 = 'SELECT count(*) FROM hive_metastore.dummydatadelta.web_sales'
    query2 = 'SELECT count(*) FROM hive_metastore.dummydatadelta.time_dim'
    queryList = [query1, query2]

    numberofbatch=1
    connection = sql.connect(
        server_hostname='.16.azuredatabricks.net',
        http_path='/sql/1.0/endpoints/',
        access_token='')
    for iteration in numberofbatch:
        print("Iteration-->"+str(iteration))
        cursor = connection.cursor()
        for i in queryList:
            cursor.execute(i)
            result = cursor.fetchall()
            for row in result:
                print(row)

    cursor.close()
    connection.close()


jobs = []
threads = 3
for i in range(0, threads):
    thread = threading.Thread(target=send_query)
    jobs.append(thread)

for j in jobs:
    j.start()

for j in jobs:
    j.join()

print("All jobs processing complete.")

