import numpy as np
import cv2 as cv

img=cv.imread(r"C:\Users\Hp\OneDrive\Desktop\OPENCV\OPENCV PROJECTS\PROJECT_FILES\fruits2.jpg")
# resize=cv.resize(img,[img.shape[1]//4,img.shape[0]//4])
cv.imshow("fruits",img)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
bgr_green=np.uint8([[[0,255,0]]]) #create green color in bgr (np array)
hue_green=cv.cvtColor(bgr_green,cv.COLOR_BGR2HSV)[0][0][0] #extract that green color in hsv (row,column,hsv color space) 
lowerlimit = np.array([max(hue_green - 20, 0), 100, 100], dtype=np.uint8)
upperlimit = np.array([min(hue_green + 20, 179), 255, 255], dtype=np.uint8)
lower_limit=np.array(lowerlimit,dtype=np.uint8)
upper_limit=np.array(upperlimit,dtype=np.uint8)
mask=cv.inRange(hsv,lower_limit,upper_limit)
cv.imshow("white Mask",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("results",masked)

cv.waitKey(0)

#if you want to get color without clicking any button
#you simply replace event_lbutton to mousemove
# def show_color(event, x, y, flags, param):
#     if event == cv.EVENT_MOUSEMOVE:        # ← changed line
#         hue = hsv_img[y, x, 0]
#         lower = np.array([max(hue-20, 0), 50, 50], np.uint8)
#         upper = np.array([min(hue+20, 179), 255, 255], np.uint8)

#         mask   = cv.inRange(hsv_img, lower, upper)
#         result = cv.bitwise_and(img, img, mask=mask)

#         cv.imshow("Mask",   mask)
#         cv.imshow("Result", result)
#         print("Hue:", hue, end="\r")       # overwrite the line, avoids flooding





#webcam
# def get_limits(color):
#     c=np.uint8([[color]])
#     hsvC=cv.cvtColor(c,cv.COLOR_BGR2HSV)
#     lower_limit=hsvC[0][0][0]-10,100,100
#     upper_limit=hsvC[0][0][0]+10,255,255
#     lower_limit=np.array(lower_limit,dtype=np.uint8)
#     upper_limit=np.array(upper_limit,dtype=np.uint8)

#     return lower_limit,upper_limit