# -*- coding: utf-8 -*-
import cv2

#read image
img = cv2.imread('../data/lena.jpg', -1)

#draw line (img, start point, end point, BGR(rgb color picker in reverse order), thickness)
img = cv2.line(img, (0,0), (255,255), (52,255,155), 10)
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10)

#(384,0):upper left point
#(510,128):lower right point
#-1:be filled with the color
img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), -1)

#(447, 63):center point
#63:radius
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

#'openCV':text
#(10,500):start point
#font:font
#4:font size
#(0,0,255):color
#10:thickness
#cv2.LINE_8:line type
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, 'openCV', (10,500), font, 4, (0,0,255), 10, cv2.LINE_8)


cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()