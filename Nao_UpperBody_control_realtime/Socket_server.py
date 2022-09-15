# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 22:24:51 2022

@author: Sandhya
"""

import zmq
import time
import json
import sys

class SocketSend:
    ctx = None
    sock = None
    
    def __init__(self):
        
        self.ctx = zmq.Context()
        print(self.ctx)
        self.sock = self.ctx.socket(zmq.PUB)
        print(self.sock)
        
        try:
            self.sock.bind("tcp://168.192.0.2:9559")
        except zmq.error.ZMQError as e:
            print(e)
            sys.exit(-1)
        
    def send(self, msg_dict):
        msg_json = json.dumps(msg_dict)
        print msg_json
        self.sock.send_string(msg_json)
        
    def close(self):
        self.sock.close()
        self.ctx.term()
        