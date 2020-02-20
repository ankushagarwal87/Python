import csv

actionDictionary={}
keyDictionary={}

'''
1. Read through mapping file to get all reload message statement , corresponding message name & key fields
2. Read through input file & pasre action message & key
3. Get corresponding message name from input file action text - If action not defined - skip that line
4. Write message name, key & dynamic value in file
5. Read this file in mapping
6. Lookup the key in Audit table to see if record alreay present in last 1 day - If present skip it
7. Another Source to read meassage sql
8. Join output file with source to get message sql
9. Replace dynamic value with key
10. Execute query & write payload to target file
'''

### Function to read Mapping file which map Action to Message & Key ###

def readMappingFile(mappingFile):
    with open(mappingFile, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            actionDictionary[row['Action']]=row['Name']
            keyDictionary[row['Name']]=row['Key']
        print(actionDictionary)

        
### Function to loop through data files ###
        
def readInputFile(fileName):
    pattern='Reload'
    with open(fileName, 'r') as csvfile:  
        csvreader = csv.reader(csvfile) 
        next(csvreader) 
        for row in csvreader:
            text = str(row)
            text = text.replace("'","")
            print(text)
            index = text.find(pattern)
            print(index)
            if(index != -1):
               data = text[index:len(text)-1]
               processReload(data)
               

### Function to process reload message ###
        
def processReload(data):
    dataSplitbyComma = data.split(',')
    print(dataSplitbyComma)
    if dataSplitbyComma[0] in actionDictionary.keys():
        actionName = actionDictionary[dataSplitbyComma[0]]
        output.write(actionName+"||"+keyDictionary[actionName]+"||"+dataSplitbyComma[1]+"\n")
    else:
        print('Reload action not defined in mapping : '+dataSplitbyComma[0])


fileName = "data.csv"
mappingFile = "mapping.csv"
output=open("Message2.txt",'w')
readMappingFile(mappingFile)
readInputFile(fileName)
output.close()
