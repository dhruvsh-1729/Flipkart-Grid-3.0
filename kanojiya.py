import cv2
import numpy as np
import requests
import time
urlarray = ['192.168.0.104', '192.168.0.9', '192.168.0.8', '192.168.0.10']

# img1 = cv2.VideoCapture(0)
# img0 = img1[-300:0,:]


def countour_count(new_img):
    # istrue, new_img = img1.read()

    hsv_frame = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
    low_green = np.array([60, 30, 50])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(new_img, new_img, mask=green_mask)

    kernel = np.ones((7, 7), np.uint8)
    img_erosion = cv2.erode(green_mask, kernel, iterations=2)

    contours, hierarchy = cv2.findContours(img_erosion,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    number_of_objects_in_image = len(contours)
    return number_of_objects_in_image


origin1 = [232, 41]
origin2 = [267, 44]
origin3 = [298, 40]
origin4 = [327, 42]

p1 = [[230, 320], [8, 325]]
p2 = [[264, 353], [8, 359]]
p3 = [[288, 349], [549, 354]]
p4 = [[322, 322], [551, 329]]

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
    x = sum(x_arr)
    x = x / len(x_arr)

    y_arr = n[1::2]
    y = sum(y_arr)
    y = y / len(y_arr)
    print(x, y)
    return x, y


def getContours(img):

    contours, hierarchy = cv2.findContours(img,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > 10 and area < 2000):
            approx = cv2.approxPolyDP(
                contour, 0.009 * cv2.arcLength(contour, True), True)
            cv2.drawContours(new_img, [approx], 0, (0, 0, 255), 5)
            n = approx.ravel()
            x, y = cordinate(n)
            # print(x_cor, y_cor)
            return x, y
    return [-1, -1]


# url="http://192.168.0.3:8080/video"
# Put 0 for webcam and link for IP webcam or enter 1 if using Droidcam via USB
capture = cv2.VideoCapture(1)
# URL = "http://192.168.0.106/Flip"

while True:

    # r=requests.get(url="http://" + urlarray[0]+"/Forward")
    # time.sleep(0.2)
    arr = []

    istrue, img = capture.read()

    cropped_img = img[:50, :]
    new_img = img

    hsv_frame = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)
    low_green = np.array([60, 30, 50])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(new_img, new_img, mask=green_mask)

    kernel = np.ones((7, 7), np.uint8)
    img_erosion = cv2.erode(green_mask, kernel, iterations=1)
    img_dilation = cv2.dilate(img_erosion, kernel, iterations=2)

    # contours, hierarchy = cv2.findContours(img_erosion,
    #                                        cv2.RETR_TREE,
    #                                        cv2.CHAIN_APPROX_SIMPLE)
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

    x_cor, y_cor = getContours(img_dilation)
    cv2.circle(new_img, (int(x_cor), int(y_cor)),
               3, (0, 0, 255), 3, cv2.FILLED)

    # arr.append([int(x_cor), int(y_cor)])
    # value = sorted(arr, key=lambda k: k[0])
    # print(value)
    # print(values)
    bot = [x_cor, y_cor]
    # bot3=value[1]
    # bot2=value[2]
    # bot1=value[3]

    i = 0

    for i in range(4):

        #  ****************
        for j in range(4):
            # if (countour_count(cropped_img) == 3):
            #     r = requests.get(url="http://"+urlarray[j]+"/Stop")
            #     print('Stop')
            #     r = requests.get(url="http://" + urlarray[j]+"/Forward")
            #     print('F')
            #     time.sleep(0.2)
            if (p1[0][1]-bot[1] > 10):
                r = requests.get(url="http://" + urlarray[j]+"/Forward")
                print('F1')
                time.sleep(0.2)
                diff = p1[0][0]-bot[0]
                if (diff > 0):
                    if (diff > 20):
                        r = requests.get(url="http://" + urlarray[0]+"/sleft")
                        print('SR1')
                elif (diff < 0):
                    if (abs(diff) > 20):
                        r = requests.get(url="http://" + urlarray[0]+"/sright")
                        print('SL1')
                x_cor, y_cor = getContours(img)
                bot = [x_cor, y_cor]
            r = requests.get(url="http://" + urlarray[0]+"/Right")  # turn
            print('R')
            if (p1[1][0]-bot[0] > 10):
                r = requests.get(url="http://" + urlarray[j]+"/Forward")
                print('F2')
                time.sleep(0.2)
                diff = p1[0][1]-bot[1]
                if (diff > 0):
                    if (diff > 20):
                        r = requests.get(url="http://" + urlarray[0]+"/sright")
                        print('SR2')
                    elif (diff < 0):
                        if (abs(diff) > 20):
                            r = requests.get(
                                url="http://" + urlarray[0]+"/sleft")
                            print('SL2')
            r = requests.get(url="http://"+urlarray[0]+"/Flip")
            print("Flip")
            r = requests.get(url="http://"+urlarray[0]+"/Right")
            r = requests.get(url="http://"+urlarray[0]+"/Right")

            if (p1[0][0]-bot[0] > 10):
                diff = p1[0][1]-bot[1]
                if (diff > 0):
                    if (diff > 20):
                        # anti
                        r = requests.get(url="http://" + urlarray[0]+"/sright")
                elif (diff < 0):
                    if (abs(diff) > 20):
                        # clock
                        r = requests.get(url="http://" + urlarray[0]+"/sleft")

            r = requests.get(url="http://" + urlarray[0]+"/Left")
          # turn()
            if (origin1[1]-bot[1] > 20):
                diff = origin1[0]-bot[0]
                if (diff > 0):
                    if (diff > 20):
                        # anti
                        r = requests.get(url="http://" + urlarray[0]+"/sleft")
                elif (diff < 0):
                    if (abs(diff) > 20):
                        # clock
                        r = requests.get(url="http://" + urlarray[0]+"/sright")

   # *********************


