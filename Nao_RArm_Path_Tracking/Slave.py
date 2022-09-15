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
    
    ss_posture = s_s.service("ALRobotPosture")
    
    ss_say = s_s.service("ALTextToSpeech")
    
    ss_motion.wakeUp()
    ss_say.say("I am the slave and I am ready")
    
    ss_posture.goToPosture("Stand",1)
    
#    isEnabled = True
#    ss_motion.wbEnable(isEnabled)
#    ss_motion.wbFootState("Fixed", "Legs")
#    ss_motion.wbEnableBalanceConstraint(isEnabled, "Legs")
    
    chainName = "RArm"
    frame = motion.FRAME_ROBOT
    fractionMaxSpeed = 1
    axisMask = 63
    
    #sr = SocketReceivesSignal()
    print len(currentPos_m)
    #currentPos_m = sr.receive()
    for i in range(len(currentPos_m)):
        
        print currentPos_m[i]
        transform = currentPos_m[i]
        ss_motion.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    ss_posture.goToPosture("Stand",1)
    time.sleep(5)
    