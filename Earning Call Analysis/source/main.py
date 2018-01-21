import imaplib
import email
import time
import os
import nltk
import math
import requests
import smtplib
import pdfkit
import shutil
import jinja2
import pickle

#from pylab import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from shutil import copyfile


login_data = {'slugs[]': '',
                  'rt': '',
                  'user[url_source]': '',
                  'user[location_source]': 'orthodox_login',
                  'user[email]': '####@gmail.com',
                  'user[password]': '####',
                  }

#Variables for sentence counting
countFutureLooking = 0
countEarningImpact = 0
countTotal = 0


#Variables for sentiment Analysis
overallSentiment = 0
overallPositiveSentiment = 0
overallNegativeSentiment = 0
overallNeutralSentiment = 0


#Variable for dictionary for showing Modal in UI
dictionaryTranscript=dict()
dictionaryForwardLooking=dict()
dictionaryEarningImpact=dict()

#Variable for Sentiment Analysis
sid= SentimentIntensityAnalyzer()

#Variables for Participants
listOfExecutives = []
listOfAnalysts=[]


#Variable for sending email
fromaddr = "###@gmail.com"
toaddr = "###@gmail.com"

#All Source file names
FLCorpusPath = os.getcwd()+ "/Forward Looking Corpus.txt"
EICorpusPath = os.getcwd()+ "/Earning Impact Corpus.txt"
AntiListCorpusPath = os.getcwd()+ "/antilist.txt"

#All Source File objets
forwardLookingCorpusFile=open(FLCorpusPath,"r")
earningImpactCorpusFile=open(EICorpusPath,"r")
antiListCorpusFile=open(AntiListCorpusPath,"r")

#All corpus words
forwardLookingWords=forwardLookingCorpusFile.read().split(',')
earningImpactWords=earningImpactCorpusFile.read().split(',')
antiListWords=antiListCorpusFile.read().split(',')


sourceDir = os.getcwd()
dataDir = ""
mail = imaplib.IMAP4_SSL('imap.gmail.com')
sentenceList = []
links =[]
data = []




#******************** Functions for Analysis *********************************
def analyzeTense(sentance):
    words = word_tokenize(sentance)
    tagged = pos_tag(words)

    tense = {}
    tense["future"] = len([word for word in tagged if word[1] == "MD"])
    tense["present"] = len([word for word in tagged if word[1] in ["VBP", "VBZ","VBG"]])
    tense["past"] = len([word for word in tagged if word[1] in ["VBD", "VBN"]]) 
    return(tense)


def analyzeForwardLooking(sentence):
    if(isAntiListPresent(sentence)):
        return False
    tense = analyzeTense(sentence)
    if(tense["future"]+ tense["present"] > tense["past"]):
        for forwardLookingWord in forwardLookingWords:
                if forwardLookingWord in sentence:                   
                        return (True)
    return (False)

def isAntiListPresent(sentence):
    for antiListWord in antiListWords:
        if antiListWord in sentence:
            return (True)
    return (False)

def analyzeEarningImpact(forwardLookingSentence):
    for earningImpactWord in earningImpactWords:
        if earningImpactWord in forwardLookingSentence:
            return (True)
    return (False)
    
    
