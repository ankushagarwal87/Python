from itertools import permutations
from itertools import combinations
import random

randomSetForSagai      = set()
randomSetForMehendi    = set()
randomSetForSangeet    = set()
randomSetForVarmala    = set()
randomSetForPhere      = set()
randomSetForSajangoth  = set()
for i in range(100):
    #print(i)
    randomSetForSagai.add(random.randrange(1,462))
    randomSetForMehendi.add(random.randrange(1,462))
    randomSetForSangeet.add(random.randrange(1,462))
    randomSetForVarmala.add(random.randrange(1,462))
    randomSetForPhere.add(random.randrange(1,462))
    randomSetForSajangoth.add(random.randrange(1,462))
#print (len(randomSetForSagai))
#print (randomSetForSagai)
randomListForSagai = list(randomSetForSagai)
randomListForMehendi = list(randomSetForMehendi)
randomListForSangeet = list(randomSetForSangeet)
randomListForVarmala = list(randomSetForVarmala)
randomListForPhere= list(randomSetForPhere)
randomListForSajangoth = list(randomSetForSajangoth)
'''
print (randomListForSagai)
print (randomListForMehendi)
print (randomListForSangeet)
print (randomListForVarmala)
print (randomListForPhere)
print (randomListForSajangoth)
'''

sagai=("Ring","Sweets","Flowers","Dry Fruits","Beetel Leaf","Kumkum","Rice","Jaggery","Coconut","Fruits","Mauli")
mehendi=("Indian","Arabic","Indo-Arabic","Moroccan","Glitter","Mughlai","Bridal","Multi Colored","Tribal","Geometric","Floral")
sangeet=("Bhangra","Hip Hop","Salsa","Dandiya","Garba","Ghoomar","Bollywood","Disco","Freestyle","Rock n Roll","Jazz")
varmala=("Pink Rose","Red Rose","Jasmine","Marigold","Orange Rose","Orchids","Lily","White Rose","Tulips","Rajnigandha","Yellow Rose")
phere=("Hast Milap","Kanyadan","Havan","Gath Bandhan","Saat Phere","Aashirvad","Sindoor","Mangalsutra","Chunri","Vachan","Rajaham")
sajangoth=("Pastries","Ice-cream","Gulab Jamun","Imarti","Jalebi","Rasmalai","Phirni","Kulfi","Malpua","Rabri","Sandesh")

combinationForSagai     = list(combinations(sagai, 5))
combinationForMehendi   = list(combinations(mehendi, 5))
combinationForSangeet   = list(combinations(sangeet, 5))
combinationForVarmala   = list(combinations(varmala, 5))
combinationForPhere     = list(combinations(phere, 5))
combinationForSajangoth = list(combinations(sajangoth, 5))

file=open('Tickets.txt','w')

'''
#perm = permutations(number)
#print(len(combinationForMehendi))
#for i in combinationForSagai :
    #print(i)

#print("random order")
blankList=["blank","blank","blank","blank"]
for i in range(52):
    sagaiRow=list(combinationForSagai[randomListForSagai[i]])
    sagaiRow=sagaiRow+blankList
    random.shuffle(sagaiRow)
    mehendiRow=list(combinationForMehendi[randomListForMehendi[i]])
    mehendiRow=mehendiRow+blankList
    random.shuffle(mehendiRow)
    sangeetRow=list(combinationForSangeet[randomListForSangeet[i]])
    sangeetRow=sangeetRow+blankList
    random.shuffle(sangeetRow)
    varmalaRow=list(combinationForVarmala[randomListForVarmala[i]])
    varmalaRow=varmalaRow+blankList
    random.shuffle(varmalaRow)
    phereRow=list(combinationForPhere[randomListForPhere[i]])
    phereRow=phereRow+blankList
    random.shuffle(phereRow)
    sajangothRow=list(combinationForSajangoth[randomListForSajangoth[i]])
    sajangothRow=sajangothRow+blankList
    random.shuffle(sajangothRow)
    print("Ticket -",i)
    print ("Sagai     --",sagaiRow)
    print ("Mehendi   --",mehendiRow)
    print ("Sangeet   --",sangeetRow)
    print ("Varmala   --",varmalaRow)
    print ("Phere     --",phereRow)
    print ("Sajangoth --",sajangothRow)
    print("\n")
    file.write("Ticket -"+str(i))
    file.write("\n")
    file.write("Sagai     --"+str(sagaiRow))
    file.write("\n")
    file.write("Mehendi   --"+str(mehendiRow))
    file.write("\n")
    file.write("Sangeet   --"+str(sangeetRow))
    file.write("\n")
    file.write("Varmala   --"+str(varmalaRow))
    file.write("\n")
    file.write("Phere     --"+str(phereRow))
    file.write("\n")
    file.write("Sajangoth --"+str(sajangothRow))
    file.write("\n")
    file.write("\n")
'''

