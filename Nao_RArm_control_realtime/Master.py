# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 00:26:46 2022

@author: Sandhya
"""

import qi
import motion
import time
  
def master(s_m):
    sm_motion = s_m.service("ALMotion")  
    chainName = 'RArm'
    frame = motion.FRAME_ROBOT
    useSensorValues = True
    
    print "Make some movement"
    currentPos_m = sm_motion.getTransform(chainName, frame, useSensorValues)
    
    #print currentPos_m
    
    #ss.send(currentPos_m)
    return currentPos_m

    
    