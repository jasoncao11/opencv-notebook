# -*- coding: utf-8 -*-
import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    #显示坐标
    print(x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x) + ', ' + str(y)
        cv2.putText(img, strxy, (x, y), font, 0.5, (255,255,0), 2)
        cv2.imshow('image', img)
    #显示BGR每个channel大小
    if event == cv2.EVENT_RBUTTONDOWN:
        #print(y, x)
        blue = img[y, x, 0]
        #print(blue)
        green = img[y, x,  1]
        #print(green)
        red = img[y, x,  2]
        #print(red)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strbgr = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strbgr, (x,y), font, 0.5, (0,255,255), 2)
        cv2.imshow('image', img)
    #显示点击处的颜色
    if event == cv2.EVENT_LBUTTONDBLCLK:
        blue = img[y, x, 0] 
        green = img[y, x, 1]
        red = img[y, x, 2]        
        mycolorimage = np.zeros((512, 512, 3), np.uint8)
        mycolorimage[:] = [blue, green, red]
        cv2.imshow('color', mycolorimage)
    #直线连接点与点
    if event == cv2.EVENT_RBUTTONDBLCLK:  
        cv2.circle(img, (x,y), 3, (0, 0, 255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)
        
img = cv2.imread('../data/messi5.jpg')
print(img.shape)
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()