#! /usr/bin/python
#Filename: generete_data.py

import matplotlib as plt
import numpy as np

#loading the data and get the face landmarks data
#each image we have 68 points


feature_data_origin = "./face_feature_data/SCUT-FBP-"
suffix = "_det_0.pts"
landmarks = open("landmarks.txt", 'w')
for i in range(0,500):
    feature_data = feature_data_origin + str(i+1) + suffix
    #print feature_data
    #now we got the sequence of original landmarks data

    feature = open(feature_data)
    lines = feature.readlines()[3:71]

    #
    landmarks_data = []
    for line in lines:
        line = line.split()
        list(line)
        landmarks_data.extend(line)

    feature.close()
    #print "Reading sequence", i+1, "sucessfully, Next, we will writing the data to landmarks.txt"

    for item in landmarks_data:
        landmarks.write(item)
        landmarks.write(' ')
    landmarks.write('\n')

print "All done!, Now you get the landmarks in landmarks.txt of 500 image."
landmarks.close()

#print landmarks_data