def analyzeTranscript(inputTranscriptFile,FLOutputPath,EIOutputPath):
    global countTotal
    global countFutureLooking
    global countEarningImpact
    global dictionaryTranscript
    global dictionaryForwardLooking
    global dictionaryEarningImpact
    countTotal=0
    countFutureLooking=0
    countEarningImpact=0
    dictionaryTranscript=dict()
    dictionaryForwardLooking=dict()
    dictionaryEarningImpact=dict()
    #print(FLOutputPath,EIOutputPath)

    earningImpactOutputFile=open(EIOutputPath,"w")
    forwardLookingOutputFile=open(FLOutputPath,"w")
    inputTranscriptSentences=sent_tokenize(inputTranscriptFile)
    for sentence in inputTranscriptSentences:
        countTotal = countTotal+1
        dictionaryTranscript[countTotal] = sentence
        if(analyzeForwardLooking(sentence.lower())):
            dictionaryForwardLooking[countTotal] = sentence
            countFutureLooking = countFutureLooking+1
            forwardLookingSentence = sentence
            forwardLookingOutputFile.write(forwardLookingSentence)
            forwardLookingOutputFile.write("\n")
            forwardLookingOutputFile.write("\n")
            if(analyzeEarningImpact(forwardLookingSentence.lower())):
                dictionaryEarningImpact[countTotal] = sentence
                countEarningImpact = countEarningImpact+1
                earningImpactSentence = forwardLookingSentence
                earningImpactOutputFile.write(earningImpactSentence)
                earningImpactOutputFile.write("\n")
                earningImpactOutputFile.write("\n")
               

    print("*******Total Sentences*******",countTotal)
    print("*******Future+Present > Past (With Anti List) Looking Sentences*******",countFutureLooking)
    print("*******Earning Impact Sentences*******",countEarningImpact)
    earningImpactOutputFile.close()
    forwardLookingOutputFile.close()
    forwardLookingCorpusFile.close()
    earningImpactCorpusFile.close()



#************ Fuctions for creating Web Page ************************************************

def createWebPage(companyName,quarter):
	#print("Work in Progress for webpage")
	os.chdir("..")
	os.chdir("..")
	os.chdir("source")
	templateFile=os.getcwd()+"/CompanyQuaterAnalyzedData.html"
	templateFileCompany=os.getcwd()+"/comapnyFinalTemplate.html"
	os.chdir("..")
	os.chdir("data")	

	os.chdir(companyName)
	os.chdir(quarter)
	env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=os.getcwd()))
	htmlFile = os.getcwd()+"/"+companyName+quarter+".html"
	copyfile(templateFile,htmlFile)

	template = env.get_template(companyName+quarter+".html")
	htmlFileQuarter=os.getcwd()+"/"+companyName+quarter+".html"
	outFile = open(htmlFileQuarter,"w")
	
	transcriptData = getFormattedData(dictionaryTranscript,'t')
	forwardLookingSentenceData = getFormattedData(dictionaryForwardLooking,'fls')
	earningStatements = getFormattedData(dictionaryEarningImpact,'ei')

	finalOutput = template.render(transcriptData = transcriptData,forwardLookingSentenceData = forwardLookingSentenceData,earningStatements=earningStatements)
	outFile.write(finalOutput)
	os.chdir("..")
	outFile.close()

	env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=os.getcwd()))
	htmlFileCompany = os.getcwd()+"/"+companyName+".html"
	copyfile(templateFileCompany,htmlFileCompany)
	prepareCompanyData(companyName,env)

        
	

#************ Fuctions for creating Web Page for Company************************************************


