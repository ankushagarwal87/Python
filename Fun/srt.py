f=open("[fmovies.se] Inside Out - Full.srt",'r')
y=open("data.txt",'w')
d=f.read()
x=d.split('\n')
#print (x)
for i in x:
    #print (i[0])
    if(len(i)>0):
        if (i[0].isnumeric()):
            continue
        else:
            y.write(i)
            #y.write('\n')
    y.write('\n')
y.close()
