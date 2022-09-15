# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:46:18 2022

@author: Sandhya
"""
class Stiffness:
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