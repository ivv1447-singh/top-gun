#!usr/bin/python

import collections

def checkE(x):
    x = collections.Counter(x)
    for i in x:
        if(i=='e'):
            if(x[i]==2):
                return True
    return False
    
print checkE(raw_input('Enter a String: '))

