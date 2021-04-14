import cv2 #imports opencv module for python
import numpy as np #imports munpy module for python

#Set image path and reads the image
imgPath = r'C:\Users\Ander\OneDrive\Dokumenter\Python\BoxDetection\BoxSortingBachelor\BoxSortingPictures\BoxesFront_Color.png'
image = cv2.imread(imgPath)

#Set ROI of image
image = image[120:700, 350:900]

#converts the image to hsv (hue saturation value)
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Defines masks for colors, and ranges for colors
red_lower = np.array([160,20,70], np.uint8)  #136,87,11
red_upper = np.array([190,255,255],np.uint8) #180,255,255
red_mask = cv2.inRange(hsvImage, red_lower, red_upper)

green_lower = np.array([25,52,72], np.uint8)
green_upper = np.array([102,255,255], np.uint8)
green_mask = cv2.inRange(hsvImage, green_lower, green_upper)

blue_lower = np.array([94,80,2], np.uint8)
blue_upper = np.array([120,255,255], np.uint8)
blue_mask = cv2.inRange(hsvImage, blue_lower, blue_upper)

#kernel for morphological transformation, dilation
kernel = np.ones((5, 5), "uint8")

#Creating the different masks for colordetection
red_mask = cv2.dilate(red_mask, kernel)
red_res =  cv2.bitwise_and(image, image, mask = red_mask)

green_mask = cv2.dilate(green_mask, kernel)
green_res = cv2.bitwise_and(image, image, mask = green_mask)

blue_mask = cv2.dilate(blue_mask, kernel)
blue_res = cv2.bitwise_and(image, image, mask = blue_mask)

#Creating contours and tracking red
contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 500):
        x, y, w, h = cv2.boundingRect(contour)
        image = cv2.rectangle(image, (x,y), (x + w, y + h), (0,0,255), 2)
        cv2.putText(image, "Red plasticpallet", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))

#Creating contours and tracking blue
contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 500):
        x, y, w, h = cv2.boundingRect(contour)
        image = cv2.rectangle(image, (x,y), (x + w, y + h), (0,0,255), 2)
        cv2.putText(image, "Blue plasticpallet", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))

#Creating contours and tracking green
contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 500):
        x, y, w, h = cv2.boundingRect(contour)
        image = cv2.rectangle(image, (x,y), (x + w, y + h), (0,0,255), 2)
        cv2.putText(image, "Green plasticpallet", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))    




cv2.imshow("Color Detection", image)
cv2.imshow("Red mask", red_res)
cv2.imshow("Blue Mask", blue_res)
cv2.imshow("Green mask", green_res)

#Keeps image open until program is closed
cv2.waitKey(0)
cv2.destroyAllWindows()