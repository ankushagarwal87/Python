def convertDataType():
    mappingFile=open("mapping.csv",'r')
    mappingData=mappingFile.read()
    line=mappingData.split('\n')
    dataTypeDictionary={}
    for record in line:
        data=record.split(',')
        if(len(data[0])>0):
            dataTypeDictionary[data[0]]=data[1]
    for type1,type2 in dataTypeDictionary.items():
        print(type1,type2)

convertDataType()
