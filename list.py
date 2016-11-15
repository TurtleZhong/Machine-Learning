#! /usr/bin/python
#Filename: list.py

shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist), 'items to purchase.'
print 'These items are:',
for i in shoplist:
    print i,
print '\n'
shoplist.append(5)
temp = shoplist[4] + 6
print  temp
print shoplist
del shoplist[0]
print '\n', shoplist

zoo = ('wolf', 'elephant', 'penguin')
print len(zoo)

new_zoo = ('monkey', 'dolphin', zoo)
print new_zoo
print len(new_zoo)


ab = {
    'kobe' : 'kobe@bit.edu.cn',
    'James' : 'James@bit.edu.cn'
}

print "Kobe's address is %s" %ab['kobe']

ab['cc'] = 'cc@bit.edu.cn'
print ab

for name, address in ab.items():
    print 'Contact %s at %s' %(name, address)

if 'cc' in ab:
    print 'yeah'

string = 'swaroop'
print string[1:3]

cd = ab
print cd

if string.startswith('swa'):
    print 'Yes, the string start with "Swa"'

if string.find('roo'):
    print 'Finf roo'

dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]
print 'The length of dataSet is %s.' %(len(dataSet))
count = 0
for featVec in dataSet:
    print featVec[-1]




