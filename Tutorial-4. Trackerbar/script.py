# -*- coding: utf-8 -*-
import cv2
      
def nothing(x):
    print(x)
    
cv2.namedWindow('image')
cv2.createTrackbar('CP', 'image', 10, 400, nothing)
switch = 'color/gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv2.imread('../data/messi5.jpg')
    pos = cv2.getTrackbarPos('CP', 'image')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, str(pos), (20,150), font, 3, (0,0,255))
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image', img)
        
   
cv2.destroyAllWindows()