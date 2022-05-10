import cv2
import numpy as np
import requests
import time

from requests.api import request 
urlarray = ['192.168.0.106','192.168.0.107','192.168.0.105','192.168.0.106']

# img1 = cv2.VideoCapture(0)
# img0 = img1[-300:0,:]
i = 0
c = 0
d = 1
cal=170
cal2=150
hd=10
####################################################################################################

def get_coordi():
    cv2.destroyAllWindows()
    cropped_img=get_frame()[cal:,:]
    new_img = cropped_img.copy()
    img_dilation=hsvimage(cropped_img)
    # cv2.imshow('Crop',cropped_img)
    # cv2.waitKey(0)
    x_cor,y_cor=getContours(img_dilation)
    #cv2.circle(new_img, (int(x_cor), int(y_cor)), 3, (0, 0, 255), 3, cv2.FILLED)
    #cv2.imshow('Video', new_img)
    bot=[x_cor,y_cor]
    return bot


def hsvimage(new_img):
    hsv_frame = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
    low_green=np.array([60,30,20])
    high_green=np.array([95,255,255])
    green_mask=cv2.inRange(hsv_frame,low_green,high_green)
    green = cv2.bitwise_and(new_img,new_img,mask=green_mask)
    kernel = np.ones((7, 7), np.uint8)
    img_erosion = cv2.erode(green_mask, kernel, iterations=1)
    img_dilation = cv2.dilate(img_erosion,kernel,iterations=1)
    return img_dilation


def countour_count():
    # istrue, new_img = img1.read()
    new_img = get_frame()[:cal,:]
    image = hsvimage(new_img)
    contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    number_of_objects_in_image= len(contours)
    return number_of_objects_in_image


##################################################################################################

origin=[[340-hd,159-cal2],
        [367-hd,159-cal2],
        [393-hd,159-cal2],
        [423-hd,159-cal2]]

p = [[[340,429-cal], [69,429-cal]],
    [[379,453-cal], [71,453-cal]],
    [[409,453-cal], [619,453-cal]],
    [[440,421-cal], [619,421-cal]]]


##################################################################################################


def get_frame():
    ret,frame = capture.read()
    return frame

##################################################################################################

def frwdf():
    r=requests.get(url="http://" + urlarray[j]+"/Forward1")
    time.sleep(0.2)

def frwds():
    r=requests.get(url="http://" + urlarray[j]+"/Forward2")
    time.sleep(0.2)

def sl():
    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
    time.sleep(0.1/3)

def sr():
    r = requests.get(url = "http://" + urlarray[j]+"/sright")
    time.sleep(0.1/3)

#################################################################################################

def frwd(a,b):
    if(abs(a)>100):
        if(a>0):
            frwdf()
            if(b>10):
                sr()
                sr()
                sr()
                # sr()
                frwdf()
                # sl()
            elif(b>5):
                sr()
                sr()
                frwdf()
            elif(b<-10):
                sl()
                sl()
                sl()
                # sl()
                frwdf()
                # sr()
            elif(b<-5):
                sl()
                sl()
                frwdf()
        if(a<0):
            frwdf()
            if(b>10):
                sl()
                sl()
                sl()
                # sl()
                frwdf()
                # sr()
            elif(b>5):
                sl()
                sl()
                frwdf()
            elif(b<-10):
                sr()
                sr()
                sr()
                # sr()
                frwdf()
                # sl()
            elif(b<-5):
                sr()
                sr()
                frwdf()

    elif(abs(a)<100):
        if(a>0):
            frwds()
            if(b>10):
                sr()
                sr()
                frwds()
                sl()
            elif(b>5):
                sr()
                frwds()
            elif(b<-10):
                sl()
                sl()
                frwds()
                sr()
            elif(b<-5):
                sl()
                frwds()
        if(a<0):
            frwds()
            if(b>10):
                sl()
                sl()
                frwds()
                sr()
            elif(b>5):
                sl()
                frwds()
            elif(b<-10):
                sr()
                sr()
                frwds()
                sl()
            elif(b<-5):
                sr()
                frwds()

###############################################################################################

def cordinate(n):
    x_arr = n[::2]
    x= sum(x_arr)
    x = x / len(x_arr)

    y_arr = n[1::2]
    y = sum(y_arr)
    y = y / len(y_arr)
    print(x,y)
    return x,y


def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area>5 and area < 2000):
            approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
            cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)
            n = approx.ravel()
            x, y = cordinate(n)
            # print(x, y)
            return x,y
    return [-1, -1]    

# url="http://192.168.0.3:8080/video"
# Put 0 for webcam and link for IP webcam or enter 1 if using Droidcam via USB
capture = cv2.VideoCapture(1)
# URL = "http://192.168.0.106/Flip"


## (Alternate Method) Alternative code if first code does not work ##

