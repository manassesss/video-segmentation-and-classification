import cv2
import numpy as np
import argparse
from Filtering import Filtering as f


def contours(frame):
    contour, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contour, _

# Receiving the arguments

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input',type=str, required=True, help='path to input video')
args = vars(ap.parse_args())
print('[INFO] input :', args['input'])


# Opening a video e checking if the video is valid
print('[INFO] Loading video...')
cap = cv2.VideoCapture(args['input'])
if (cap.isOpened() == False): 
    print("[INFO] Unable to read camera feed")

# Preparing the subtractors to identify the background
subtractor1 = cv2.createBackgroundSubtractorMOG2(800, 16, True) #it is not so good if compared with the o KNN method
subtractor2 = cv2.createBackgroundSubtractorKNN(dist2Threshold=1000, detectShadows=False)

frame_number = 0

filter = f()
print('[INFO] Video loaded. Showing it...')
while (True):
    ret, frame = cap.read()
    object_number = 0
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Applying the subtractor and separetin background and foreground
    mask = subtractor2.apply(frame2)
    
    #cv2.imshow("mask", mask)
    
    #mask11 = subtractor1.apply(frame2)   -- it is not being used because the other presented method the best result, if you compare with the other    
    
    rett, mask = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    #cv2.imshow("mask", mask)
    
    hei, wid = frame2.shape
    # Taking the countours of the objects and drawning them on the frame
    mask1 = mask.copy()
    mask1 = filter.opening(mask1, 1, 1)
    mask1 = filter.dilating(mask1, 2, 2)
    
    # Fill the contours and the convex hull | I did twice because it presents better results this way.
    c, hierarchy = contours(mask1)
    hull = []
    filter.fillCountours(mask1, c, wid, hei)
    filter.fillConvexHull(mask1, hull, c, wid, hei)
    c, hierarchy = contours(mask1)
    hull = []
    filter.fillCountours(mask1, c, wid, hei)
    filter.fillConvexHull(mask1, hull, c, wid, hei)
    cv2.imshow("filled convex hull", mask1)
    
    # Drawning a rectangule around the objects
    mask2 = mask1.copy()
    c, hierarchy = contours(mask2)
    for contour in c:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 700:
            continue
        crop = frame[y:y+h,x:x+w]
        #cv2.imwrite('CARS/'+'car'+str(frame_number)+str(object_number)+'.png', crop)
        object_number += 1
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.putText(frame,'object',(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),1)
    frame_number += 1
    
    # Display the resulting frame
    cv2.imshow("calssified", frame)  
    cv2.waitKey(50)
    
    # Press Q on keyboard to stop recording
print('[INFO] Done!')
cap.release()
cv2.destroyAllWindows()

