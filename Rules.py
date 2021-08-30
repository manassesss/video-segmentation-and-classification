import cv2
import numpy as np 


class Rules():
    
    CAM_POSITION = True #VERTICAL
    FLUXO_DUAL = True #DUAL
    PLACAS = []
    
    def __init__(self):
        pass
    
    def defineROI(self, frame, cam_position, fluxo_dual, traffic_signs):
        '''
        It is a method to define the area we should take in consideration to avaliate the situation in the traffic
        
        :param cam_position: a boolean value
        :param fluxo_dual: a boolean value
        :param traffic_signs: a list of traffic signs that it should take in count to define the area
        
        :return area: a set of countour to draw the area
        '''
        h, w = frame.shape[:2]
        a = (w/4),(5*(h/6))
        b = (w/4),(h/6) #aqui
        c = (3*(w/4)),(h/6)
        d = (3*(w/4)),(5*(h/6)) #aqui
        ROI= np.array([[(a),(b),(c),(d)]], dtype= np.int32)
        cv2.rectangle(gray, (int(b[0]), int(b[1])), (int(d[0]), int(d[1])), (0,0,255), 2)