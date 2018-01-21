import AccessWebsite
import ExtractData
import mysql.connector

from AccessWebsite import getdata
from ExtractData import extractTablename
from mysql.connector import Error

 
def connect(data):
    """ Connect to MySQL database """
    source=[]
    i=0;
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='INFORMATION_SCHEMA',
                                       user='root',
                                       password='sak###')
        if conn.is_connected():
            print('Connected to MySQL database')
            cursor = conn.cursor()
            for table in data:
                #print (table)
                query=("SELECT table_schema,table_name FROM INFORMATION_SCHEMA.tables where table_name=%s")
                cursor.execute(query,(table,))
                results = cursor.fetchall()
                source_dictionary={}
                #print(results)
                for row in results:
                    print("Table "+row[1]+" is present in schema "+row[0])
                    source_dictionary['DATABASETYPE']='MySql'
                    source_dictionary['DBDNAME']=row[0]
                    source_dictionary['NAME']=row[1]
                    source_dictionary['OWNERNAME']=row[0]
                    #print(source_dictionary)
                    query=("Select DATA_TYPE,ORDINAL_POSITION,"+
                           "CASE WHEN COLUMN_KEY='PRI' THEN 'PRIMARY KEY' WHEN COLUMN_KEY='' THEN 'NOT A KEY' END,"+
                           "COALESCE(NUMERIC_PRECISION,DATETIME_PRECISION,0),COLUMN_NAME,"+
                           "CASE WHEN IS_NULLABLE='NO' THEN 'NOTNULL' WHEN IS_NULLABLE='YES' THEN 'NULL' END,"+
                           "COALESCE(NUMERIC_PRECISION,CHARACTER_MAXIMUM_LENGTH,DATETIME_PRECISION),COALESCE(NUMERIC_SCALE,0) from columns where table_name=%s")
                    cursor.execute(query,(row[1],))
                    column_details=cursor.fetchall()
                    print(column_details)
                    print(column_details[0][0])
                    print(column_details[1][0])
                #cursor.execute("show tables")
                #for (table_name,) in cursor:
                    #if "user" in table_name:
                       #print (table_name)

 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 



if __name__ == '__main__':
    #link=input("Enter website link : ")
    #data=getdata(link)
    #tablename=extractTablename(data)
    #connect(tablename)
    connect(['review','reach'])