def prepareCompanyData(companyName,env):
    template = env.get_template(companyName+".html")
    htmlFileCompany=os.getcwd()+"/"+companyName+".html"
    outFile = open(htmlFileCompany,"w")
	
    packetData = []	
    NumberOfQuarter = 0
    quarters=[]
    Q1ImageAddress=""
    Q2ImageAddress=""
    Q3ImageAddress=""
    Q4ImageAddress=""
    Q1ExecutiveName=[]
    Q2ExecutiveName=[]
    Q3ExecutiveName=[]
    Q4ExecutiveName=[]
    Q1AnalystName=[]
    Q2AnalystName=[]
    Q3AnalystName=[]
    Q4AnalystName=[]
    Q1Positive=[]
    Q2Positive=[]
    Q3Positive=[]
    Q4Positive=[]
    Q1Negative=[]
    Q2Negative=[]
    Q3Negative=[]
    Q4Negative=[]
    Q1Compound=[]
    Q2Compound=[]
    Q3Compound=[]
    Q4Compound=[]
   
    
    
    for i in range(1,4):
        os.chdir("Q"+str(i))
        if(i==1):
            if(os.path.exists('listOfExecutives.p')):
                tempDict = {}
                quarters.append(["Q1","Quarter 1",os.getcwd()+"/"+companyName+"Q1.html"])
                NumberOfQuarter=NumberOfQuarter+1
                Q1ImageAddress= os.getcwd()+"/piechart.png"
                
                executive = open('listOfExecutives.p', 'rb')
                Q1ExecutiveName =pickle.load(executive)

                analyst = open('listOfAnalysts.p', 'rb')
                Q1AnalystName =pickle.load(analyst)

                positive = open('positiveSentences.p', 'rb')
                Q1Positive =pickle.load(positive)

                negative = open('negativeSentences.p', 'rb')
                Q1Negative =pickle.load(negative)
                 
                compound = open('compoundSentiment.p', 'rb')
                Q1Compound =pickle.load(compound)

                piChartData = open(dataDir + '/' + companyName + '/' + "Q1" + '/' + "piChartData.p", 'rb')
                piChartDataValues =pickle.load(piChartData)

                tempDict["quarterIndex"] = 1
                tempDict["company"]= companyName
                tempDict["quarterNum"]="Q1"
                tempDict["quarter"]="Quarter 1"
                tempDict["year"]= " "
                tempDict["quarterFile"] = "file:///"+os.getcwd()+"/"+companyName+"Q1.html"
                tempDict["negativeValueForGraph"]= piChartDataValues[1]
                tempDict["positiveValueForGraph"]= piChartDataValues[0]
                tempDict["neutralValueForGraph"]=  piChartDataValues[2]
                tempDict["negativeSentences"] = Q1Negative
                tempDict["positiveSentences"] = Q1Positive
                tempDict["analyst"] = Q1AnalystName
                tempDict["executive"] = Q1ExecutiveName
                tempDict["compoundSentiment"] = "{0:.2f}".format(Q1Compound)
                #print(tempDict)
                packetData.append([tempDict])
                                                                                                       
        if(i==2):
            if(os.path.exists('listOfExecutives.p')):
                tempDict = {}
                quarters.append(["Q2","Quarter 2",os.getcwd()+"/"+companyName+"Q2.html"])
                NumberOfQuarter=NumberOfQuarter+1
                Q2ImageAddress= os.getcwd()+"/piechart.png"
                
                executive = open('listOfExecutives.p', 'rb')
                Q2ExecutiveName =pickle.load(executive)

                analyst = open('listOfAnalysts.p', 'rb')
                Q2AnalystName =pickle.load(analyst)

                positive = open('positiveSentences.p', 'rb')
                Q2Positive =pickle.load(positive)

                negative = open('negativeSentences.p', 'rb')
                Q2Negative =pickle.load(negative)
                 
                compound = open('compoundSentiment.p', 'rb')
                Q2Compound =pickle.load(compound)
                
                piChartData = open(dataDir + '/' + companyName + '/' + "Q2" + '/' + "piChartData.p", 'rb')
                piChartDataValues =pickle.load(piChartData)

                tempDict["quarterIndex"] = 2
                tempDict["company"]= companyName
                tempDict["quarterNum"]="Q2"
                tempDict["quarter"]="Quarter 2"
                tempDict["year"]= " "
                tempDict["quarterFile"] = "file:///"+os.getcwd()+"/"+companyName+"Q2.html"
                tempDict["negativeValueForGraph"]= piChartDataValues[1]
                tempDict["positiveValueForGraph"]= piChartDataValues[0]
                tempDict["neutralValueForGraph"]=  piChartDataValues[2]
                tempDict["negativeSentences"] = Q2Negative
                tempDict["positiveSentences"] = Q2Positive
                tempDict["analyst"] = Q2AnalystName
                tempDict["executive"] = Q2ExecutiveName
                tempDict["compoundSentiment"] = "{0:.2f}".format(Q2Compound)
                #print(tempDict)
                packetData.append([tempDict])

        if(i==3):
            if(os.path.exists('listOfExecutives.p')):
                tempDict = {}
                quarters.append(["Q3","Quarter 3",os.getcwd()+"/"+companyName+"Q3.html"])
                NumberOfQuarter=NumberOfQuarter+1
                Q3ImageAddress= os.getcwd()+"/piechart.png"
                
                executive = open('listOfExecutives.p', 'rb')
                Q3ExecutiveName =pickle.load(executive)

                analyst = open('listOfAnalysts.p', 'rb')
                Q3AnalystName =pickle.load(analyst)

                positive = open('positiveSentences.p', 'rb')
                Q3Positive =pickle.load(positive)

                negative = open('negativeSentences.p', 'rb')
                Q3Negative =pickle.load(negative)
                 
                compound = open('compoundSentiment.p', 'rb')
                Q3Compound =pickle.load(compound)

                piChartData = open(dataDir + '/' + companyName + '/' + "Q3" + '/' + "piChartData.p", 'rb')
                piChartDataValues =pickle.load(piChartData)

                tempDict["quarterIndex"] = 3
                tempDict["company"]= companyName
                tempDict["quarterNum"]="Q3"
                tempDict["quarter"]="Quarter 3"
                tempDict["year"]= " "
                tempDict["quarterFile"] = "file:///"+os.getcwd()+"/"+companyName+"Q3.html"
                tempDict["negativeValueForGraph"]= piChartDataValues[1]
                tempDict["positiveValueForGraph"]= piChartDataValues[0]
                tempDict["neutralValueForGraph"]=  piChartDataValues[2]
                tempDict["negativeSentences"] = Q3Negative
                tempDict["positiveSentences"] = Q3Positive
                tempDict["analyst"] = Q3AnalystName
                tempDict["executive"] = Q3ExecutiveName
                tempDict["compoundSentiment"] = "{0:.2f}".format(Q3Compound)
                #print(tempDict)
                packetData.append([tempDict])
        
        if(i==4):
            if(os.path.exists('listOfExecutives.p')):
                tempDict = {}
                quarters.append(["Q4","Quarter 4",os.getcwd()+"/"+companyName+"Q4.html"])
                NumberOfQuarter=NumberOfQuarter+1
                Q4ImageAddress= os.getcwd()+"/piechart.png"
                
                executive = open('listOfExecutives.p', 'rb')
                Q4ExecutiveName =pickle.load(executive)

                analyst = open('listOfAnalysts.p', 'rb')
                Q4AnalystName =pickle.load(analyst)

                positive = open('positiveSentences.p', 'rb')
                Q4Positive =pickle.load(positive)

                negative = open('negativeSentences.p', 'rb')
                Q4Negative =pickle.load(negative)
                 
                compound = open('compoundSentiment.p', 'rb')
                Q4Compound =pickle.load(compound)

                
                piChartData = open(dataDir + '/' + companyName + '/' + "Q4" + '/' + "piChartData.p", 'rb')
                piChartDataValues =pickle.load(piChartData)

                tempDict["quarterIndex"] = 4
                tempDict["company"]= companyName
                tempDict["quarterNum"]="Q4"
                tempDict["quarter"]="Quarter 4"
                tempDict["year"]= " "
                tempDict["quarterFile"] = "file:///"+os.getcwd()+"/"+companyName+"Q4.html"
                tempDict["negativeValueForGraph"]= piChartDataValues[1]
                tempDict["positiveValueForGraph"]= piChartDataValues[0]
                tempDict["neutralValueForGraph"]=  piChartDataValues[2]
                tempDict["negativeSentences"] = Q4Negative
                tempDict["positiveSentences"] = Q4Positive
                tempDict["analyst"] = Q4AnalystName
                tempDict["executive"] = Q4ExecutiveName
                tempDict["compoundSentiment"] = "{0:.2f}".format(Q4Compound)
                packetData.append([tempDict])
                #print(tempDict)



        os.chdir("..")

    #print(packetData)
    finalOutput = template.render(info = packetData,company=companyName)
    
    outFile.write(finalOutput)
    outFile.close()

	
