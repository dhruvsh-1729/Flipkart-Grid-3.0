import cv2 as cv
import numpy as np 
import requests

URL="192.168.0.103"

# Put 0 for webcam and link for IP webcam or enter 1 if using Droidcam via USB
capture=cv.VideoCapture(0)
# 
while True:
    istrue,frame=capture.read()
    
    hsv_frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    low_green=np.array([25,52,72])
    high_green=np.array([102,255,255])
    green_mask=cv.inRange(hsv_frame,low_green,high_green)
    green=cv.bitwise_and(frame,frame,mask=green_mask)
    cv.imshow("Video",frame)
    cv.imshow("Bots",green)
    print("Forward")
    
    r = requests.get(url = "http://" + URL+"/Flip")

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()