# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:52:04 2022

@author: Paulo_Vi
"""

import cv2 as cv
import numpy as np

blank = np.zeros((510,510,3), dtype='uint8')
cv.imshow('Blank', blank)
blank[10:320, 10:500] = 0,200,0
cv.imshow('green', blank)
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 08:52:04 2022

@author: Paulo_Vi
"""

import cv2 as cv
import numpy as np

blank = np.zeros((510,510,3), dtype='uint8')
cv.imshow('Blank', blank)
blank[10:320, 10:500] = 0,200,0
cv.imshow('green', blank)



for i in range(120):

    p1 = (255,55+i)
    p2 = (50+i,170) 
    p3 =(255,280-i)
    p4 = (450-i,170)
    cv.line(blank, p1,p2, (0,255,255), 2)
    cv.line(blank, p2,p3, (0,255,255), 2)
    cv.line(blank, p3,p4, (0,255,255), 2)
    cv.line(blank, p4,p1, (0,255,255), 2)
    cv.imshow('Triangle',blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//3), 75, (255,0,0), -1)
cv.imshow('Circle',blank)

for i in range(20):
    cv.rectangle(blank, (180,160+i), (330,179-i), (255,255,255), 1)
    cv.imshow('Rectangle',blank)


cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//3), 75, (255,0,0), -1)
cv.imshow('Circle',blank)


p1 = (255,55)
p2 = (50,170) 
p3 =(255,280)
p4 = (450,170)
cv.line(blank, p1,p2, (0,255,255), 2)
cv.line(blank, p2,p3, (0,255,255), 2)
cv.line(blank, p3,p4, (0,255,255), 2)
cv.line(blank, p4,p1, (0,255,255), 2)
cv.imshow('Triangle',blank)

cv.destroyAllWindows()

cv.putText(blank, 'Ordem e Progresso', (185,175),cv.FONT_HERSHEY_SIMPLEX, 0.45, (255,255,255), 1)
cv.imshow('Text',blank)


cv.waitKey(0)

