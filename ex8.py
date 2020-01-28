#!usr/bin/python

import xml.etree.ElementTree as xml

e = xml.parse('bookstore.xml').getroot()

data={}
for i in e.findall('book'):
    data[i.attrib['category']]={'title':i[0].text, 'author': i[1].text, 'year':i[2].text, 'price':i[3].text}
    
print 'Book category - CHILDERN:',data['CHILDREN']

print 'Book category - Web@Author:',data['WEB']['title']
print 'Book category - Web@Price:',data['WEB']['price']

