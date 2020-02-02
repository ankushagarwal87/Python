from xlrd import open_workbook

# Functions to extract column Name & Table Name from Sql Query

def extractColumn(query):
    column_list=[]
    table_list=[]
    alias_list=[]
    #print(query)
    queryUpperCase=query.upper()
    queryWithoutDuplicateSpace=' '.join(queryUpperCase.split())
    querySplitOnFrom=queryWithoutDuplicateSpace.split('FROM')
    querySplitOnComma=querySplitOnFrom[0].split(',')
    #print(querySplitOnComma)
    first_column=querySplitOnComma[0].split(' ')[1]
    #print(first_column.strip())
    column_list.append(first_column.strip())
    for i in querySplitOnComma[1:len(querySplitOnComma)]:
        #print(i.strip())
        column_list.append(i.strip())
    querySplitOnJoin=querySplitOnFrom[1].split('JOIN')
    #print(querySplitOnJoin)
    for i in querySplitOnJoin:
        data=i.strip()
        tableData=data.split(" ")
        table_list.append(tableData[0])
        alias_list.append(tableData[1])
    print(table_list)
    print(alias_list)
    return [table_list,alias_list,column_list]


def extractTable(query,column_list):
    table_list=[]
    alias_list=[]
    #print(query)
    queryUpperCase=query.upper()
    queryWithoutDuplicateSpace=' '.join(queryUpperCase.split())
    querySplitOnFrom=queryWithoutDuplicateSpace.split('FROM')
    querySplitOnJoin=querySplitOnFrom[1].split('JOIN')
    #print(querySplitOnJoin)
    for i in querySplitOnJoin:
        data=i.strip()
        tableData=data.split(" ")
        table_list.append(tableData[0])
        alias_list.append(tableData[1])
    print(table_list)
    print(alias_list)
    return [table_list,alias_list]


# Function to Loop over table list

def connectToDB(tableData):
    for tableName in tableData[0]:
        print (tableName)


# Function to flag if column required for mapping

def checkColumnNeeded(column,tableName,column_list,tableData):
    flag=0
    for presentColumn in column_list:
        if('.' in presentColumn):
            columnData=presentColumn.split(".")
            columnAlias=columnData[0]
            columnName=columnData[1]
            if(column.upper() ==columnName):
                try:
                    aliasindex=tableData[1].index(columnAlias)
                except ValueError:
                    continue
                else:
                    if(tableName.upper() ==tableData[0][aliasindex]):
                        print("Column Present in query")
                        flag=1
        else:
             if(presentColumn == column.upper()):
                 print("Column Present in query")
                 flag=1
    return flag


def getCompareColumn():
    compare_column1=[]
    compare_column2=[]
    wb = open_workbook('compare.xlsx')
    for s in wb.sheets():
        for row in range(s.nrows):
            compare_column1.append(s.cell(row,0).value.upper())
            compare_column2.append(s.cell(row,1).value.upper())
    print(compare_column1)
    print(compare_column2)

file=open("Sql Query",'r')
query=file.read()
masterData=extractColumn(query)
column_list=masterData[2]
table_list=masterData[0]
alias_list=masterData[1]
tableData=[table_list,alias_list]
print(column_list)
#tableData=extractTable(query,column_list)
print(tableData)
connectToDB(tableData)
print(checkColumnNeeded('rel_code','source.master_claim',column_list,tableData))
getCompareColumn()
