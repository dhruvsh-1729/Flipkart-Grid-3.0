import cv2
import numpy as np
import requests

p1 = []  # the list which stores the clicked points
p2 = []
p3 = []
p4 = []
i = 0
for i in range(4):

    def click_event(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img, (x, y), 10, (0, 0, 0), -1)
            cv2.circle(img, (x, y), 5, (255, 255, 255), -1)
            if (i == 0):
                p1.append([x, y])
                arr = np.array(p1)
                # print(p1)
                cv2.polylines(img, [arr], False, (255, 0, 0), 4)
                cv2.imshow('image', img)
            elif (i == 1):
                p2.append([x, y])
                arr = np.array(p2)
                # print(p2)
                cv2.polylines(img, [arr], False, (255, 0, 0), 4)
                cv2.imshow('image', img)

            elif (i == 2):
                p3.append([x, y])
                arr = np.array(p3)
                # print(p3)
                cv2.polylines(img, [arr], False, (255, 0, 0), 4)
                cv2.imshow('image', img)
            elif (i == 3):
                p4.append([x, y])
                arr = np.array(p4)
                # print(p4)
                cv2.polylines(img, [arr], False, (255, 0, 0), 4)
                cv2.imshow('image', img)


    if __name__ == "__main__":
        img = cv2.imread("path.png")
        img = img[0:(int(img.shape[0])-300),0:int(img.shape[1])]
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow("image", img)
        cv2.setMouseCallback('image', click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
print(p1)
print(p2)
print(p3)
print(p4)