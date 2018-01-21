#!/usr/bin/python
import cx_Oracle
from cx_Oracle import Error

def connectToOracle(data):
    connstr='scott/tiger'
    try:
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        for table in data:
                targetlist=[]
                query='Select owner,table_name,tablespace_name,cluster_name from all_tables where table_name=:1'
                cursor.execute(query,{'1':table.upper()})
                #print(cursor.statement)
                result=cursor.fetchall()
                #print(result)
                for row in result:
                    print("Table "+row[1]+" is present in tablespace "+row[2])
                    targetlist.append('Oracle')
                    targetlist.append(row[2])
                    targetlist.append(row[1])
                    query='SELECT DATA_TYPE,COLUMN_ID,COLUMN_NAME,DATA_LENGTH,DATA_SCALE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME=:1'
                    cursor.execute(query,{'1':table.upper()})
                    column_details=cursor.fetchall()
                    for column in column_details:
                        print(column)

    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()


connectToOracle(['REVIEW_WRHS'])
