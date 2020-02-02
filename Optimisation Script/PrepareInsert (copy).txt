import os
import cx_Oracle
from cx_Oracle import Error

inputPath='/home/ankush/Github/Python/Optimisation Script/InsertQuery/Input'
outputPath='/home/ankush/Github/Python/Optimisation Script/InsertQuery/Output'

def readAllFiles():
    for (dirname, dirs, files) in os.walk(inputPath):
        for filename in files:
            print(filename)
            file=open(os.path.join(inputPath,filename),'r')
            output=open(os.path.join(outputPath,"InsertFor_"+filename),'w')
            inputQuery=file.read()
            prepareInsert(inputQuery,output)
            output.close()
            
def prepareInsert(query,output):
    queryUpperCase=query.upper()
    queryWithoutDuplicateSpace=' '.join(queryUpperCase.split())
    querySplit=queryWithoutDuplicateSpace.split('FROM')
    querySplitOnWhere=queryWithoutDuplicateSpace.split('WHERE')
    querySplitOnFrom=querySplitOnWhere[0].split('FROM')
    querySplitOnComma=querySplitOnFrom[1].split(',')
    #print(querySplitOnComma)
    for i in querySplitOnComma:
        data=i.strip()
        tableData=data.split(" ")
        singleTableQuery="SELECT "+tableData[1]+".* FROM "+querySplit[1]
        insertQuery=prepareInsertQuery(singleTableQuery,tableData[0])
        #print(insertQuery)
        insertQueryWithoutDuplicate=dict.fromkeys(insertQuery).keys()
        #print(insertQueryWithoutDuplicate)
        for data in insertQueryWithoutDuplicate:
            #print(data)
            output.write(data+";\n")


def prepareInsertQuery(singleTableQuery,table):
    #data=executeOracleQuery(singleTableQuery)
    #columns=str(tuple(getTableColumns(table)))
    columns=""
    insertPrefix="INSERT INTO "+table+columns+" VALUES "
    data=[[1,2,3,4],[5,6,7,8],[1,2,3,4]]
    insertQuery=[]
    for row in data:
        query=insertPrefix+str(tuple(row))
        insertQuery.append(query)
    return insertQuery

def executeOracleQuery(query):
    connstr='scott/tiger'
    try:
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        cursor.execute(query)
        row_details=cursor.fetchall()            
    except Error as e:
        print(e) 
    finally:
        cursor.close()
        conn.close()        
    return row_details
        
def getTableColumns(table):
    connstr='scott/tiger'
    try:
        conn = cx_Oracle.connect(connstr)
        cursor = conn.cursor()
        query='SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME=:1 ORDER BY COLUMN_ID'
        cursor.execute(query,{'1':table.upper()})
        column_details=cursor.fetchall()       
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return column_details

readAllFiles()
