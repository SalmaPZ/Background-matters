import cv2  
import numpy as np  
  
video = cv2.VideoCapture(0) 
image = cv2.imread("me.jpeg") 
  
while True: 
  
    ret, frame = video.read() 
    print(frame)
    
  //add code (refer step 1) 
  
  
    //add code(refer step 2)
  
    //add code(refer step 3)
  
   //add code(refer step 4)
  
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
video.release() 
cv2.destroyAllWindows() 
