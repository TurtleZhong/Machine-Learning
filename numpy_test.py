##This code just for learning numpy
#! /usr/bin/python
# Filename: test1.py

import numpy as np
import matplotlib.pyplot as plt

a = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print a
print a.shape
b = np.array([[1, 2, 3, 4], [1, 2, 3, 4]], dtype=np.float)

print b

plt.figure(figsize=(10,6),dpi=80)
plt.subplot(111)
X = np.linspace(-np.pi, np.pi, num=256, endpoint=True)
C,S = np.cos(X), np.sin(X)+1

ax = plt.gca() #get current axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))


plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$']) #for latex format

plt.xlim(-4, 4)

t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color = 'blue', linewidth = 1.5, linestyle = "--")
plt.scatter([t,],[np.cos(t)],50, color = 'blue')

plt.plot([t, t], [0, np.sin(t)], color = 'red', linewidth = 1.5, linestyle = "--")
plt.scatter([t,],[np.sin(t)],50, color = 'red')

plt.plot(X, S, color = "red", linewidth = 2.5, linestyle = "-", label = "sine", alpha = 1)
plt.plot(X, C, color = "blue", linewidth = 2.5, linestyle = "-", label = "cosine")
plt.legend(loc = 'upper left', frameon = False)

#plt.show()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'b^', t2, f(t2), 'red')
plt.show()