#*************Function for generating Quarter html *****

def getFormattedData(sentence_dict,typeOfFile):
    #data = fileObject.read()
    #lines = data.split('\n')
    ids = []
    tr  = []
    results = []
    i=0
    for linenumber,sent in sentence_dict.items():
        #if (typeOfFile=='ei'):
            #print(linenumber,sent)
        #for i in range(0,len(lines)):
        tr.append('t'+str(linenumber))
        ids.append(typeOfFile+str(linenumber))
        results.append([tr[i],ids[i],sent])
        i=i+1
    return(results)

#************ Fuctions for creating PDF ************************************************

def createPDF(companyName,quarter):
        htmlFile = os.getcwd()+"/"+companyName+quarter+".html"
        Pdfname = companyName+quarter+".pdf"
	#os.chdir("..")
	#os.chdir("..")
	#os.chdir("source")
	#path_wkthmltopdf = os.getcwd()+"\\"+"wkhtmltopdf.exe"
        #path_wkthmltopdf = r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe'
        #config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
        #pdfkit.from_file(htmlFile,Pdfname,configuration=config)
        pdfkit.from_file(htmlFile,Pdfname)
	#os.chdir("..")
	#os.chdir("data")
	#os.chdir(companyName)


#************ Fuctions for sending email ************************************************

