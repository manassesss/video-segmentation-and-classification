import cv2
import numpy as np 


class Rules():
    
    CAM_POSITION = True #VERTICAL
    FLUXO_DUAL = True #DUAL
    PLACAS = []
    
    def __init__(self):
        pass
    
        
    def defineArea(self, cam_position, fluxo_dual, traffic_signs):
        '''
        It is a method to define the area we should take in consideration to avaliate the situation in the traffic
        
        :param cam_position: a boolean value
        :param fluxo_dual: a boolean value
        :param traffic_signs: a list of traffic signs that it should take in count to define the area
        
        :return area: a set of countour to draw the area
        '''
        pass