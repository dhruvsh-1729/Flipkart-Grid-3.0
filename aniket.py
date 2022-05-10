
import cv2 as cv
capture=cv.VideoCapture(1)

ret,img=capture.read()
# img=cv.resize(img,(img.shape[1]//3,img.shape[0]//3))
# imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# box=cv.selectROI("test",img,False)
# print(box)
# mat=imghsv[box[1]:box[1]+box[3],box[0]:box[0]+box[2]]
# print(imghsv[box[1]:box[1]+box[3],box[0]:box[0]+box[2]])
# hue_min=mat[mat[:,:,0].argmin()]
cv.imwrite('Amanop2.jpg',img)
cv.waitKey(0)
cv.destroyAllWindows()
