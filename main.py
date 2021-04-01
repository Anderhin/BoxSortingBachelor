#This program's intented use is for a bachelor's thesis for Currence Robotics
#It's used to identify different types of boxes or measure the gap between stacks of boxes.
#Code by Anders Indrelid
#
import cv2 #imports opencv module for python
import numpy as np #imports munpy module for python

#Set image path and read the image
imgPath = r'C:\Users\Ander\OneDrive\Dokumenter\Python\BoxDetection\BoxSortingBachelor\BoxSortingPictures\BoxesFront_Color.png'
image = cv2.imread(imgPath)

#Extract ROI for box
image = image[120:700, 350:900]

#Apply masks and filters for imageprocessing
imgGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),4)
imgEdge = cv2.Canny(imgBlur,70,70)

#Creates and shows image in a window
cv2.imshow("Original", image)
cv2.imshow("Grayscale",imgGray)
cv2.imshow("Blurred",imgBlur)
cv2.imshow("Edge",imgEdge)

#Keeps image open until program is closed or "q" is pressed
cv2.waitKey(0)
cv2.destroyAllWindows(q)