import cv2
import numpy as np
from Filtering import Filtering as f


def contours(frame):
    _,contour, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contour

# Opening a video e checking if the video is valid
cap = cv2.VideoCapture('STRANS/cam20.AVI')
if (cap.isOpened() == False): 
    print("Unable to read camera feed")

# Preparing the subtractors to identify the background
subtractor1 = cv2.createBackgroundSubtractorMOG2(800, 16, True)
subtractor2 = cv2.createBackgroundSubtractorKNN(dist2Threshold=1000, detectShadows=True)

filter = f()

while (True):
    ret, frame = cap.read()
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Applying the subtractor and separetin background and foreground
    mask = subtractor2.apply(frame2)
    mask11 = subtractor1.apply(frame2)
    rett, mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    cv2.imshow("mask", mask)
    
    hei, wid = frame2.shape
    # Taking the countours of the objects and drawning them on the frame
    mask1 = mask.copy()
    mask1 = filter.eroding(mask1)
    mask1 = filter.dilating(mask1)
    
    cv2.imshow("mask2", mask1)
    c = contours(mask1)
    for i in range(len(c)):
        area = cv2.contourArea(c[i])
        areaImage = wid*hei
        if area > (areaImage*0.001):
            cv2.drawContours(mask1, c, i, (255,255,255), cv2.FILLED)
    
    hull = []
    
    for i in range(len(c)):
        hull.append(cv2.convexHull(c[i]), False)
        
    # Drawning a rectangule around the object
    mask2 = mask1.copy()
    c = contours(mask2)
    for contour in c:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), 3)
        cv2.putText(frame,'object',(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2)

    # Display the resulting frame
    cv2.imshow("calssified", frame)  
    cv2.waitKey(20)
    # Press Q on keyboard to stop recording
    
cap.release()
cv2.destroyAllWindows()

