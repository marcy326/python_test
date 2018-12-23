# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 14:06:11 2018

@author: marcy
"""

import time
import numpy as np
import math
from matplotlib import pyplot as plt

i = 300

fig, ax = plt.subplots(1, 1)

X = np.zeros(3)
Y = np.zeros(3)


t1 = time.time()

ims = []
for t in range(i):
    rad = math.radians(t)
    U = (np.cos(rad), 0, np.cos(rad))
    V = (0, np.sin(rad), np.sin(rad))
    Q = ax.quiver(X, Y, U, V, color=('r','g','b'))
    ims.append(Q)
fig.clear()

t2 = time.time()

ims = []
for t in range(i):
    rad = math.radians(t)
    U = (np.cos(rad), 0)
    V = (0, np.sin(rad))
    U += (U[0] + U[1],)
    V += (V[0] + V[1],)
    Q = ax.quiver(X, Y, U, V, color=('r','g','b'))
    ims.append(Q)
fig.clear()

t3 = time.time()

ims = []
for t in range(i):
    rad = math.radians(t)
    U12 = (np.cos(rad), 0)
    V12 = (0, np.sin(rad))
    U = U12 + (U12[0] + U12[1],)
    V = V12 + (V12[0] + V12[1],)
    Q = ax.quiver(X, Y, U, V, color=('r','g','b'))
    ims.append(Q)
fig.clear()

t4 = time.time()

ims = []
for t in range(i):
    rad = math.radians(t)
    U = np.array((np.cos(rad), 0))
    np.append(U, U[0]+U[1])
    V = np.array((0, np.sin(rad)))
    np.append(V, V[0]+V[1])
    Q = ax.quiver(X, Y, U, V, color=('r','g','b'))
    ims.append(Q)
fig.clear()

t5 = time.time()

plt.close(fig)

print("time1:", t2-t1)
print("time2:", t3-t2)
print("time3:", t4-t3)
print("time4:", t5-t4)