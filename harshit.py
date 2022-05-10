# importing Module
import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in  i]
#print(events)

# function click
def click_event(event, x, y, flags, param):
    # Checking Event left Key Down
    if event == cv2.EVENT_LBUTTONDOWN:
        # printing the x and y coordinate
        print(x,', ' ,y)

        # Creating the Text to put on screen
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        # Note -- Can also create string f"{x} , {y}"
        # Putting string at the coordinate the user clicked  
        # cv2.putText(frame, text, coordinate bottom left, font, fontscale, color,thickness)
        cv2.putText(frame, strXY, (x, y), font, .5, (255, 255, 0), 2)

        # Showing the Image
        cv2.imshow('image', frame)

    # Checking Event right Key Down
    if event == cv2.EVENT_RBUTTONDOWN:
        # getting value of blue , green , red at the coordinate clicked
        blue = frame[y, x, 0]
        green = frame[y, x, 1]
        red = frame[y, x, 2]

        # Creating the Text to put on screen
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        # Note -- Can also create string f"{blue} , {green} , {red}"
        # Putting string at the coordinate the user clicked  
        # cv2.putText(frame, text, coordinate bottom left, font, fontscale, color,thickness)
        cv2.putText(frame, strBGR, (x, y), font, .5, (0, 255, 255), 2)

        # Showing the Image
        cv2.imshow('image', frame)

# Reading Image
#frame = np.zeros((512, 512, 3), np.uint8)
cap = cv2.VideoCapture(1)
while True:
    ret,frame = cap.read()
    cv2.imshow('image',frame)
    cv2.setMouseCallback('image',click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Calling Image and added click event
#cv2.setMouseCallback('image', click_event)