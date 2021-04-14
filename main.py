#This program's intented use is for a bachelor's thesis for Currence Robotics
#It's used to identify different types of boxes or measure the gap between stacks of boxes.
#Code by Anders Indrelid
#
import cv2 #imports opencv module for python
import numpy as np #imports munpy module for python

#Set image path and reads the image
imgPath = r'C:\Users\Ander\OneDrive\Dokumenter\Python\BoxDetection\BoxSortingBachelor\BoxSortingPictures\BoxesFront_Color.png'
image = cv2.imread(imgPath)

#Extract ROI for box
image = image[120:700, 350:900]

#
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area<20:
            cv2.drawContours(imgContours,cnt,-1,(0,0,255),2)
        

#Apply masks and filters for image processing
imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),4)
imgEdge = cv2.Canny(imgBlur,45,45)
imgContours = image.copy()
getContours(imgEdge)

#Creates a window and shows image
cv2.imshow("Original", image)
cv2.imshow("Grayscale",imgGray)
cv2.imshow("Blurred",imgBlur)
cv2.imshow("Edge",imgEdge)
cv2.imshow("Contours",imgContours)

#Keeps image open until program is closed
cv2.waitKey(0)
cv2.destroyAllWindows()