# contours, hierarchy = cv2.findContours(img_erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# for contour in contours:
#     area = cv2.contourArea(contour)
#     if (area>10 and area<200):
#         approx = cv2.approxPolyDP(contour, 0.009 * cv2.arcLength(contour, True), True)
#         cv2.drawContours(new_img, [approx], 0, (0, 0, 255), 5)
#         n = approx.ravel()
#         x_cor,y_cor=cordinate(n)
#         print(x_cor,y_cor)
#         cv2.circle(new_img, (int(x_cor), int(y_cor)), 3, (0, 0, 255), 3, cv2.FILLED)
#         arr.append([int(x_cor), int(y_cor)])
    

# arr.append([int(x_cor), int(y_cor)])
# value = sorted(arr, key=lambda k: k[0])
# print(value)
#print(values)

# bot3=value[1]
# bot2=value[2]
# bot1=value[3]

#  **

#######################################  START  #################################################################

print(countour_count())
for j in range(4):
    if (countour_count()==4):
        r=requests.get(url="http://" + urlarray[j]+"/Forward1")
        r=requests.get(url="http://" + urlarray[j]+"/Forward1")
        print('F')
        time.sleep(0.4)
    c = 0
    d = 1
    bot = get_coordi()

    ###########################  REACHES FIRST CHECKPOINT  #####################################

    while (p[j][0][1]-bot[1]>10):
        frwd(p[j][0][1]-bot[1],bot[0]-p[j][0][0])
        bot=get_coordi() 
        print(bot) 
    
    ###########################  TURNS LEFT OR RIGHT 90 DEGREES  #####################################

    c=1
    d = 0
    time.sleep(1)
    if(j==2 or j==3): 
        r=requests.get(url="http://" + urlarray[j]+"/Left")
        time.sleep(0.3)
        r = requests.get(url = "http://" + urlarray[j]+"/sleft")
        r = requests.get(url = "http://" + urlarray[j]+"/sleft")
        # r = requests.get(url = "http://" + urlarray[j]+"/sleft")
        # r = requests.get(url = "http://" + urlarray[j]+"/sleft")
    else:    
        r = requests.get(url = "http://" + urlarray[j]+"/Right") #turn
        time.sleep(0.3)
        r = requests.get(url = "http://" + urlarray[j]+"/sright")
        r = requests.get(url = "http://" + urlarray[j]+"/sright")
        # r = requests.get(url = "http://" + urlarray[j]+"/sright")
        # r = requests.get(url = "http://" + urlarray[j]+"/sright")
    
    bot = get_coordi()

    ######################  REACHES SECOND CHECKPOINT  #########################################
   
    while (abs(bot[0]-p[j][1][0])>20):
        frwd(bot[0]-p[j][1][0],bot[1]-p[j][1][1])
        bot=get_coordi() 
        print(bot) 

    ######################   FLIPS THE LOAD  #########################################
    
    r = requests.get(url = "http://"+urlarray[j]+"/Flip")
    time.sleep(0.9)
    print("Flip")
    
    ########################  TURNS 180 DEGREES TO REVERSE DIRECTION  #######################################

    if(j<=1):
        r = requests.get(url = "http://" + urlarray[j]+"/Right")
        r = requests.get(url = "http://" + urlarray[j]+"/Right")
        # r=requests.get(url="http://"+urlarray[j]+"/sleft")
        # r=requests.get(url="http://"+urlarray[j]+"/sleft")
        # r=requests.get(url="http://"+urlarray[j]+"/sleft")
    else:    
        r = requests.get(url = "http://" + urlarray[j]+"/Left")
        r = requests.get(url = "http://" + urlarray[j]+"/Left")
        # r=requests.get(url="http://"+urlarray[j]+"/sright")
        # r=requests.get(url="http://"+urlarray[j]+"/sright")
    time.sleep(0.5)
    bot = get_coordi()

    ######################### REACHES THE FIRST CHECK POINT AGAIN #####################################
    
    while (abs(p[j][0][0]-bot[0])>15):
        frwd(bot[0]-p[j][0][0],bot[1]-p[j][0][1])
        bot=get_coordi() 
        print(bot) 

    #######################  TURNS 90 DEGREES  ######################################
        
    if(j<=1):
        r = requests.get(url = "http://" + urlarray[j]+"/Left")
        r = requests.get(url = "http://" + urlarray[j]+"/sleft")
        r = requests.get(url = "http://" + urlarray[j]+"/sleft")
    else:    
        r = requests.get(url = "http://" + urlarray[j]+"/Right")
        r=requests.get(url="http://"+urlarray[j]+"/sright")
        r=requests.get(url="http://"+urlarray[j]+"/sright")
        # r = requests.get(url = "http://" + urlarray[j]+"/Right")
    time.sleep(0.5)
    bot = get_coordi()

    #######################   REACHES ORIGIN AGAIN  ######################################

    while (bot[1]-origin[j][1]>10):
        frwd(origin[j][1]-bot[1],bot[0]-origin[j][0])
        bot=get_coordi() 
        print(bot)  

    ########################   THE END   #####################################    

    r=requests.get(url="http://"+urlarray[j]+"/Forward1")
    
    r=requests.get(url="http://"+urlarray[j]+"/Forward1")
    
    # r=requests.get(url="http://"+urlarray[j]+"/Forward")
    j=j+1    

    # cv2.imshow("Bots", green)
    # r = requests.get(url=URL)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()