import cv2
import numpy as np
from numpy.core.numeric import count_nonzero
from numpy.lib.type_check import imag

class Filtering():
    
    KERNEL_1 = np.ones((2,2), np.uint8)
    KERNEL_2 = np.ones((3,3), np.uint8)
    KERNEL_3 = np.ones((4,4), np.uint8)
    KERNEL_4 = np.ones((5,5), np.uint8)
    
    
    def __init__(self):
        pass
    
    def opening(self, image, kernel, iterations):
        if kernel == 1:
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_1, iterations=iterations)
        elif kernel == 2:
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_2, iterations=iterations)
        elif kernel == 3:
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_3, iterations=iterations)
        elif kernel == 4:
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_4, iterations=iterations)
    
    def closing(self, image, kernel, iterations):
        if kernel == 1:
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_1, iterations=iterations)
        elif kernel == 2:
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_2, iterations=iterations)
        elif kernel == 3:
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_3, iterations=iterations)
        elif kernel == 4:
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_4, iterations=iterations)
    
    def dilating(self, image, kernel, iterations):
        if kernel == 1:
            return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_1, iterations=iterations)
        elif kernel == 2:
            return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_2, iterations=iterations)
        elif kernel == 3:
            return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_3, iterations=iterations)
        elif kernel == 4:
            return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_4, iterations=iterations)
    
    def eroding(self, image, kernel, iterations):
        if kernel == 1:
            return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_1, iterations=iterations)
        elif kernel == 2:
            return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_2, iterations=iterations)
        elif kernel == 3:
            return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_3, iterations=iterations)
        elif kernel == 4:
            return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_4, iterations=iterations)
    
    def fillCountours(self, image, contours, width, height):
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])
            areaImage = width*height
            if area > (areaImage*0.001):
                cv2.drawContours(image, contours, i, (255,255,255), cv2.FILLED)
    
    def fillConvexHull(self, image, hull, contours, width, height):
        for i in range(len(contours)):
            hull.append(cv2.convexHull(contours[i], False))
        for i in range(len(hull)):
            area = cv2.contourArea(contours[i])
            areaImage = width*height
            if area > (areaImage*0.001):
                cv2.drawContours(image, hull, i, (255,255,255), cv2.FILLED)
        