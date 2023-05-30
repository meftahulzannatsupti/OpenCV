import cv2
import numpy as np
canvas = np.zeros((500,500,3))
#Drawing a line
cv2.line(canvas,(0,0),(100,100),(0,255,0),2, cv2.LINE_4)
cv2.line(canvas,(0,20),(120,120),(0,255,0),2, cv2.LINE_AA)
cv2.imshow('winname',canvas)
cv2.waitKey(20000)
