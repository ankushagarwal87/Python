import imaplib
import email
from bs4 import BeautifulSoup

mail = imaplib.IMAP4_SSL('imap.outlook.com')

def setupOutlook(mailId,password):
    mail.login(mailId,password)

def getLatestMail():
    a=[]
    mail.list()
    mail.select("Inbox") # connect to inbox.
    result, data = mail.search(None, "(UNSEEN)")
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    #print(id_list)
    for id in id_list:
        # fetch the email body (RFC822) for the given ID
        result, email_data = mail.fetch(id, "(RFC822)")
        raw_email = email_data[0][1]
        #print(raw_email)
        #continue inside the same for loop as above
        raw_email_string = raw_email.decode('utf-8')
        #print(raw_email_string)        # converts byte literal to string removing b''
        email_message = email.message_from_string(raw_email_string)
        print(email_message['From'])
        print(email_message['Subject'])
        print(email_message['Date'])
        #print(email_message)
        print(email_message.is_multipart())
        if email_message.is_multipart():
            for part in email_message.walk():
                if part.get_content_type() == "text/plain": 
                    body = part.get_payload(decode=True)
                    print("plain",body.decode('utf-8'))
                if part.get_content_type() == "text/html":
                    body = part.get_payload(decode=True)
                    htmlContent = BeautifulSoup(body , "html.parser")
                    print("beautiful Soup")
                    #print(htmlContent)
                    contentWithTags = htmlContent.find_all('p')
                    for contentWithTag in contentWithTags:
                        print(contentWithTag.get_text())
        else:
            if email_message.get_content_type() == "text/html":
                    body = email_message.get_payload(decode=True)
                    htmlContent = BeautifulSoup(body , "html.parser")
                    print("beautiful Soup")
                    #print(htmlContent)
                    contentWithTags = htmlContent.find_all('p')
                    for contentWithTag in contentWithTags:
                        print(contentWithTag.get_text())
            else:
                body = email_message.get_payload(decode=True)
                #print(body.decode('utf-8'))
                a=body.decode('utf-8')
                print(a)
                     


if __name__ == "__main__":
    setupOutlook('####@outlook.com', '###')
    getLatestMail()
