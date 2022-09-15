# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:30:57 2022

@author: Sandhya
"""
import qi
import time
from Socket_receiver import SocketSend
from Socket_receiver import SocketReceivesSignal
from Master import master
from Slave import Slave
from Initialization import Initialise

def main():
    
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

    enableConnection = True
    MasterIP = "192.168.0.2"
    SlaveIP = "192.168.0.3"
    Port = "9559"
    
    s_m = Initialise(MasterIP, Port)
    s_s = Initialise(SlaveIP, Port)
    
    sm_motion = s_m.service("ALMotion")       
    sm_posture = s_m.service("ALRobotPosture")        
    sm_say = s_m.service("ALTextToSpeech")
    
    sm_motion.wakeUp()
    sm_say.say("I am the master and I am ready")
    
    ss_motion = s_s.service("ALMotion")
    ss_posture = s_s.service("ALRobotPosture")
    ss_say = s_s.service("ALTextToSpeech")
    
    ss_motion.wakeUp()
    ss_say.say("I am the slave and I am ready")
    
    t_end = time.time() + 30
    
    StiffnessOff(sm_motion, "RArm")
    sm_say.say("Make Movement")
    
    while time.time() < t_end:
        MCP = master(s_m)
        
        Slave(s_s, MCP)
        
        time.sleep(0.25)
    
    sm_say.say("Stop Movement")
    sm_posture.goToPosture("Stand",1)
    
    ss_posture.goToPosture("Stand",1)
    
#    sm_motion.rest()
#
#    ss_motion.rest()
    
if __name__ == "__main__":
    main()


    
    