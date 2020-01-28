#!usr/bin/python

def countWord(x):
    x = x.split(' ')
    return len(x);
    
def countChar(x):
    return sum(len(i) for i in x.split(' '))
    
    
def analyseFile(i,x):
    f = open('output.txt','a')
    f.write("Line "+str(i)+": Character count - "+str(countChar(x))+" and word count - "+str(countWord(x))+"\n")
    f.close()

f = open('input.txt','r')
j=0
for i in f:
    j +=1
    analyseFile(j,i)
f.close()
    
