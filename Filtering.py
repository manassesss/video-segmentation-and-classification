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
        """
        It do an opening morphological operation in an image/frame
        
        :param image: an image array
        :param kernel: an interger value from 1 to 4 corresponding to one of the constant kernels will apply on the image/frame
        :param iterations: an interger value to determine how many iterations will apply on the image/frame
        
        :return: an image/frame with the opening morphological operation applied
        """
        if kernel == 1:
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_1, iterations=iterations)
        elif kernel == 2:
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_2, iterations=iterations)
        elif kernel == 3:
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_3, iterations=iterations)
        elif kernel == 4:
            return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_4, iterations=iterations)
    
    def closing(self, image, kernel, iterations):
        """
        It do an closing morphological operation in an image/frame
        
        :param image: an image array
        :param kernel: an interger value from 1 to 4 corresponding to one of the constant kernels will apply on the image/frame
        :param iterations: an interger value to determine how many iterations will apply on the image/frame
        
        :return: an image/frame with the closing morphological operation applied
        """
        if kernel == 1:
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_1, iterations=iterations)
        elif kernel == 2:
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_2, iterations=iterations)
        elif kernel == 3:
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_3, iterations=iterations)
        elif kernel == 4:
            return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_4, iterations=iterations)
    
    def dilating(self, image, kernel, iterations):
        """
        It do an dilating morphological operation in an image/frame
        
        :param image: an image array
        :param kernel: an interger value from 1 to 4 corresponding to one of the constant kernels will apply on the image/frame
        :param iterations: an interger value to determine how many iterations will apply on the image/frame
        
        :return: an image/frame with the dilating morphological operation applied
        """
        if kernel == 1:
            return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_1, iterations=iterations)
        elif kernel == 2:
            return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_2, iterations=iterations)
        elif kernel == 3:
            return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_3, iterations=iterations)
        elif kernel == 4:
            return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_4, iterations=iterations)
    
    def eroding(self, image, kernel, iterations):
        """
        It do an eroding morphological operation in an image/frame
        
        :param image: an image array
        :param kernel: an interger value from 1 to 4 corresponding to one of the constant kernels will apply on the image/frame
        :param iterations: an interger value to determine how many iterations will apply on the image/frame
        
        :return: an image/frame with the eroding morphological operation applied
        """
        if kernel == 1:
            return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_1, iterations=iterations)
        elif kernel == 2:
            return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_2, iterations=iterations)
        elif kernel == 3:
            return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_3, iterations=iterations)
        elif kernel == 4:
            return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_4, iterations=iterations)
    
    def fillCountours(self, image, contours, width, height):
        """
        It will fill the contours of the identified objects in the image/frame
        
        :param image: an image array
        :param contours: a list of contours of each object in the image/frame
        :param width: the width of the image/frame
        :param height: the height of the image/frame
        
        :return: an image/frame with the filled contours of objects
        """
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])
            areaImage = width*height
            if area > (areaImage*0.001):
                cv2.drawContours(image, contours, i, (255,255,255), cv2.FILLED)
    
    def fillConvexHull(self, image, hull, contours, width, height):
        """
        It do an opening morphological operation in an image/frame
        
        :param image: an image array
        :param hull: a list where identified hulls will be saved 
        :param contours: a list of contours of each object in the image/frame
        :param width: the width of the image/frame
        :param height: the height of the image/frame
        
        :return: an image/frame with the filled hulls of objects
        """
        for i in range(len(contours)):
            hull.append(cv2.convexHull(contours[i], False))
        for i in range(len(hull)):
            area = cv2.contourArea(contours[i])
            areaImage = width*height
            if area > (areaImage*0.001):
                cv2.drawContours(image, hull, i, (255,255,255), cv2.FILLED)
        