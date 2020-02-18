import cx_Oracle
from cx_Oracle import Error

tableList=[]
insertList=[]
tableOrder=[]

def getTableColumns(table):
    query='SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME=:1 ORDER BY COLUMN_ID'
    cursor.execute(query,{'1':table})
    tableColumns=cursor.fetchall()       
    return tableColumns    
    
def getTableRows(table,column,value):
    query='SELECT * FROM '+table+' WHERE '+  column+' = :1'
    #print(query,table,column,value)
    cursor.execute(query,{'1':value})
    tableRows=cursor.fetchall()       
    return tableRows

def getTableConstraintsUpward(table):
    query='SELECT A.CONSTRAINT_NAME,A.TABLE_NAME,B.CONSTRAINT_NAME FROM ALL_CONSTRAINTS A,ALL_CONSTRAINTS B WHERE A.CONSTRAINT_NAME = B.R_CONSTRAINT_NAME \
        AND B.TABLE_NAME=:1 AND B.CONSTRAINT_TYPE=\'R\''
    cursor.execute(query,{'1':table})
    tableConstraints=cursor.fetchall()       
    return tableConstraints
  
def prepareInsertList(table,column,value):
    tableColumns = getTableColumns(table)
    columns=str(tuple([y for x in tableColumns for y in x]))
    columns = columns.replace("'","")
    tableRows = getTableRows(table,column,value)
    print(columns)
    print(tableRows)

    tableList.append([table,column,value])
    if(table not in tableOrder):
        tableOrder.append(table)

    insertPrefix="INSERT INTO "+table+" "+columns+" VALUES "
    for row in tableRows:
        query=insertPrefix+str(tuple(row))
        insertList.append(query)

    tableConstraintsUpward = getTableConstraintsUpward(table)
    for constraint in tableConstraintsUpward:
        print(constraint)
        referenceColumn = constraint[0].split("_PK")[0]
        referenceTable = constraint[1]
        foreignColumn = constraint[2].split(table+"_")[1].split("_FK")[0]
        columnPosition = 0
        for index,column in enumerate(tableColumns):
            if(foreignColumn == column[0]):
                columnPosition = index
        for row in tableRows:
            value = row[columnPosition]
            if(value is not None and [referenceTable,referenceColumn,value] not in tableList):
                tableList.append([referenceTable,referenceColumn,value])
                prepareInsertList(referenceTable,referenceColumn,value)        
            else:
                print(str(referenceTable)+" "+str(referenceColumn)+" "+str(value)+' already added')

def prepareInsertFile():
    #for table in reversed(tableOrder):
    for statement in reversed(insertList):
            #if(table+" " in statement):
        output.write(statement+"\n")

table = input('Enter Table name : ')
column = input('Enter Column name : ')
value = input('Enter Column Value : ')

output=open("InsertFor_"+table,'w')
connstr='scott/tiger'
try:
    conn = cx_Oracle.connect(connstr)
    cursor = conn.cursor()
    prepareInsertList(table.upper(),column.upper(),value)
    #print(insertList)
    #print(tableOrder)
    prepareInsertFile()
except Error as e:
    print(e)
finally:
    cursor.close()
    conn.close()
output.close()
