#This program's intented use is for a bachelor's thesis for Currence Robotics
#It's used to identify different types of boxes or measure the gap between stacks of boxes.
#Code by Anders Indrelid
#
import cv2 #imports opencv module for python
import numpy as np #imports munpy module for python


imgPath = r'C:\Users\Ander\OneDrive\Dokumenter\Python\BoxDetection\BoxSortingBachelor\BoxSortingPictures\BlueBoxFront_Color.png'
image = cv2.imread(imgPath)

window_name = 'image'
image = image[200:650, 250:900]

cv2.imshow(window_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows(q)