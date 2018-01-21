import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet

from itertools import product

def findVerb(sentence):
    words = word_tokenize(sentence)
    tagged = pos_tag(words)
    print(tagged)


def findwordnet():    
    list1 = ['Compare', 'require']
    list2 = ['choose', 'copy', 'define']#, 'duplicate', 'find', 'how', 'identify', 'label', 'list', 'listen', 'locate', 'match', 'memorise', 'name', 'observe', 'omit', 'quote', 'read', 'recall', 'recite', 'recognise', 'record', 'relate', 'remember', 'repeat', 'reproduce', 'retell', 'select', 'show', 'spell', 'state', 'tell', 'trace', 'write']
    list = []

    for word1 in list1:
        for word2 in list2:
            wordFromList1 = wordnet.synsets(word1)
            wordFromList2 = wordnet.synsets(word2)
            if wordFromList1 and wordFromList2: 
                s = wordFromList1[0].wup_similarity(wordFromList2[0])
                list.append([s,wordFromList1[0],wordFromList2[0]])
    print((list))


file=open('Transformation List','r')
data=file.read()
transformationlist=data.split('\n')
#print(data)
#line=input("Enter sentence")
#findVerb(line)
findwordnet()


