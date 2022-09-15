# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 19:39:42 2022

@author: Sandhya
"""

import qi
import motion
#import almath
import time
from Socket_receiver import SocketSend
from Socket_receiver import SocketReceivesSignal

def StiffnessOff(proxy):
    
    pNames = 'RArm'
    pStiffnessLists = 0.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
    
def StiffnessOn(proxy):
    
    pNames = 'RArm'
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
    
def SendVals(currentPos, ss):
    ss.send(currentPos)

def ReceiveVals(currentPos, sr):
    currentPos = ss.receive()
    return currentPos
    
def Master(s_m):
    
    sm_motion = s_m.service("ALMotion")
    
    sm_posture = s_m.service("ALRobotPosture")
    
    sm_say = s_m.service("ALTextToSpeech")
    
    sm_motion.wakeUp()
    sm_say.say("I am the master and I am ready")
    sm_posture.goToPosture("Stand",1)
    
    #sm_memory = s_m.service("ALMemory")
    name = 'RHand'
    frame = motion.FRAME_TORSO
    useSensorValues = True
    
#    initialPos_m = sm_motion.getTransform(name, frame, useSensorValues)
#    print initialPos_m
    sm_say.say("Move my right arm")
    
    
    StiffnessOff(sm_motion)
    print "Mave some movement in the right arm"
    
    time.sleep(10) #time delay of 10 seconds
    
    StiffnessOn(sm_motion)
    
    
    currentPos_m = sm_motion.getTransform(name, frame, useSensorValues)
    
    #SendVals(currentPos_m, ss)
    
    print currentPos_m
    return currentPos_m
    
    
def Slave(s_s, currentPos_m):
    
    ss_motion = s_s.service("ALMotion")
    
    ss_posture = s_s.service("ALRobotPosture")
    
    ss_say = s_s.service("ALTextToSpeech")
    
    ss_motion.wakeUp()
    ss_say.say("I am the slave and I am ready")
    
    ss_posture.goToPosture("Stand",1)
    
    chainName = "RArm"
    frame = motion.FRAME_TORSO
    fractionMaxSpeed = 0.7
    axisMask = 63

    isEnabled = True
    ss_motion.wbEnable(isEnabled)

    #currentPos_m = ReceiveVals(currentPos_m, sr)
    transform = currentPos_m
    print transform
    
    time.sleep(5)
    
    ss_motion.setTransforms(chainName, frame, transform, fractionMaxSpeed, axisMask)
    
    time.sleep(5)
    
    ss_motion.rest()
    
def main():
    
    enableConnection = True
    
    Master_IP = "192.168.0.3"
    Slave_IP = "192.168.0.2"
    
    s_m = qi.Session()
    
    s_m.connect("tcp://192.168.0.2:9559")
    
    s_s = qi.Session()
    
    s_s.connect("tcp://192.168.0.3:9559")
    
#    if enableConnection:
#        sr = SocketReceivesSignal()
#        ss = SocketSend()
    
    CP = Master(s_m)
    
    Slave(s_s, CP)
    
    
if __name__ == "__main__":
    main()


    
    
    
    
    
    
    
    
    
    
    
