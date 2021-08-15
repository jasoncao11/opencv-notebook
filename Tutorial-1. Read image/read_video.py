# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)

# 3:cv2.CAP_PROP_FRAME_WIDTH
# 4:cv2.CAP_PROP_FRAME_HEIGHT
print(cap.get(3))
print(cap.get(4))

ret, frame = cap.read()
while True:
  if frame is not None:
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     cv2.imshow("preview", gray)
  ret, frame = cap.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break
 
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)