# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:51:30 2022

@author: Sandhya
"""
import qi

def Initialise(IP, Port):
     s = qi.Session()

     s.connect("tcp://" + IP + ":" +  Port)
     print( IP + "connected")
     return s