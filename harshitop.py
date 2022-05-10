import cv2
import numpy as np
import requests
import time 
urlarray = ['192.168.0.106','192.168.0.103','192.168.0.104','192.168.0.107']

# img1 = cv2.VideoCapture(0)
# img0 = img1[-300:0,:]

def get_coordi():
    cropped_img=get_frame()[135:,:]
    img_dilation=hsvimage(cropped_img)
    # cv2.imshow('Crop',cropped_img)
    # cv2.waitKey(0)
    x_cor,y_cor=getContours(img_dilation)
    # cv2.circle(new_img, (int(x_cor), int(y_cor)), 3, (0, 0, 255), 3, cv2.FILLED)
    bot=[x_cor,y_cor]
    return bot

def get_frame():
    ret,frame = capture.read()
    return frame

def hsvimage(new_img):
    hsv_frame = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
    low_green=np.array([60,30,30])
    high_green=np.array([102,255,255])
    green_mask=cv2.inRange(hsv_frame,low_green,high_green)
    green = cv2.bitwise_and(new_img,new_img,mask=green_mask)
    kernel = np.ones((7, 7), np.uint8)
    img_erosion = cv2.erode(green_mask, kernel, iterations=2)
    img_dilation = cv2.dilate(img_erosion,kernel,iterations=3)
    return img_dilation


def countour_count():
    # istrue, new_img = img1.read()
    new_img = get_frame()[:135,:]
    image = hsvimage(new_img)
    contours, hierarchy = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    number_of_objects_in_image= len(contours)
    return number_of_objects_in_image

cal=120
cal2=110
origin=[[275,115-cal2],
        [306,111-cal2],
        [336,111-cal2],
        [367,111-cal2]]

p = [[[283,367-cal], [70,376-cal]],
    [[315,385-cal], [74,385-cal]],
    [[343,397-cal], [623,402-cal]],
    [[372,367-cal], [616,370-cal]]]

# p1 = []  # the list which stores the clicked points
# p2 = []
# p3 = []
# p4 = []
# i = 0
# for i in range(4):

#     def click_event(event, x, y, flags, params):
#         if event == cv2.EVENT_LBUTTONDOWN:
#             cv2.circle(img, (x, y), 10, (0, 0, 0), -1)
#             cv2.circle(img, (x, y), 5, (255, 255, 255), -1)
#             if (i == 0):
#                 p1.append([x, y])
#                 arr = np.array(p1)
#                 print(p1)
#                 cv2.polylines(img, [arr], False, (255, 0, 0), 4)
#                 cv2.imshow('image', img)
#             elif (i == 1):
#                 p2.append([x, y])
#                 arr = np.array(p2)
#                 print(p2)
#                 cv2.polylines(img, [arr], False, (255, 0, 0), 4)
#                 cv2.imshow('image', img)

