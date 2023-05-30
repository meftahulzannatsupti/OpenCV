import cv2
import numpy as np
print(cv2.__version__)
img=np.zeros((500,500))
img[:,:]=100
img=img[:,:]+10
img[100:200,200:300]=255
cv2.imwrite('simp.jpg',img)