#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 18:55:44 2021

@author: fiture
"""

import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxhands=2, detectioncon=0.5, trackcon=0.5):
        self.mode = mode
        self.maxhands = maxhands
        self.detectioncon = detectioncon
        self.trackcon = trackcon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxhands, self.detectioncon, self.trackcon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):        
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:                                        
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
                    
    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 25, (225, 0, 255), -1)
        return lmList

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()    
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if lmList:
            print(lmList[4])
        
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
                
        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
        cv2.imshow('IMage', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    cap.release()        
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()