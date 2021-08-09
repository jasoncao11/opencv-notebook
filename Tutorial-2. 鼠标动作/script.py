# -*- coding: utf-8 -*-
import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ', ' + str(y)
        cv2.putText(img, strxy, (x,y), font, 0.5, (255,255,0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0] 
        green = img[x, y, 1]
        red = img[x, y, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strbgr = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strbgr, (x,y), font, 0.5, (0,255,255), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        blue = img[x, y, 0] 
        green = img[x, y, 1]
        red = img[x, y, 2]        
        mycolorimage = np.zeros((512, 512, 3), np.uint8)
        mycolorimage[:] = [blue, green, red]
        cv2.imshow('color', mycolorimage)
    if event == cv2.EVENT_RBUTTONDBLCLK:  
        cv2.circle(img, (x,y), 3, (0, 0, 255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)
        
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()