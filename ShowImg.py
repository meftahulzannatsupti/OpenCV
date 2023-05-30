import cv2
import numpy as np
#channel order is BGR
image= cv2.imread('nature.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Test Image',image)
cv2.waitKey(5000)
