# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 00:33:32 2022

@author: Sandhya
"""

import qi
#import motion
#import almath
import numpy as np
import time
from Socket_receiver import SocketReceivesSignal


def Slave(s_s, Pos_list, effectorList):
    
    ss_motion = s_s.service("ALMotion")
    
    frame = 2
    fractionMaxSpeed = 1
    axisMask = 63
    
    #sr = SocketReceivesSignal()
    
    print Pos_list
    
    t_rarm = Pos_list[0]
    t_larm = Pos_list[1]
    t_head = Pos_list[2]
    
    ss_motion.setTransforms(effectorList[0], frame, t_rarm, fractionMaxSpeed, axisMask)
    ss_motion.setTransforms(effectorList[1], frame, t_larm, fractionMaxSpeed, axisMask)
    ss_motion.setTransforms(effectorList[2], frame, t_head, fractionMaxSpeed, axisMask)

    time.sleep(0.25)

    Angle_list = []
    Pos_r = ss_motion.getPosition('RArm', 1, True)
    Pos_l = ss_motion.getPosition('LArm', 1, True)
    Angle_list.append(Pos_r)
    Angle_list.append(Pos_l)

    return Angle_list
    
