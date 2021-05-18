import cv2 #imports opencv module for python
import numpy as np #imports munpy module for python

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()

    #converts the image to hsv (hue saturation value)
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #Defines masks for colors, and ranges for colors
    red_lower = np.array([0,100,100], np.uint8)  #136,87,11
    red_upper = np.array([25,255,255],np.uint8) #180,255,255
    red_mask = cv2.inRange(hsvImage, red_lower, red_upper)

    green_lower = np.array([69,100,100], np.uint8)
    green_upper = np.array([89,255,255], np.uint8)
    green_mask = cv2.inRange(hsvImage, green_lower, green_upper)

    blue_lower = np.array([93,100,100], np.uint8)
    blue_upper = np.array([113,255,255], np.uint8)
    blue_mask = cv2.inRange(hsvImage, blue_lower, blue_upper)

    #kernel for morphological transformation, dilation
    kernel = np.ones((9, 9), "uint8")

    #Creating the different masks for colordetection
    red_mask = cv2.dilate(red_mask, kernel)
    red_pre_res = cv2.bitwise_and(image, image)
    red_res =  cv2.bitwise_and(image, image, mask = red_mask)

    green_mask = cv2.dilate(green_mask, kernel)
    green_res = cv2.bitwise_and(image, image, mask = green_mask)

    blue_mask = cv2.dilate(blue_mask, kernel)
    blue_res = cv2.bitwise_and(image, image, mask = blue_mask)

    #For keeping track of ammounts of pallets:
    redPallets = 0
    bluePallets = 0
    greenPallets = 0

    #Creating contours and tracking red
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 2500):
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(image, (x,y), (x + w, y + h), (0,0,255), 1)
            cv2.putText(image, "Red plasticpallet", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
            redPallets += 1

    #Creating contours and tracking blue
    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 2500):
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(image, (x,y), (x + w, y + h), (255,0,0), 1)
            cv2.putText(image, "Blue plasticpallet", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
            bluePallets += 1

    #Creating contours and tracking green
    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 2500):
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(image, (x,y), (x + w, y + h), (0,255,0), 1)
            cv2.putText(image, "Green plasticpallet", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))
            greenPallets  += 1


    #Shows the color detected image and the different masks
    cv2.imshow("Color Detection", image)
    cv2.imshow("Red mask", red_res)
    cv2.imshow("Blue Mask", blue_res)
    cv2.imshow("Green mask", green_res)


    #Printing out ammount of each pallet type
    #print('Ammounts of blue pallets in picture: ' + str(bluePallets))
    #print('Ammounts of green pallets in picture: ' + str(greenPallets))
    #print('Ammounts of red pallets in picture: ' + str(redPallets))
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()