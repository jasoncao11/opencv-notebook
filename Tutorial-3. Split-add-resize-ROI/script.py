# -*- coding: utf-8 -*-
import cv2
        
img = cv2.imread('../data/messi5.jpg')
img2 = cv2.imread('../data/opencv-logo-white.png')

print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

#The co-ordinates used in the array follow the format of 
#img [y1: y2, x1: x2]
#Therefore, when copying to another part of the image, you need to ensure that (y2-y1) value remains the same, as well as (x2-x1)
#Here's another example to copy messi's head, where Top left coordinates is (200, 60) and bottom right is (270, 140) in x,y format
#messi_head = img[60:140, 200:270]
#img[260:340,100:170] = messi_head

hand = img[140:185, 340:385]
img[200:245, 300:345] = hand

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .2, img2, .8, 0)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()