#             elif (i == 2):
#                 p3.append([x, y])
#                 arr = np.array(p3)
#                 print(p3)
#                 cv2.polylines(img, [arr], False, (255, 0, 0), 4)
#                 cv2.imshow('image', img)
#             elif (i == 3):
#                 p4.append([x, y])
#                 arr = np.array(p4)
#                 print(p4)
#                 cv2.polylines(img, [arr], False, (255, 0, 0), 4)
#                 cv2.imshow('image', img)


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
            approx = cv2.approxPolyDP(contour, 0.009 * cv2.arcLength(contour, True), True)
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

 
#r=requests.get(url="http://" + urlarray[0]+"/Forward")
#time.sleep(0.2)



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
print(countour_count())
for j in range(4):
    if (countour_count()==4):
        r=requests.get(url="http://"+urlarray[j]+"/Stop")
        print('Stop')  
        r=requests.get(url="http://" + urlarray[j]+"/Forward")
        print('F')
        time.sleep(0.2)
    bot = get_coordi()
    while (p[j][0][1]-bot[1]>30):
        r=requests.get(url="http://" + urlarray[j]+"/Forward")
        print('F1')
        time.sleep(0.2)
        bot  = get_coordi()
        diff=p[j][0][0]-bot[0]
        if (diff>0):
            if (diff>5):
                r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                time.sleep(0.2/3)
                print('SL1')
        elif (diff<0):
            if (abs(diff)>5):
                r = requests.get(url = "http://" + urlarray[j]+"/sright")
                r = requests.get(url = "http://" + urlarray[j]+"/sright")
                time.sleep(0.2/3)
                print('SR1')
        bot=get_coordi() 
        print(bot) 
    time.sleep(1)
    if(j==2 or j==3): 
        r=requests.get(url="http://" + urlarray[j]+"/Left")
        time.sleep(1)
        r = requests.get(url = "http://" + urlarray[j]+"/sleft")
        r = requests.get(url = "http://" + urlarray[j]+"/sleft")
    else:    
        r = requests.get(url = "http://" + urlarray[j]+"/Right") #turn
        time.sleep(1)
        r = requests.get(url = "http://" + urlarray[j]+"/sright")
        r = requests.get(url = "http://" + urlarray[j]+"/sright")
    
    bot = get_coordi()
    print('R')
    if (j==1 or j==0):
        while (bot[0]-p[j][1][0]>20):
            r=requests.get(url="http://" + urlarray[j]+"/Forward")
            print('F2')
            time.sleep(0.2)
            bot = get_coordi()
            diff=p[j][1][1]-bot[1]
            if (diff>0):
                if (diff>5):
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    print('SL2')
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    time.sleep(0.2/3)
            elif (diff<0):
                if (abs(diff)>5):
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    print('SR2')
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    print('SR2')
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    time.sleep(0.2/3)
            bot = get_coordi()
    else:
        while (p[j][1][0]-bot[0]>20):
            r=requests.get(url="http://" + urlarray[j]+"/Forward")
            print('F2')
            time.sleep(0.2)
            bot = get_coordi()
            diff=p[j][1][1]-bot[1]
            if (diff>0):
                if (diff>5):
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    print('SR2')
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    time.sleep(0.2/3)
                    r=requests.get(url="http://"+urlarray[j]+"/sright")
                    time.sleep(0.2/3)
            elif (diff<0):
                if (abs(diff)>5):
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    print('SL2')
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    print('SL2')
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    time.sleep(0.2/3)
            bot = get_coordi()

    r = requests.get(url = "http://"+urlarray[j]+"/Flip")
    time.sleep(0.9)
    print("Flip")
    if(j<=1):
        r = requests.get(url = "http://" + urlarray[j]+"/Right")
        r = requests.get(url = "http://" + urlarray[j]+"/Right")
    else:    
        r = requests.get(url = "http://" + urlarray[j]+"/Left")
        r = requests.get(url = "http://" + urlarray[j]+"/Left")
    time.sleep(0.5)
    bot = get_coordi()
    if(j<=1):
        while (p[j][0][0]-bot[0]>20):
            r=requests.get(url="http://" + urlarray[j]+"/Forward")
            print('F2')
            time.sleep(0.2)
            bot = get_coordi()
            diff=p[j][0][1]-bot[1]
            if (diff>0):
                if (diff>5):
                #anti
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    time.sleep(0.2/3)
            elif (diff<0):
                if (abs(diff)>5):
                #clock
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    time.sleep(0.2/3)
            bot = get_coordi()
        r = requests.get(url = "http://" + urlarray[j]+"/Left")
    else:
        while (bot[0]-p[j][0][0]>20):
            r=requests.get(url="http://" + urlarray[j]+"/Forward")
            print('F2')
            time.sleep(0.2)
            bot = get_coordi()
            diff=p[j][0][1]-bot[1]
            if (diff>0):
                if (diff>5):
                #anti
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    r = requests.get(url = "http://" + urlarray[j]+"/sright")
                    time.sleep(0.2/3)
            elif (diff<0):
                if (abs(diff)>5):
                #clock
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                    time.sleep(0.2/3)
            bot = get_coordi()
        r = requests.get(url = "http://" + urlarray[j]+"/Right")    
    # turn()
    bot = get_coordi()
    while (bot[1]-origin[j][1]>10):
        r=requests.get(url="http://" + urlarray[j]+"/Forward")
        print('F2')
        time.sleep(0.2)
        bot = get_coordi()
        diff=origin[j][0]-bot[0]
        if (diff>0):
            if (diff>5):
            #anti
                r = requests.get(url = "http://" + urlarray[j]+"/sright")
                r = requests.get(url = "http://" + urlarray[j]+"/sright")
                time.sleep(0.2/3)
        elif (diff<0):
            if (abs(diff)>5):
            #clock
                r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                r = requests.get(url = "http://" + urlarray[j]+"/sleft")
                time.sleep(0.2/3)
        bot = get_coordi()
    r=requests.get(url="http://"+urlarray[j]+"/Forward")
    j=j+1    

    # cv2.imshow("Bots", green)
    # r = requests.get(url=URL)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()