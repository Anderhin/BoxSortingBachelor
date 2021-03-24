#This program's intented use is for a bachelor's thesis for Currence Robotics
#It's used to identify different types of boxes or measure the gap between stacks of boxes.
#Code by Anders Indrelid
#
import cv2 #imports opencv module for python
import numpy #imports munpy module for python


imgPath = r'C:\Users\Ander\OneDrive\Dokumenter\BoxSortingPictures\BadExample.jpg'
boxesExample = cv2.imread(imgPath,1)
#boxesExampleResize = cv2.resize(boxesExample, (1280,720))
cv2.imshow('image',boxesExample)
cv2.waitKey(0)
cv2.destroyAllWindows()