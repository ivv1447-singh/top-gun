#!usr/bin/python

def IP(x):
    ip = '1'*x + '0'*(32 - x)
    r = str(int(ip[:8], 2)) + '.' + str(int(ip[8:16], 2)) + '.' +str(int(ip[16:24], 2)) + '.' + str(int(ip[24:32], 2))
    return r
    
print IP(input())

