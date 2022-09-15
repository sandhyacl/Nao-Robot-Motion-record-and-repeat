# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 00:26:46 2022

@author: Sandhya
"""

import qi
#import motion
import time
from Socket_server import SocketSend
#import almath

  
def master(s_m, effectorList):
    sm_motion = s_m.service("ALMotion")  
    
    frame = 2
    
    useSensorValues = True
    Pos_list= []
    Angle_list = []
    
    print "Make some movement"
    time.sleep(5)
    pos_rarm = sm_motion.getTransform(effectorList[0], frame, useSensorValues)
    
    Pos_list.append(pos_rarm)
    
    pos_larm = sm_motion.getTransform(effectorList[1], frame, useSensorValues)
    Pos_list.append(pos_larm)
    
    pos_head = sm_motion.getTransform(effectorList[2], frame, useSensorValues)
    Pos_list.append(pos_head)
    
    Pos_r = sm_motion.getPosition('RArm', 1, useSensorValues)
    Pos_l = sm_motion.getPosition('LArm', 1, useSensorValues)
    Angle_list.append(Pos_r)
    Angle_list.append(Pos_l)
    #print currentPos_m
    
    #ss.send(currentPos_m)
    return Pos_list, Angle_list

    
    
