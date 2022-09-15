# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:30:57 2022

@author: Sandhya
"""

import time
from Socket_receiver import SocketSend
from Socket_receiver import SocketReceivesSignal
from Master import master
from Slave import Slave
from Initialization import Initialise
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

def main():
    
    def StiffnessOff(proxy, chainName):
        #Turn off the stiffness of the Joints of a Chain
        pNames = chainName
        pStiffnessLists = 0.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)
            
    def StiffnessOn(proxy, chainName):
        #Turn on the stiffness of the Joints of a Chain.
        pNames = chainName
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

    #Initialize the IP of the robots
    MasterIP = "192.168.0.3"
    SlaveIP = "192.168.0.2"
    Port = "9559"
    
    #Initialise both robots and put them in stand position.
    s_m = Initialise(MasterIP, Port)
    s_s = Initialise(SlaveIP, Port)
    
    sm_motion = s_m.service("ALMotion")       
    sm_posture = s_m.service("ALRobotPosture")        
    sm_say = s_m.service("ALTextToSpeech")
    
    sm_motion.wakeUp()
    sm_posture.goToPosture("Stand",1)
    sm_say.say("I am the leader and I am ready")
    
    ss_motion = s_s.service("ALMotion")
    ss_posture = s_s.service("ALRobotPosture")
    ss_say = s_s.service("ALTextToSpeech")
    
    ss_motion.wakeUp()
    ss_posture.goToPosture("Stand",1)
    ss_say.say("I am the follower and I am ready")

    t_end = time.time() + 30
    
    effectorList = ["RArm","LArm" , "Head"]
    
    for i in range(len(effectorList)):
        StiffnessOff(sm_motion, effectorList[i])

    sm_say.say("Make Movement")
    
    #while time.time() < t_end:
    MPL, Master_pos = master(s_m, effectorList)
    
    for i in range(len(effectorList)):
            StiffnessOn(sm_motion, effectorList[i])

    sm_say.say("Stop Movement")
    
    Slave_pos = Slave(s_s, MPL, effectorList)

    print "Master pos list"
    print Master_pos

    print "Slave pos list"
    print Slave_pos

    Coords_m = np.array(0)
    Coords_s = np.array(0)
    
    for i in range(len(Master_pos)):
        xyz = Master_pos[0:3]
        Coords_m.append(xyz)

    for i in range(len(Slave_pos)):
        xyz = Slave_pos[0:3]
        Coords_s.append(xyz)
    #The coordinates of the master and slave are saved as a list.
    
    sm_posture.goToPosture("Stand",1)
    
    ss_posture.goToPosture("Stand",1)
    
    sm_motion.rest()

    ss_motion.rest()
    
if __name__ == "__main__":
    main()


    
    