sagaiFinal=""
mehendiFinal=""
sangeetFinal=""
varmalaFinal=""
phereFinal=""
sajangothFinal=""

for i in range(52):
    sagaiRow=list(combinationForSagai[randomListForSagai[i]])
    random.shuffle(sagaiRow)
    sagaiFinal=sagaiRow[0]+", blank , "+sagaiRow[1]+", blank , blank , "+sagaiRow[2]+" , "+sagaiRow[3]+" , blank , "+sagaiRow[4]
    
    mehendiRow=list(combinationForMehendi[randomListForMehendi[i]])
    random.shuffle(mehendiRow)
    mehendiFinal="blank , "+mehendiRow[0]+" , "+mehendiRow[1]+" , "+mehendiRow[2]+" , blank , "+mehendiRow[3]+" , blank , "+mehendiRow[4]+" , blank "
    
    sangeetRow=list(combinationForSangeet[randomListForSangeet[i]])
    random.shuffle(sangeetRow)
    sangeetFinal=sangeetRow[0]+" , blank , "+sangeetRow[1]+" , blank , "+sangeetRow[2]+" , blank , "+sangeetRow[3]+" , blank , "+sangeetRow[4]

    varmalaRow=list(combinationForVarmala[randomListForVarmala[i]])
    random.shuffle(varmalaRow)
    varmalaFinal="blank , blank , "+varmalaRow[0]+" , "+varmalaRow[1]+" , "+varmalaRow[2]+" , "+varmalaRow[3]+" , "+varmalaRow[4]+" , blank , blank "

    phereRow=list(combinationForPhere[randomListForPhere[i]])
    random.shuffle(phereRow)
    phereFinal=phereRow[0]+" , blank , "+phereRow[1]+" , blank , "+phereRow[2]+" , blank , "+phereRow[3]+" , blank , "+phereRow[4]

    sajangothRow=list(combinationForSajangoth[randomListForSajangoth[i]])
    random.shuffle(sajangothRow)
    sajangothFinal="blank , "+sajangothRow[0]+" , blank , "+sajangothRow[1]+" , blank , "+sajangothRow[2]+" , "+sajangothRow[3]+" , "+sajangothRow[4]+" , blank "

    print("Ticket -",i)
    print ("Sagai     --",sagaiFinal)
    print ("Mehendi   --",mehendiFinal)
    print ("Sangeet   --",sangeetFinal)
    print ("Varmala   --",varmalaFinal)
    print ("Phere     --",phereFinal)
    print ("Sajangoth --",sajangothFinal)
    print("\n")
    file.write("Ticket -"+str(i))
    file.write("\n")
    file.write("Sagai     --"+sagaiFinal)
    file.write("\n")
    file.write("Mehendi   --"+mehendiFinal)
    file.write("\n")
    file.write("Sangeet   --"+sangeetFinal)
    file.write("\n")
    file.write("Varmala   --"+varmalaFinal)
    file.write("\n")
    file.write("Phere     --"+phereFinal)
    file.write("\n")
    file.write("Sajangoth --"+sajangothFinal)
    file.write("\n")
    file.write("\n")

file.close()

