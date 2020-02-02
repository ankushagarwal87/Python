import xml.etree.ElementTree as ET

def writeWindow(line,splitby,output):
    if(len(line)>70):
       lines = line.split(splitby)
       output.write(lines[0]+'\n')
       output.write(' '*int(level-4)+splitby+lines[1]+'\n')
    else:
       output.write(line+'\n') 
           
def openTag(tag):
    line=' '*int(level-6)+str(level)+' WW-'+tag.tag.upper()+'-OPEN PIC X('+str(len(tag.tag)+2)+') VALUE "<'+tag.tag+'>".'
    writeWindow(line,'PIC',out)

def closeTag(tag):
    line=' '*int(level-6)+str(level)+' WW-'+tag.tag.upper()+'-CLOSE PIC X('+str(len(tag.tag)+2)+') VALUE "</'+tag.tag+'>".'
    writeWindow(line,'PIC',out)

def valueTag(tag):
    line=' '*int(level-6)+str(level)+' WW-'+tag.tag.upper()+'-VALUE PIC X('+str(len(tag.text))+') VALUE SPACE.'
    writeWindow(line,'PIC',out)
    line=' '*int(level-6)+'MOVE "'+tag.tag+'" TO'+' WW-'+tag.tag.upper()+'-VALUE.'
    writeWindow(line,'TO',codeOut)
         
def parseChild(child):
    for elem in child:
        #print(' '*level,level,elem.tag,elem.text)
        if(not list(elem)):
            openTag(elem)
            valueTag(elem)
            closeTag(elem)
        else:
            openTag(elem)
            parseChild(elem)
            closeTag(elem)
            
level = 10
out=open('copybook3.txt','w')
codeOut=open('code3.txt','w')
tree = ET.parse('Test2.xml')
root = tree.getroot()
openTag(root)
parseChild(root)
closeTag(root)
out.close()
codeOut.close()


