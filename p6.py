#!usr/bin/python

list1 = [1,2,3,4]
list2 = [3,6,7,8]
list3 = [12,24,36,48]

def MaxListAVG():
    maxList=[]
    for list in [list1,list2,list3]:
        if len(list)>1:
            list.sort()
            list = list[::-1]
            maxList.append(list[0])
            maxList.append(list[1])
        else:
            maxList.append(list[0])
    return sum(maxList)/(len(maxList)*1.0)
    
def MinListAVG():
    minList=[]
    for list in [list1,list2,list3]:
        if len(list)>1:
            list.sort()
            minList.append(list[0])
            minList.append(list[1])
        else:
            minList.append(list[0])
    return sum(minList)/(len(minList)*1.0)
    
print 'Average of MaxList:',MaxListAVG()
print 'Average of MinList:',MinListAVG()

