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

def getAllData():
    htmlContent = getData(startPageMoneyControl)
    contentWithTags = htmlContent.findAll('a', {'class': 'opt_notselected'})
    for contentWithTag in contentWithTags:
        #print('Sector Link - ',contentWithTag.attrs['href'])
        sectorLink=homeMoneyControl+contentWithTag.attrs['href'] 
        getSectorData(sectorLink)
        #break

def getSectorData(sectorLink):
    global count
    htmlContent = getData(sectorLink)
    stockPriceWithTags = htmlContent.findAll('td', {'class': 'brdrgtgry'})    
    contentWithTags = htmlContent.findAll('a', {'class': 'bl_12'})
    k=5
    for contentWithTag in contentWithTags[2:]:
        companyName = contentWithTag.text
        marketCap = float(stockPriceWithTags[k].text.replace(',',''))
        if(marketCap < marketCapThreshold):
            break
        companyLink=homeMoneyControl+contentWithTag.attrs['href']
        getCompanyData(companyName,companyLink,marketCap)
        k=k+6
        count=count+1        
    print('Number of stocks visited so far : ',count)          
        
def getCompanyData(companyName,companyLink,marketCap):
    masterData={}
    masterData['Company Name'] = companyName.replace(',','').replace(';','')
    masterData['Market Cap(in cr)'] = marketCap
    masterData['Company Link'] = companyLink
    masterData['minimumRSI'] = 0
    masterData['currentRSI'] = 0
    htmlContent = getData(masterData['Company Link'])
    #print(htmlContent.find('p',{'class':'bsns_pcst'}).text.split('|')[1].split(':')[1].strip(' ').replace(',','').replace(';',''))
    masterData['Company Symbol'] = htmlContent.find('p',{'class':'bsns_pcst'}).text.split('|')[1].split(':')[1].strip(' ').replace(',','').replace(';','')
    currentPrice = float(htmlContent.find('span',{'class':'nse_span_price_wrap'}).text.strip(' '))
    masterData['currentPrice'] = currentPrice
    masterData['minimumPrice'] = currentPrice
    currentDate = datetime.datetime.now().strftime('%Y-%m-%d 00:00:00')
    masterData['minimumPriceDate'] = currentDate
    getMinimumPrice(masterData,currentPrice)
    getMinimumRSI(masterData)
    allData.append(masterData)

def getMinimumPrice(data,currentPrice):
    flag = True
    historyPage = yahooPage+quote(data['Company Symbol'])+".BO/history"
    htmlContent = getData(historyPage)
    contentWithTags = htmlContent.findAll('tr',{'class':'BdT'})
    for contentWithTag in contentWithTags[0:30]:
        #print(contentWithTag)
        try:
            date = contentWithTag.findAll('td')[0].text
            price = float(contentWithTag.findAll('td')[4].text.replace(',',''))
            if(price <= currentPrice or flag):
                data['minimumPrice'] = price
                new_date = datetime.datetime.strptime(date,'%d-%b-%Y')
                data['minimumPriceDate'] = new_date
                #print(data['minimumPriceDate'])
                currentPrice = price
                flag = False
        except:
            print("error in getMinimumPrice")
            print(data)

def getMinimumRSI(data):
    flag = True
    stockPage = TraderscockpitRSI+quote(data['Company Symbol']) 
    htmlContent = getData(stockPage)
    contentWithTags = htmlContent.findAll('tr',{'class':['odd','even']})
    for contentWithTag in contentWithTags[0:30]:
        #print(contentWithTag)
        try:
        #if True:
            if flag:
                data['currentRSI'] = float(contentWithTag.findAll('td')[2].text)
                data['minimumRSI'] = data['currentRSI']
                flag = False
            date = contentWithTag.findAll('td')[0].text
            new_date = datetime.datetime.strptime(date,'%Y-%m-%d')          
            if(data['minimumPriceDate'] == new_date):
                dataValue = float(contentWithTag.findAll('td')[2].text)
                data['minimumRSI'] = dataValue
                break
        except:
            print("error in getMinimumRSI")
            print(data)

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
#marketCapThreshold = float(input("Market Cap(in cr) Start value you want to set as criteria for BSE: "))
marketCapThreshold = 5000
getAllData()
newlist = sorted(allData, key=lambda k: k['Market Cap(in cr)'],reverse = True)
writeDictToCSV('MasterFile1028',newlist)
print("End Time: ",datetime.datetime.now())
