import jinja2
import os

def sitemap():

    values = [
        {'name': 'John', 'surname': 'Doe', 'age': 25},
        {'name': 'Jane', 'surname': 'Doe', 'age': 19}
    ]
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=os.getcwd()))
    template = env.get_template('sitemap.xml')
    finalOutput = template.render(values=values)
    outFile = open('test.xml',"w")
    outFile.write(finalOutput)
    outFile.close()

def worflow():

    repository ={'name': 'RS_Dev', 'version': '182', 'codepage': 'MS1252', 'database':'Oracle'}
    folder ={'name': 'Anush', 'group': '', 'owner': 'Administrator', 'shared':'NOTSHARED'}
    sourcelist=[{'DATABASETYPE':'Oracle','DBDNAME':'mpdb4','NAME':'DIM_COUNTRIES','OBJECTVERSION':'1','OWNERNAME':'MPDB4','VERSIONNUMBER':'1'}]
    sourcefieldslist=[]
    sourcefields=['','number','','1','0','ELEMITEM','NO','PRIMARY KEY','24','0','COUNTRY_KEY','NOTNULL','0','0','15','0','','15','0','']
    sourcefieldslist.append(sourcefields)
    #print(repository[0].get('name'))
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=os.getcwd()))
    template = env.get_template('workflow.XML')
    finalOutput = template.render(repository=repository,folder=folder,sourcelist=sourcelist,sourcefieldslist=sourcefieldslist)
    outFile = open('test1.xml',"w")
    outFile.write(finalOutput)
    outFile.close()
    
#sitemap()
worflow()
