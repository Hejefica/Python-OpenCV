import numpy as np
import cv2

img = cv2.imread('CETI Icon.png',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(200,300),(255,255,255),10)
cv2.rectangle(img,(200,250),(500,500),(0,0,255),15)
cv2.circle(img,(447,163), 63, (0,255,0), -1)
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 2, (200,255,155), 13, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()