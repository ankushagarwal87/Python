import pandas as pd
import cx_Oracle
from cx_Oracle import Error

actionDictionary={}
keyDictionary={}

'''
1. Read through mapping file to get all reload message statement , corresponding message name & key fields
2. Read through input file & pasre action message & key
3. Get corresponding message name from input file action text - If action not defined - skip that line
4. Check if audit table has entry in last 1 day - if present then skip that line
5. Get message sql by calling database with message name
6. Replace dynamic value with key field
7. Execute query & write payload message to file
'''

### Function to read Mapping file which map Action to Message & Key ###

def readMappingFile(mappingFile):
    df = pd.read_csv(mappingFile)
    for index, row in df.iterrows():
        actionDictionary[row['Action']]=row['Name']
        keyDictionary[row['Name']]=row['Key']


### Function to loop through data files ###
        
def readInputFile(fileName):
    df = pd.read_csv(fileName)
    for index, row in df.iterrows():
        print(row['ACTION_ITEM'])
        print(row['ACTION'])
        processReload(row['ACTION'],str(row['ACTION_ITEM']))


### Function to process reload message ###
        
def processReload(action,key):
    if action in actionDictionary.keys():
        actionName = actionDictionary[action]
        if(checkAudit(key)):
            print("Not older than 1 day")
        else:
            query = getQuery(actionName)
            print(query)
            if(query):
                queryUpdated = query.replace(keyDictionary[actionName],key)
                print(queryUpdated)
                message = getReloadMessage(queryUpdated)
                if(message):
                    output.write(str(message[0][0]))
                    print(message[0][0])
    else:
        print('Reload action not defined in mapping')


### Function to get message sql from Domian table based on message name ###
        
def getQuery(actionName):
    query='SELECT message_sql FROM message WHERE message_name=:1 '
    #print(query)
    cursor.execute(query,{'1':actionName})
    message_sql=cursor.fetchall()       
    return str(message_sql[0][0])   


### Function to fire message sql & get payload ###

def getReloadMessage(query):
    cursor.execute(query)
    message=cursor.fetchall()       
    return message


### Function to check if entry present in audit table ###

def checkAudit(key):
    query='SELECT log_id FROM LOGS WHERE log_id = :1 and log_time >= (SYSDATE-1) and log_time <= SYSDATE'
    cursor.execute(query,{'1':key})
    auditLogs=cursor.fetchall()       
    return auditLogs


fileName = "data.csv"
mappingFile = "mapping.csv"
output=open("Message",'w')
readMappingFile(mappingFile)
connstr='scott/tiger'
try:
    conn = cx_Oracle.connect(connstr)
    cursor = conn.cursor()
    readInputFile(fileName)
except Error as e:
    print(e)
finally:
    cursor.close()
    conn.close()
    output.close()


