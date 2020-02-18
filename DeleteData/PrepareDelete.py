import cx_Oracle
from cx_Oracle import Error

tableList=[]
deleteList=[]
tableOrder=[]

def getTableColumns(table):
    query='SELECT COLUMN_NAME,COLUMN_ID FROM ALL_TAB_COLUMNS WHERE TABLE_NAME=:1 ORDER BY COLUMN_ID'
    cursor.execute(query,{'1':table})
    tableColumns=cursor.fetchall()       
    return tableColumns    
    
def getTableRows(table,column,value):
    query='SELECT * FROM '+table+' WHERE '+  column+' = :1'
    #print(query,table,column,value)
    cursor.execute(query,{'1':value})
    tableRows=cursor.fetchall()       
    return tableRows

def getTableConstraintsDownward(table):
    query='SELECT A.CONSTRAINT_NAME,B.TABLE_NAME,B.CONSTRAINT_NAME FROM ALL_CONSTRAINTS A,ALL_CONSTRAINTS B WHERE A.CONSTRAINT_NAME = B.R_CONSTRAINT_NAME \
        AND A.TABLE_NAME=:1 AND B.CONSTRAINT_TYPE=\'R\''
    cursor.execute(query,{'1':table})
    tableConstraints=cursor.fetchall()       
    return tableConstraints

def getTableConstraintsUpward(table):
    query='SELECT A.CONSTRAINT_NAME,A.TABLE_NAME,B.CONSTRAINT_NAME FROM ALL_CONSTRAINTS A,ALL_CONSTRAINTS B WHERE A.CONSTRAINT_NAME = B.R_CONSTRAINT_NAME \
        AND B.TABLE_NAME=:1 AND B.CONSTRAINT_TYPE=\'R\''
    cursor.execute(query,{'1':table})
    tableConstraints=cursor.fetchall()       
    return tableConstraints    
  
def prepareDeleteList(table,column,value):
    tableColumns = getTableColumns(table)
    tableRows = getTableRows(table,column,value)
    print(tableColumns)
    print(tableRows)

    tableList.append([table,column,value])
    if(table not in tableOrder):
        tableOrder.append(table)    
    deleteList.append('DELETE FROM '+table+' WHERE '+  column+' = \''+str(value)+'\';')
        
    tableConstraintsDownward = getTableConstraintsDownward(table)
    for constraint in tableConstraintsDownward:
        print(constraint)
        referenceColumn = constraint[0].split("_PK")[0]
        referenceTable = constraint[1]
        foreignColumn = constraint[2].split(referenceTable+"_")[1].split("_FK")[0]
        columnPosition = 0
        for column in tableColumns:
            if(referenceColumn == column[0]):
                columnPosition = column[1] - 1
        for row in tableRows:
            value = row[columnPosition]
            if(value is not None and [referenceTable,foreignColumn,value] not in tableList):
                tableList.append([referenceTable,foreignColumn,value])
                prepareDeleteList(referenceTable,foreignColumn,value)        
            else:
                print(str(referenceTable)+" "+str(foreignColumn)+" "+str(value)+' already added')
    
    '''
    tableConstraintsUpward = getTableConstraintsUpward(table)
    for constraint in tableConstraintsUpward:
        print(constraint)
        referenceColumn = constraint[0].split("_PK")[0]
        referenceTable = constraint[1]
        foreignColumn = constraint[2].split(table+"_")[1].split("_FK")[0]
        columnPosition = 0
        for column in tableColumns:
            if(foreignColumn == column[0]):
                columnPosition = column[1] - 1
        for row in tableRows:
            value = row[columnPosition]
            if(value is not None and [referenceTable,referenceColumn,value] not in tableList):
                tableList.append([referenceTable,referenceColumn,value])
                prepareDeleteList(referenceTable,referenceColumn,value)        
            else:
                print(str(referenceTable)+" "+str(referenceColumn)+" "+str(value)+' already added')
    '''

def PrepareDeleteFile():
    #for table in reversed(tableOrder):
    for statement in reversed(deleteList):
            #if(table+" " in statement):
        output.write(statement+"\n")
    


table = input('Enter Table name : ')
column = input('Enter Column name : ')
value = input('Enter Column Value : ')

#table='Employees'
output=open("DeleteForrr_"+table,'w')
connstr='scott/tiger'
try:
    conn = cx_Oracle.connect(connstr)
    cursor = conn.cursor()
    prepareDeleteList(table.upper(),column.upper(),value)
    #print(deleteList)
    #print(tableOrder)
    PrepareDeleteFile()
except Error as e:
    print(e)
finally:
    cursor.close()
    conn.close()
output.close()