def sendEmail(companyName,quarter):
        linkName=companyName+" "+quarter+" analysis"
        link="file:///"+os.getcwd()+"/"+companyName+".html"
        #print(os.getcwd())
        print(link)
        #link="https://pythonprogramming.net/creating-first-flask-web-app/"
        body = "<p>Earning Call Transcript Analysis for "+companyName+" Quarter "+quarter+" has been generated & available for your review.</p><br><p>Please go through the attach pdf/links for detailed review for the same.</p><br><a href="+link+">"+linkName+"</a><br><p>Thanks<br>Data Vaders<p>" 
        Pdfname = companyName+quarter+".pdf"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = companyName+" "+quarter+" Earning Call Transcript Analysis"
        msg.attach(MIMEText(body, 'html'))
        attachment = open(os.getcwd()+"/"+quarter+"/"+Pdfname, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % Pdfname)
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "####")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()


#************ Functions for getting Transcript from SeekingAlpha ************************

def setupGmail(mailId,password):
    mail.login(mailId,password)

def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

def getdata(link):
    global data
    data = []
    count = False
    companyName = " "
    company = " "
    dataTemp = []
    quarter = ""
    if 'q1' in link:
        quarter = "Q1"
    if 'q2' in link:
        quarter = "Q2"
    if 'q3' in link:
        quarter = "Q3"
    if 'q4' in link:
        quarter = "Q4"
        
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0'
    response = s.post('https://seekingalpha.com/account/login', data=login_data)
    #After login, can access single view for the whole article, so add ?part=single after each link    
    page = requests.get(link, headers={'User-Agent': 'Mozilla/5.0'}, timeout = 10)
    #print(page)
    htmlContent = BeautifulSoup(page.content , "html.parser")
    contentWithTags = htmlContent.find_all('p')
    for contentWithTag in contentWithTags:
        data.append(contentWithTag.get_text())
        #print(contentWithTag.get_text())
        if count == False:
            company = contentWithTag.get_text()
            count = True
    dataTemp = company.split(' ')
    companyName = dataTemp[0]
    return(companyName,quarter)
        
        

def getNumberOfUnseenMail():
    mail.list()
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.
    result, data = mail.search(None, "(UNSEEN)")
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string

    return(id_list)
    #print(id_list)

def readMailById(id):
    links.clear() 
    # fetch the email body (RFC822) for the given ID
    result, email_data = mail.fetch(id, "(RFC822)")
    
    raw_email = email_data[0][1]
    #print(raw_email)
    #continue inside the same for loop as above
    raw_email_string = raw_email.decode('utf-8')
    #print(raw_email_string)
    # converts byte literal to string removing b''
    email_message = email.message_from_string(raw_email_string)
    # this will loop through all the available multiparts in mail
    for part in email_message.walk():
     if part.get_content_type() == "text/html": # ignore attachments/html
      body = part.get_payload(decode=True)
      #print(body)
      htmlContent = BeautifulSoup(body , "html.parser")
      contentWithTags = htmlContent.find_all('a')
      for contentWithTag in contentWithTags:
            #print(contentWithTag['href'])
            end = contentWithTag['href'].find('?')
            link = contentWithTag['href'][0:end]
            links.append(link)

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
def setupDir(companyName):
    os.chdir("..")
    parentDir = os.getcwd()
    os.chdir("data")
    dataDir = os.getcwd()
    ensure_dir(dataDir +'/'+ companyName)
    os.chdir(companyName)
    companyDir = os.getcwd()
    ensure_dir(companyDir +'/Q1')
    ensure_dir(companyDir +'/Q2')
    ensure_dir(companyDir +'/Q3')
    ensure_dir(companyDir +'/Q4')
    os.chdir("..")
    os.chdir("..")
    os.chdir("source")
    #print(os.getcwd())

