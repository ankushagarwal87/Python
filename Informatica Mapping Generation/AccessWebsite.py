import requests
from bs4 import BeautifulSoup


def getdata(link):
    #data=''
    #page = requests.get('https://issues.apache.org/jira/browse/HIVE-16998')
    page = requests.get(link)
    print(page)
    htmlContent = BeautifulSoup(page.content , "html.parser")
    #print(htmlContent)
    #sprint(htmlContent.find('title'))
    #div=htmlContent.find_all('div')
    #contentWithTags = htmlContent.find_all('p')
    description=htmlContent.find(id="description-val").get_text()
    #print(description)
    return description 


if __name__ == "__main__":
    link=input("Enter website link : ")
    data=getdata(link)
    print(data)
