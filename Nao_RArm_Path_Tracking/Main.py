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
    
    enableConnection = True
    MasterIP = "192.168.0.3"
    SlaveIP = "192.168.0.2"
    Port = "9559"
    
    s_m = Initialise(MasterIP, Port)
    s_s = Initialise(SlaveIP, Port)
    
#    if enableConnection:
#        sr = SocketReceivesSignal()
#        ss = SocketSend()
    MCP = master(s_m)
    print len(MCP)
    Slave(s_s, MCP)
#    for i in range (1,1000):
#        
#        MCurPos = master(s_m)
#        print MCurPos
#        time.sleep(1)
#        Slave(s_s, MCurPos)
#        time.sleep(5)
#        i = i+1
    
    motion1 = s_m.service("ALMotion")
    motion1.rest()
    
    motion2 = s_s.service("ALMotion")
    motion2.rest()
    
if __name__ == "__main__":
    main()


    
    