def saverawfile(companyName,quarter):
    filename = companyName + '-' + quarter+ 'transcript.txt'
    os.chdir("..")
    parentDir = os.getcwd()
    os.chdir("data")
    dataDir = os.getcwd()
    os.chdir(dataDir)
    #print(os.getcwd())
    os.chdir(dataDir+'/'+companyName)
    curDir = os.getcwd()
    os.chdir(curDir+'/'+quarter)
    #print(os.getcwd())
    filepath = os.getcwd() + '/' + filename
    file = open(filename,"w")
    for line in data:
        file.write(line)
        file.write('\n')
    file.close()
    os.chdir(sourceDir)
    #print(os.getcwd())
    return(filepath)
    

def createPieChart(dataDir,companyName,quarter):
    global overallPositiveSentiment
    global overallNegativeSentiment
    global overallNeutralSentiment

    fracs = [overallPositiveSentiment, overallNegativeSentiment, overallNeutralSentiment]
    pickle.dump(fracs,open(dataDir + '/' + companyName + '/' + quarter + '/' + "piChartData.p", "wb"))
    #print("Pi chart data")
    #print(fracs)
def getSentiments(fullTranscriptSentences,dataDir,companyName,quarter):
    global overallSentiment
    global overallPositiveSentiment
    global overallNegativeSentiment
    global overallNeutralSentiment

    totalSentencesInTranscript = len(fullTranscriptSentences)
    for sentence in fullTranscriptSentences:
        ss= sid.polarity_scores(sentence)
        negative = ss["neg"]
        positive = ss["pos"]
        neutral = ss["neu"]
        compound = ss["compound"]
                     
        overallSentiment = overallSentiment + compound
        overallPositiveSentiment = overallPositiveSentiment + positive
        overallNegativeSentiment = overallNegativeSentiment + negative
        overallNeutralSentiment = overallNeutralSentiment + neutral

    overallSentiment = overallSentiment/totalSentencesInTranscript
    overallPositiveSentiment = overallPositiveSentiment/totalSentencesInTranscript
    overallNegativeSentiment = overallNegativeSentiment/totalSentencesInTranscript
    overallNeutralSentiment = overallNeutralSentiment/totalSentencesInTranscript
            
    print("*****Overall Sentiments*********")
    print("compound :",overallSentiment)
    print("pos :",overallPositiveSentiment)
    print("neg :",overallNegativeSentiment)
    print("neu :",overallNeutralSentiment)
    createPieChart(dataDir,companyName,quarter)
    pickle.dump(overallSentiment,open(dataDir + '/' + companyName + '/' + quarter + '/' + "compoundSentiment.p", "wb"))
    overallSentiment =0
    overallPositiveSentiment =0
    overallNegativeSentiment=0
    overallNeutralSentiment=0

def getPositiveSentences(fwdLookingSentences,dataDir,companyName,quarter):
    PositiveSentences = []
    for fwdlookingSentence in fwdLookingSentences:
        fwss= sid.polarity_scores(fwdlookingSentence)
        positive = fwss["pos"]
        if(positive>0.2):
            PositiveSentences.append(fwdlookingSentence)

    #print("*****Positive Satements*********")
    #print(PositiveSentences)
    pickle.dump(PositiveSentences,open(dataDir + '/' + companyName + '/' + quarter + '/' + "positiveSentences.p", "wb"))
    PositiveSentences = []
    


def getNegativeSentences(fwdLookingSentences,dataDir,companyName,quarter):
    NegativeSentences = []
    for fwdlookingSentence in fwdLookingSentences:
        fwss= sid.polarity_scores(fwdlookingSentence)
        negative = fwss["neg"]
        if(negative>0.2):
            NegativeSentences.append(fwdlookingSentence)
       
    #print("*****Negative Satements*********")
    #print(NegativeSentences)
    pickle.dump(NegativeSentences,open(dataDir + '/' + companyName + '/' + quarter + '/' + "negativeSentences.p", "wb"))
    NegativeSentences = []





    
