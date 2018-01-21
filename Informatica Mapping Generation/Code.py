import requests
import jinja2
import os
import mysql.connector
import cx_Oracle
from bs4 import BeautifulSoup
from mysql.connector import Error
from cx_Oracle import Error



############Function to get description tag values from a website############## 

def getdata(link):
    #page = requests.get('https://issues.apache.org/jira/browse/HIVE-16998')
    page = requests.get(link)
    print(page)
    htmlContent = BeautifulSoup(page.content , "html.parser")
    description=htmlContent.find(id="description-val").get_text()
    return description 


############Function to extract possible table name words############## 

def extractTablename(data):
    words=data.split(" ")
    tablename=[]
    for word in words:
        if "_" in word:
            tablename.append(word)
    return tablename


############ Function to get informatice native data type ###########

dataTypeDictionary={}
def convertDataType():
    mappingFile=open("mapping.csv",'r')
    mappingData=mappingFile.read()
    line=mappingData.split('\n')
    for record in line:
        data=record.split(',')
        if(len(data[0])>0):
            dataTypeDictionary[data[0]]=data[1]
    #for type1,type2 in dataTypeDictionary.items():
        #print(type1,type2)


############Function to connect to Mysql##############

def connectToSource(data):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='INFORMATION_SCHEMA',
                                       user='root',
                                       password='sak###')
        if conn.is_connected():
            print('Connected to MySQL database')
            output=[]
            cursor = conn.cursor()
            for table in data:
                sourcelist=[]
                query=("SELECT table_schema,table_name FROM INFORMATION_SCHEMA.tables where table_name=%s")
                cursor.execute(query,(table,))
                results = cursor.fetchall()
                for row in results:
                    print("Souce Table "+row[1]+" is present in schema "+row[0])
                    sourcelist.append('MySql')
                    sourcelist.append(row[0])
                    sourcelist.append(row[1])
                    query=("Select DATA_TYPE,ORDINAL_POSITION,"+
                           "CASE WHEN COLUMN_KEY='PRI' THEN 'PRIMARY KEY' WHEN COLUMN_KEY='' THEN 'NOT A KEY' END,"+
                           "COALESCE(NUMERIC_PRECISION,DATETIME_PRECISION,0),COLUMN_NAME,"+
                           "CASE WHEN IS_NULLABLE='NO' THEN 'NOTNULL' WHEN IS_NULLABLE='YES' THEN 'NULL' END,"+
                           "COALESCE(NUMERIC_PRECISION,CHARACTER_MAXIMUM_LENGTH,DATETIME_PRECISION),COALESCE(NUMERIC_SCALE,0) from columns where table_name=%s")
                    cursor.execute(query,(row[1],))
                    column_details=cursor.fetchall()
                    #print(column_details)   
                    output.append([sourcelist,column_details])
                    break
            return output
                        
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()



############Function to connect to Oracle##############

def connectToTarget(data):
    connstr='scott/tiger'
    try:
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        output=[]
        for table in data:
                targetlist=[]
                query='Select owner,table_name,tablespace_name,cluster_name from all_tables where table_name=:1'
                cursor.execute(query,{'1':table.upper()})
                #print(cursor.statement)
                result=cursor.fetchall()
                #print(result)
                for row in result:
                    print("Target Table "+row[1]+" is present in tablespace "+row[2])
                    targetlist.append('Oracle')
                    targetlist.append(row[1])
                    query='SELECT DATA_TYPE,COLUMN_ID,COLUMN_NAME,DATA_LENGTH,DATA_SCALE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME=:1'
                    cursor.execute(query,{'1':table.upper()})
                    column_details=cursor.fetchall()
                    #print(column_details)
                    output.append([targetlist,column_details])
                    break
        return output

    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
        

############Function to render Xml##############

def worflow(sourcedata,targetdata):

    repository ={'name': 'RS_Dev', 'version': '182', 'codepage': 'MS1252', 'database':'Oracle'}
    folder ={'name': 'Ankush', 'group': '', 'owner': 'Administrator', 'shared':'NOTSHARED'}
    mapping ={'name': 'm_DYNAMIC_FILTER_VIA_PARAMETER'}
    session ={'SCHEDULERNAME':'Scheduler','SERVERNAME':'RS_IS','SERVER_DOMAINNAME':'Domain_950'}
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=os.getcwd()))
    template = env.get_template('workflow.XML')
    finalOutput = template.render(repository=repository,folder=folder,
                                  sourcedata=sourcedata,targetdata=targetdata,
                                  mapping=mapping,dataTypeDictionary=dataTypeDictionary,session=session)
    outFile = open('test5.xml',"w")
    outFile.write(finalOutput)
    outFile.close()

       

##########Main method#########
    
if __name__ == "__main__":
    #link=input("Enter website link : ")
    #data=getdata(link)
    #print(data)
    #tablename=extractTablename(data)
    convertDataType()
    sourcedata=connectToSource(['review','REVIEW_WRHS'])
    targetdata=connectToTarget(['review','REVIEW_WRHS'])
    worflow(sourcedata,targetdata)
