##This program is a simple demo for decision tree algorithm by TurtleZhong
##You can find this code in the book of <<The practice of Machine Learning>>
#! /usr/bin/python
# Filename: test1.py

from math import log

##This is the dataSet and just for test
mydataSet = [[1, 1, 'yes'],
           [1, 1, 'yes'],
           [1, 0, 'no'],
           [0, 1, 'no'],
           [0, 1, 'no']]
print 'The length of dataSet is %s.' %(len(mydataSet))

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    #creat dictionary for trait
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        #print labelCounts

    #print labelCounts
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    #print 'shannonEnt is %s' %shannonEnt
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDatSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            #print featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            #print reducedFeatVec
            retDatSet.append(reducedFeatVec)

    #print retDatSet
    return retDatSet

def chooseBestFeatureToSplit(dataSet):
    numFeature = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeature):
        featList = [example[i] for example in dataSet]
        print featList
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        print infoGain
        if infoGain > bestInfoGain :
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


#calcShannonEnt(mydataSet)
#splitDataSet(mydataSet, 1, 0)
chooseBestFeatureToSplit(mydataSet)

