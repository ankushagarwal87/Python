import requests
import csv
import os
import datetime
from bs4 import BeautifulSoup
from urllib.parse import quote
import time

s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0'

startPageMoneyControl="https://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/index.html"
homeMoneyControl="https://www.moneycontrol.com"
TraderscockpitRSI="https://www.traderscockpit.com/?pageView=rsi-indicator-rsi-chart&type=rsi&symbol="
yahooPage="https://in.finance.yahoo.com/quote/"

columnName=['Company Name','Market Cap(in cr)','Company Link','Company Symbol','minimumPrice','minimumRSI','minimumPriceDate','currentPrice','currentRSI']
allData=[]
count=0
notifyData=[]

def getData(link):
    #print(link)
    time.sleep(1)
    try:
        page = s.get(link)
    except requests.exceptions.Timeout:
        print ("Timeout occurred")
    except:
        print(page)
    htmlContent = BeautifulSoup(page.content , "html.parser")
    return htmlContent

def readMasterFile(masterFile):
    count = 0
    try:
        with open(masterFile, 'r') as csvfile:
            print("Started reading the masterfile")
            csvreader = csv.DictReader(csvfile,fieldnames=columnName)
            next(csvreader)
            for row in csvreader:
                count = count + 1
                companySymbol = row['Company Symbol']
                companyLink = row['Company Link']
                rsiValue = 0.0
                sharePrice = 0.0
                sharePrice = getSharePrice(companyLink)
                if companySymbol != None and len(companySymbol)>0:
                    stockPage = TraderscockpitRSI+quote(companySymbol) 
                    rsiValue = getTraderscockpit(stockPage)
                row['currentPrice'] = sharePrice
                row['currentRSI'] = rsiValue
                comparePrice(row,rsiValue,sharePrice)
                allData.append(row)
                
                if(count % 5 == 0):
                    print("Number of stocks visited so far : ",count)
                #break
    except:
        print("error in reading csv")
    print("End reading")

def getSharePrice(stockPage):
    htmlContent = getData(stockPage)
    dataTable = htmlContent.find('span',{'class':'nse_span_price_wrap'}).text.strip(' ')
    return float(dataTable)

def getTraderscockpit(stockPage):
    htmlContent = getData(stockPage)
    dataTable = htmlContent.find('tr',{'class':'odd'})
    if dataTable != None:
        dataValue = float(dataTable.findAll('td')[2].text)
        return dataValue
    return 0

def comparePrice(data,rsiValue,sharePrice):
    if(sharePrice < float(data['minimumPrice']) and rsiValue > float(data['minimumRSI'])):
        data['minimumPrice'] = sharePrice
        data['minimumRSI'] = rsiValue
        currentDate = datetime.datetime.now().strftime('%Y-%m-%d')
        data['minimumPriceDate'] = currentDate
        notifyData.append(data)

def writeDictToCSV(prefix,newlist):
    #suffix = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    suffix = ""
    csv_file = os.getcwd() + "/" + prefix + suffix + ".csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columnName)
        writer.writeheader()
        for data in newlist:
            writer.writerow(data)

print("Start Time: ",datetime.datetime.now())
#masterFile = input("Enter MasterFile name : ")
masterFile="MasterFile1028.csv"
readMasterFile(masterFile)
newlist = sorted(allData, key=lambda k: float(k['Market Cap(in cr)']),reverse = True)
writeDictToCSV('MasterFile1028',newlist)
newlist = sorted(notifyData, key=lambda k: float(k['Market Cap(in cr)']),reverse = True)
writeDictToCSV('notifyData1028',newlist)
print("End Time: ",datetime.datetime.now())
