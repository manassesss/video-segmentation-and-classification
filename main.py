import cv2
import numpy as np
import Filtering as f


def contours(frame):
    _, contour, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contour

# Opening a video e checking if the video is valid
cap = cv2.VideoCapture('strans/cam20.AVI')
if (cap.isOpened() == False): 
    print("Unable to read camera feed")

# Preparing the subtractors to identify the background
subtractor1 = cv2.createBackgroundSubtractorMOG2(800, 16, True)
subtractor2 = cv2.createBackgroundSubtractorKNN(dist2Threshold=1000, detectShadows=True)

filter = f()

while (True):
    ret, frame = cap.read()
    
    # Applying the subtractor and separetin background and foreground
    mask = subtractor2.apply(frame)
    
    # Taking the countours of the objects and drawning them on the frame
    c = contours(frame)
    for i in range(len(c)):
        area = cv2.contourArea(c[i])
        areaImage = wid*hei
        if area > (areaImage*0.001):
            cv2.drawContours(mask, c, i, (255,255,255), cv2.FILLED)
    
    # Drawning a rectangule around the object
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), 3)
    
    # Display the resulting frame    
    cv2.imshow('frame', frame)
 
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    
    break
