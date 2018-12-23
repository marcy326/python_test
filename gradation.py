# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:25:15 2018

@author: marcy
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def triangle(x, max_x):
    y = x % (2 * max_x)
    if y >= max_x:
        y = 2 * (max_x) - y -1
    return int(y)

def plus_sin(x, max_x):
    y = -1 * (max_x-1) / 2 * np.cos(np.pi / max_x * x) + max_x/2
    return y

func1 = np.frompyfunc(triangle, 2, 1)
func2 = np.frompyfunc(plus_sin, 2, 1)

X = np.arange(256*8)
Y1 = func1(X, 256)
Y2 = func2(X, 256)

#plt.plot(X, Y1)
#plt.plot(X, Y2)
#plt.show()

width=1024
height=512

imageArray1 = np.zeros((height, width, 3), np.uint8)
imageArray2 = np.zeros((height, width, 3), np.uint8)


for w in range(width):
    imageArray1[:,w,:] = func1(w, 256);
    imageArray2[:,w,:] = func2(w, 256);


cv2.imwrite("gra1.bmp", imageArray1)
cv2.imwrite("gra2.bmp", imageArray2)

