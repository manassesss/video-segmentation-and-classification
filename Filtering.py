import cv2
import numpy as np

class Filtering():
    
    KERNEL_OPENING = np.ones((3,3), np.uint8)
    KERNEL_CLOSING = np.ones((3,3), np.uint8)
    KERNEL_DILATING = np.ones((3,3), np.uint8)
    KERNEL_ERODING = np.ones((2,2), np.uint8)
    
    
    def __init__(self):
        pass
    
    def opening(self, image):
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel= self.KERNEL_OPENING, iterations=2)
    
    def closing(self, image):
        return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel= self.KERNEL_CLOSING, iterations=2)
    
    def dilating(self, image):
        return cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel= self.KERNEL_DILATING, iterations=2)
    
    def eroding(self, image):
        return cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel= self.KERNEL_ERODING, iterations=2)
  