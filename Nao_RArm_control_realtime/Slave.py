# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 00:33:32 2022

@author: Sandhya
"""

import qi
import motion
#import almath
import numpy as np
import time
from Socket_receiver import SocketReceivesSignal


def Slave(s_s, currentPos_m):
    
    ss_motion = s_s.service("ALMotion")
#    isEnabled = True
#    ss_motion.wbEnable(isEnabled)
#    ss_motion.wbFootState("Fixed", "Legs")
#    ss_motion.wbEnableBalanceConstraint(isEnabled, "Legs")
    
    chainName = "RArm"
    frame = motion.FRAME_ROBOT
    fractionMaxSpeed = 0.7
    axisMask = 63
    
    #sr = SocketReceivesSignal()
    
        
    print currentPos_m
    transform = currentPos_m
    ss_motion.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    

    
    