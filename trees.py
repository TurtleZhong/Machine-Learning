##This program is a simple demo for decesion tree algorithm by TurtleZhong
##You can find this code in the book of <<The pritice of Machine Learning>>
#! /usr/bin/python
# Filename: test1.py

from math import log

##This is the dataSet and just for test
dataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]
print 'The length of dataSet is %s.' %(len(dataSet))

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    #creat dictionary for trait
    for featVec in dataSet:
        courrentLabel = featVec[-1]
        if courrentLabel not in labelCounts.keys():
            labelCounts[courrentLabel] = 0
        labelCounts[courrentLabel] += 1
        print labelCounts

    #print labelCounts
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    print 'shannonEnt is %s' %shannonEnt
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDatSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            print featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            print reducedFeatVec
            retDatSet.append(reducedFeatVec)

    print retDatSet
    return retDatSet

calcShannonEnt(dataSet)
splitDataSet(dataSet, 1, 0)
