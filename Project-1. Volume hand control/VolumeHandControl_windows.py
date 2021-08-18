# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np
import math
import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volrange = volume.GetVolumeRange()
minvol = volrange[0]
maxvol = volrange[1]

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectioncon=0.7)
volbar = 400
volper = 0

while True:
    success, img = cap.read()    
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if lmList:

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        
        cx, cy = (x1 + x2)//2, (y1 + y2)//2
        
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), -1)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), -1)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), -1)
        
        length = math.hypot(x2-x1, y2-y1)
        
        # hand range 50-300
        # volume range -64-0
        vol = np.interp(length, [50, 300], [minvol, maxvol])
        print(length, vol)
        volume.SetMasterVolumeLevel(vol, None)
        volbar = np.interp(length, [50, 300], [400, 150])
        volper = np.interp(length, [50, 300], [0, 100])
        
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), -1)
            
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volbar)), (85, 400), (255, 0, 0), -1)
    cv2.putText(img, f'{int(volper)} %', (40,450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 3)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
            
    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 3)
    
    cv2.imshow('IMage', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   
cap.release()        
cv2.destroyAllWindows()