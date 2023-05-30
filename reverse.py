import cv2
import numpy as np

cap=cv2.VideoCapture('flower.mp4')
opened= cap.isOpened()
frames= cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps= cap.get(cv2.CAP_PROP_FPS)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width= cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fourcc= cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter('reverse.mp4', fourcc, fps, (int(width*0.5), int(height*0.5)))
print("No of Frames are: {}".format(frames))
print("fp is: {}".format(fps))
frame_index=frames-1

if(opened):
    while(frame_index!=0):
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret, frame = cap.read()
        frame=cv2.resize(frame,(int(width*0.5),int (height*0.5)))
        cv2.imshow('winname',frame)
        out.write(frame)
        frame_index=frame_index-1
        if(frame_index%100==0):
            print(frame_index)
          
out.release()
cap.release()
cv2.destroyAllWindows()