#     i=i+1

#     if (bot==[-1,-1]):
        # r=requests.get(url="http://" + urlarray[j]+"/Forward")
        # time.sleep(0.2)

#     else:


#       while (p2[0][1]-bot[1]>20):

#           diff=p2[0][0]-bot[0]
#           if (diff>0):
#               if (diff>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")
#           elif (diff<0):
#               if (abs(diff)>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#       turn()
#       while (p2[1][0]-bot2[0]>10):
#           diff=p2[0][1]-bot2[1]
#           if (diff>0):
#               if (diff>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#           elif (diff<0):
#               if (abs(diff)>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")

#       # - - ERROR CHECK - -
#       r = requests.get(url = "http://"+urlarray[z]+"/Flip")

#       while (p2[0][0]-bot2[0]>10):
#           diff=p2[0][1]-bot2[1]
#           if (diff>0):
#               if (diff>20):
#                 #anti
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#           elif (diff<0):
#               if (abs(diff)>20):
#                 #clock
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")

#       turn()
#       while (origin2[1]-bot2[1]>20):
#           diff=origin2[0]-bot2[0]
#           if (diff>0):
#               if (diff>20):
#                 #anti
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")
#           elif (diff<0):
#               if (abs(diff)>20):
#                 #clock
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")

# #  ********************

#     i=i+1

#     if (bot3==[-1,-1]):
#         r=requests.get(url="http://" + urlarray[j]+"/Forward")

#     else:


#       while (p3[0][1]-bot3[1]>20):

#           diff=p3[0][0]-bot3[0]
#           if (diff>0):
#               if (diff>20):
#                 r = requests.get(url = "http://" + urlarray[z]+"/sleft")
#           elif (diff<0):
#               if (abs(diff)>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#       turn()
#       while (p3[1][0]-bot3[0]>10):
#           diff=p3[0][1]-bot3[1]
#           if (diff>0):
#               if (diff>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#           elif (diff<0):
#               if (abs(diff)>20):
#                 r = requests.get(url = "http://" + urlarray[z]+"/sleft")
#       r = requests.get(url = "http://"+urlarray[z]+"/Flip")


#       while (p3[0][0]-bot3[0]>10):
#           diff=p3[0][1]-bot3[1]
#           if (diff>0):
#               if (diff>20):
#                 #anti
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#           elif (diff<0):
#               if (abs(diff)>20):
#                 #clock
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")

#       turn()
#       while (origin3[1]-bot3[1]>20):

#           diff=origin3[0]-bot3[0]
#           if (diff>0):
#               if (diff>20):
#                 #anti
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")
#           elif (diff<0):
#               if (abs(diff)>20):
#                 #clock
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")

# #    ********************

#     i=i+1

#     if (bot4==[-1,-1]):
#         r=requests.get(url="http://" + urlarray[j]+"/Forward")

#     else:


#       while (p4[0][1]-bot4[1]>20):

#           diff=p4[0][0]-bot4[0]
#           if (diff>0):
#               if (diff>20):
#                 r = requests.get(url = "http://" + urlarray[z]+"/sleft")
#           elif (diff<0):
#               if (abs(diff)>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#       turn()
#       while (p4[1][0]-bot4[0]>10):
#           diff=p4[0][1]-bot4[1]
#           if (diff>0):
#               if (diff>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#           elif (diff<0):
#               if (abs(diff)>20):
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")
#       r = requests.get(url = "http://"+urlarray[z]+"/Flip")

#       while (p4[0][0]-bot4[0]>10):
#           diff=p4[0][1]-bot4[1]
#           if (diff>0):
#               if (diff>20):
#                 #anti
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")
#           elif (diff<0):
#               if (abs(diff)>20):
#                 #clock
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")

#       turn()
#       while (origin4[1]-bot4[1]>20):

#           diff=origin4[0]-bot4[0]
#           if (diff>0):
#               if (diff>20):
#                 #anti
#                   r = requests.get(url = "http://" + urlarray[z]+"/sleft")
#           elif (diff<0):
#               if (abs(diff)>20):
#                 #clock
#                   r = requests.get(url = "http://" + urlarray[z]+"/sright")

# *********************

    cv2.imshow("Video", new_img)
    cv2.imshow("Bots", green)
    # r = requests.get(url=URL)
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()