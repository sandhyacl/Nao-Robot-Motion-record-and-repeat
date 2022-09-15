# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 00:26:46 2022

@author: Sandhya
"""

import qi
import motion
import time
from Socket_server import SocketSend
  
def master(s_m):
    def StiffnessOff(proxy, chainName):
            
            pNames = chainName
            pStiffnessLists = 0.0
            pTimeLists = 1.0
            proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
            
    def StiffnessOn(proxy, chainName):
        
        pNames = chainName
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
        
    sm_motion = s_m.service("ALMotion")       
    sm_posture = s_m.service("ALRobotPosture")        
    sm_say = s_m.service("ALTextToSpeech")
    
    sm_motion.wakeUp()
    sm_say.say("I am the master and I am ready")
    sm_posture.goToPosture("Stand",1)
    
    
    chainName = 'RArm'
    frame = motion.FRAME_ROBOT
    useSensorValues = True
    
    sm_say.say("Make some movement")
    
    initialPos = sm_motion.getTransform(chainName, frame, useSensorValues)
    currentPos_m = []
    
    t_end = time.time() + 20
    
    while time.time() < t_end:
        StiffnessOff(sm_motion, chainName)
        print "Make some movement"
        time.sleep(0.10)
        pos = sm_motion.getTransform(chainName, frame, useSensorValues)
        print pos
        if pos != initialPos:
            currentPos_m.append(pos)
            initialPos = pos
    sm_say.say("you can stop movement now")
    sm_posture.goToPosture("Stand",1)
    
    #print currentPos_m
    
    #ss.send(currentPos_m)
    return currentPos_m

    
    