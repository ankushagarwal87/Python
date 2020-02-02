import requests
import csv
import os
from bs4 import BeautifulSoup
s = requests.Session()
s.headers['User-Agent'] = 'Mozilla/5.0'
homePage="https://www.glassdoor.com/Reviews/company-reviews.htm"
home="https://www.glassdoor.com/"
product = ['Dental Insurance','Vision Insurance','Life Insurance','Disability Insurance','Accidental Death & Dismemberment Insurance','Occupational Accident Insurance']
masterData={}
columnName=['Company Name','Website','Headquarters','Size','Founded','Type','Industry','Revenue','Competitors',
            'Life Insurance','# voted having Life Insurance','# not having Life Insurance','% having Life Insurance','Rating Life Insurance',
            'Dental Insurance','# voted having Dental Insurance','# not having Dental Insurance','% having Dental Insurance','Rating Dental Insurance',
            'Vision Insurance','# voted having Vision Insurance','# not having Vision Insurance','% having Vision Insurance','Rating Vision Insurance',
            'Disability Insurance','# voted having Disability Insurance','# not having Disability Insurance','% having Disability Insurance','Rating Disability Insurance',
            'Accidental Death & Dismemberment Insurance','# voted having Accidental Death & Dismemberment Insurance',
            '# not having Accidental Death & Dismemberment Insurance','% having Accidental Death & Dismemberment Insurance',
            'Rating Accidental Death & Dismemberment Insurance',
            'Occupational Accident Insurance','# voted having Occupational Accident Insurance','# not having Occupational Accident Insurance',
            '% having Occupational Accident Insurance','Rating Occupational Accident Insurance'
            ]
allData=[]

def getData(link):
    #print(link)
    page = requests.get(link,headers={'User-Agent': 'Mozilla/5.0'},timeout = 10)
    #print(page)
    htmlContent = BeautifulSoup(page.content , "html.parser")
    return htmlContent

def getCompanyLink(companyName):
    data={'sc.keyword':companyName}
    response = s.post(homePage, data=data)
    #print(response.url)
    companyLink=response.url
    if('SRCH' in companyLink):
        htmlContent = getData(companyLink)
        searchFirstLink = htmlContent.find('a', {'class': 'sqLogoLink'})
        companyLink=home+searchFirstLink.attrs['href']
    #print('Company Page Link -- ',companyLink)
    return companyLink

def getBenefitLink(companyLink):
    htmlContent = getData(companyLink)
    contentWithTags = htmlContent.find('h1', {'class': 'strong'})
    print(contentWithTags.text.strip())
    masterData['Company Name']=contentWithTags.text.strip()
    contentWithTags = htmlContent.find_all('div', {'class': 'infoEntity'})
    for contentWithTag in contentWithTags:
        #print(contentWithTag.find('label').text,contentWithTag.find('span').text)
        masterData[contentWithTag.find('label').text.strip()]=contentWithTag.find('span').text.strip()
    benefitPageLink=htmlContent.find('a', {'class': 'eiCell','class':'cell','class':'benefits'})
    benefitLink=home+benefitPageLink.attrs['href']
    #print('Benefit Page Link -- ',benefitLink)
    return benefitLink

def getInsuranceLink(benefitLink):
    insuranceLink=''
    htmlContent = getData(benefitLink)
    links=htmlContent.findAll('a',{'class':'tt'})
    getBenefitData(links,1)
    links=htmlContent.findAll('span',{'class':'tt subtle'})
    getBenefitData(links,0)
    '''
    majorLink = htmlContent.findAll('a', {'class': 'tightVert', 'class': 'h3'})
    print(majorLink)
    for i in majorLink:
        print(i)
        if(i.find('i',{['class','health']['class','dental']})):
            print(i)
            insuranceLink=home+i.attrs['href']
    print('Insurance Page Link -- ',insuranceLink)
    '''
    return insuranceLink 

