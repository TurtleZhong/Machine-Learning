#! /usr/bin/python
# Filename: test3.py

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print M

col2 = []
for row in M:
    col2.append(row[1] + 1)

print col2

col2 = [row[1] for row in M if row[1] < 6]
print col2

dig = [M[i][i] for i in range(0,3)]
print "dig = " , dig

doubles = [c * 2 for c in "springer"]
print doubles

G = [sum(row) for row in M]
print G

D = {'food':'Spam', 'quantity': 4, 'color':'pink'}
print D["food"]

rec = {'name':{'first':'Bob', 'last':'Smith'},
       'job':['dev','mgr'],
       'age':40.5}
rec['job'].append('jjj')
print rec['job']

Ks = list(D.keys())
print Ks
Ks.sort()
print Ks

for key in Ks:
    print key, '->',D[key]
for key in sorted(D):
    print key, '->', D[key]


T = (1, 2)
print T[0]

if type(D) == dict:
    print 'yes'

class Worker:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)
        return self.pay

bob = Worker('bob smith', 5000)

print bob.lastName()
print bob.giveRaise(.1)