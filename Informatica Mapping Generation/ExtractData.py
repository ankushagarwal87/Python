import AccessWebsite
from AccessWebsite import getdata

def extractTablename(data):
    words=data.split(" ")
    tablename=[]
    for word in words:
        if "_" in word:
            tablename.append(word)
    return tablename




if __name__ == "__main__":
    link=input("Enter website link : ")
    #link='https://issues.apache.org/jira/browse/SQOOP-3107'
    data=getdata(link)
    #print(data)
    tablename=extractTablename(data)
    #print("table list : ",tablename)
