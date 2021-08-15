# -*- coding: utf-8 -*-
import cv2
import numpy as np
    
img = cv2.imread('../data/gradient.png', 0)

_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)

cv2.imshow('img', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)

cv2.waitKey(0)
cv2.destroyAllWindows()