def getBenefitData(links,flag):
    for i in links:
        for j in product:
            if (j in i.text):
                #print(i.text,i.attrs['title'])
                splitList=i.attrs['title'].split(' ')
                NumberofEmployeeReportedBenefit=int(splitList[0])
                TotalNumberofEmployeeWhoReported=int(splitList[2])
                start=i.attrs['title'].find('(')
                end=i.attrs['title'].find(')')
                percentOfEmployeeHavingBenefit=float(i.attrs['title'][start+1:end])
                masterData[j]='Already Present'
                masterData['# voted having '+j]=NumberofEmployeeReportedBenefit
                masterData['# not having '+ j]=TotalNumberofEmployeeWhoReported-NumberofEmployeeReportedBenefit
                masterData['% having '+j]=percentOfEmployeeHavingBenefit
                if(percentOfEmployeeHavingBenefit<=25.0 and TotalNumberofEmployeeWhoReported>5):
                    print('We can sell our '+j+' product as overall enrollment '+str(percentOfEmployeeHavingBenefit)+' seem to be very low')
                    masterData[j]='Can be Sell as high chances of product not there with Employer'
                else:
                    if(flag==1):
                        insuranceLink=home+i.attrs['href']
                        #print('Insurance Page Link -- ',insuranceLink)
                        result=getInsuranceData(insuranceLink)
                        masterData['Rating '+j]=result[1]
                        if(result[1]<=2.5 and result[0]>5):
                            masterData[j]='Can be Sell as employee not happy as per rating'
                            

def getInsuranceData(insuranceLink):
    flag=1
    count=2
    nextPageLink=insuranceLink
    htmlContent=getData(insuranceLink)
    #print("Employee who has reported having Insurance: ",htmlContent.find('p',{'class','minor'}).text)
    #print("Employee who has given rating: ",htmlContent.find('span',{'class','votes'}).text)
    #print("Star rating: ",htmlContent.find('span',{'class','rating'}).text)
    result=[int(htmlContent.find('span',{'class','votes'}).text),float(htmlContent.find('span',{'class','rating'}).text)]
    return result
    '''
    while flag:
        flag=getReview(nextPageLink)            
        nextPageLink=insuranceLink[0:len(insuranceLink)-4]+"_IP"+str(count)+".htm"
        count=count+1
   '''   

def getReview(insuranceLink):
    #print('Insurance Page Link -- ',insuranceLink)
    flag=0
    htmlContent=getData(insuranceLink)
    review = htmlContent.findAll('p',{'class','description'})
    for i in review:
        flag=1
        print(i.text)
    return flag


def loopSearchPage(stateSearchLink):
    flag=1
    count=2
    nextPageLink=stateSearchLink
    while flag:
       print("On Search Page",nextPageLink)
       flag=searchStateCompaniesInPage(nextPageLink)
       nextPageLink=stateSearchLink[0:len(stateSearchLink)-4]+"_IP"+str(count)+".htm"
       count=count+1


def searchStateCompaniesInPage(stateLink):
    global masterData
    #print("searchStateCompaniesInPage",stateLink)
    flag=0
    htmlContent=getData(stateLink)
    companieslink=htmlContent.findAll('a',{'class': 'sqLogoLink'})
    for i in companieslink:
        companyLink=home+i.attrs['href']
        print('******************************************************************************************************************')
        #print('Company Page Link -- ',companyLink)
        benefitLink=getBenefitLink(companyLink)
        insuranceLink=getInsuranceLink(benefitLink)
        #print(masterData)
        allData.append(masterData)
        #print(allData)
        masterData={}
        print('******************************************************************************************************************')
        flag=1
    return flag


def writeDictToCSV(dict_data):
    csv_file = os.getcwd() + "/Data.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columnName)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)

        

stateSearchLink=input("Enter state search link :")
loopSearchPage(stateSearchLink)
writeDictToCSV(allData)
'''
companyName=input("Enter company name you want to search for :")
companyLink=getCompanyLink(companyName)
benefitLink=getBenefitLink(companyLink)
insuranceLink=getInsuranceLink(benefitLink)
#getInsuranceData(insuranceLink)
#print(masterData)
writeDictToCSV([masterData])
'''
