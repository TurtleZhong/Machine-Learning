##This program is a simple demo for decision tree algorithm by TurtleZhong
##You can find this code in the book of <<The practice of Machine Learning>>
#! /usr/bin/python
# Filename: test1.py

from math import log
import operator
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
##This is the dataSet and just for test
def createDataSet():
    mydataSet = [[1, 1, 1, 'yes'],
                 [1, 1, 0, 'maybe'],
                 [1, 0, 1, 'no'],
                 [0, 1, 1, 'no'],
                 [0, 1, 1, 'no']]
    #print 'The length of dataSet is %s.' % (len(mydataSet))
    labels = ['no surfacing', 'flippers', 'others']
    return mydataSet, labels



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
        #print featList
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        #print infoGain
        if infoGain > bestInfoGain :
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classCount:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def creatTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueValues = set(featValues)
    for value in uniqueValues:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = creatTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    print myTree
    return myTree





##This is just test the matplotlib
decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")
leafNode = dict(boxstyle = "roubd4", fc = "0.8")
arrow_args = dict(arrowstyle = "<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy = parentPt, \
                            xycoords = 'axes fraction',\
                            xytext = centerPt, textcoords = 'axes fraction',\
                            va = "center", ha = "center", bbox = nodeType, arrowprops = arrow_args)
def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon = False)
    plotNode(U'decision Node', (0.5,0.1),(0.1,0.5), decisionNode)
    plt.show()



#calcShannonEnt(mydataSet)
#splitDataSet(mydataSet, 1, 0)
mydataSet, labels = createDataSet()
chooseBestFeatureToSplit(mydataSet)
creatTree(mydataSet,labels)
#createPlot()