def getListOfParticipants(fullTranscriptSentences,dataDir,companyName,quarter):
    
    executiveStart = 0
    AnalystStart = 0
    OperatorStart = 0
    i=0
    global listOfExecutives
    global listOfAnalysts
    for transcriptSentence in fullTranscriptSentences:
        if "Executives" == transcriptSentence:
            executiveStart = i
        if "Analysts" == transcriptSentence:
            AnalystStart = i
        if "Operator" == transcriptSentence: 
            OperatorStart = i
            break
        i = i+1
        
    i=0
    for transcriptSentence in fullTranscriptSentences:
        if i>executiveStart and i<AnalystStart:
            listOfExecutives.append(transcriptSentence)

        if i>AnalystStart and i<OperatorStart:
            listOfAnalysts.append(transcriptSentence)
        i = i+1

    #print("**********List of Participants**********")
    #print("executives :",listOfExecutives)
    #print("analysts :",listOfAnalysts)
    
    pickle.dump(listOfExecutives,open(dataDir + '/' + companyName + '/' + quarter + '/' + "listOfExecutives.p", "wb"))
    pickle.dump(listOfAnalysts,open(dataDir + '/' + companyName + '/' + quarter + '/' + "listOfAnalysts.p", "wb"))

    listOfExecutives=[]
    listOfAnalysts=[]




       
#*********************************Main Funtion call*************************************#           

if __name__ == "__main__":
    setupGmail('####@gmail.com', '#####')
    while True:
        id_list = getNumberOfUnseenMail()
        if len(id_list) is not 0:
            print(str(len(id_list)) + " "+ "Mails. Starting the Analyzer")
            for mailId in id_list:
                readMailById(mailId)
                uniquelinks = uniq(links)    
                for link in uniquelinks:
                    if 'article' and 'earnings' and 'call' and 'transcript' in link:
                        print("***************************************************************************************************")
                        print(link)
                        companyName,quarter = getdata(link+'?part=single')
                        print(companyName + ' ' + quarter)
                        setupDir(companyName)
                        inputfilePath = saverawfile(companyName,quarter)
                        os.chdir("..")
                        parentDir = os.getcwd()
                        os.chdir("data")
                        dataDir = os.getcwd()
                                                 
                        infile = open(inputfilePath, 'r')
                        inputTranscriptFile = infile.read()
                        analyzeTranscript(inputTranscriptFile,dataDir + '/' + companyName + '/' + quarter + '/' + 'fwdlooking.txt', dataDir + '/' + companyName + '/' + quarter + '/' + 'earningimpact.txt' )
                        forwardLookingOutputFile=open(dataDir + '/' + companyName + '/' + quarter + '/' + 'fwdlooking.txt',"r")
            
                        fullTranscriptSentences = sent_tokenize(inputTranscriptFile)
                        fwdLookingSentences = sent_tokenize(forwardLookingOutputFile.read())
                        getSentiments(fullTranscriptSentences,dataDir,companyName,quarter)
                        getPositiveSentences(fwdLookingSentences,dataDir,companyName,quarter)
                        getNegativeSentences(fullTranscriptSentences,dataDir,companyName,quarter)
                        getListOfParticipants(inputTranscriptFile.split('\n'),dataDir,companyName,quarter)
                     

                        companyDataDir=dataDir+ '/' + companyName
                        #print(companyDataDir)
                        os.chdir(companyDataDir)
                        #print(os.getcwd())
                        createWebPage(companyName,quarter)
                        os.chdir(quarter)
                        createPDF(companyName,quarter)
                        os.chdir("..")
                        sendEmail(companyName,quarter)
                        os.chdir("..")
                        os.chdir("..")
                        os.chdir("source")
                        #print(packetData)
                        #print(os.getcwd())
                        #for linenumber,sent in dictionaryEarningImpact.items():
                            #print(linenumber,sent)
                        
        else:
            print("No Mail Found in INBOX")
            print("\n")
            time.sleep(10)
            
            
    
