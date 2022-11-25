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
        server_hostname='adb-3444365482071356.16.azuredatabricks.net',
        http_path='/sql/1.0/endpoints/c99ec7169d9dcabf',
        access_token='dapi1a7e6a5de54b65765e0593d25cbf9afc-3')
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

