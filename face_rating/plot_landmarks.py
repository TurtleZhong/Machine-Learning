#! /usr/bin/python
#Filename: plot_landmarks.py

import matplotlib.pyplot as plt
import numpy as np



with open("./landmarks.txt") as landmarks:
    data = landmarks.readlines()[1:2]
    data = data[0].split()

    x_data = data[0:137:2]
    y_data = data[1:137:2]

    x = np.array(x_data)
    y = np.array(y_data)

    plt.scatter(x,y, c = 'r', s=25,alpha=0.4,marker='o')
    plt.show()




