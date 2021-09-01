import cv2
import numpy as np 


class Rules():
    
    FLOW = True #DUAL
    PLACAS = []
    
    def __init__(self):
        pass
    
    
    def defineROI(self, frame):
        '''
        It is a method to define the area we should take in consideration to avaliate the situation in the traffic
        
        :param frame: a image
        
        :return area: a image with the ROI marked.
        '''
        h, w = frame.shape[:2]
        a = (w/4),(5*(h/6))
        b = (w/4),(h/6) #aqui
        c = (3*(w/4)),(h/6)
        d = (3*(w/4)),(5*(h/6)) #aqui
        ROI= np.array([[(a),(b),(c),(d)]], dtype= np.int32)
        cv2.rectangle(frame, (int(b[0]), int(b[1])), (int(d[0]), int(d[1])), (0,0,255), 2)
        
    
    def defineRules(self, flow, traffic_signs):
        '''
        It is a method to define the area we should take in consideration to avaliate the situation in the traffic
        
        :param flow: a boolean value
        :param traffic_signs: a list of traffic signs that it should take in count to define the area
        
        :return area: a set of countour to draw the area
        '''
        pass
    
    
        