#! /usr/bin/python
#Filename: decision_tree.py
from IPython.display import Image
import pydot
from sklearn import tree
from sklearn.datasets import  load_iris
import numpy as np
# iris = load_iris()
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(iris.data, iris.target)
# print iris
#
# dot_data = tree.export_graphviz(clf, out_file=None,
#                          feature_names=iris.feature_names,
#                          class_names=iris.target_names,
#                          filled=True, rounded=True,
#                          special_characters=True)
# graph = pydot.graph_from_dot_data(dot_data)
# graph.write_pdf("iris.pdf")
# Image(graph.create_png())

dataset = np.loadtxt("treedata.txt",delimiter=",")
print dataset
X = dataset[:,0:2]
print X
Y = dataset[:,2]
print Y
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X, Y)
with open("fish_or_not.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
