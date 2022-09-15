# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 22:33:19 2022

@author: Sandhya
"""

import zmq
import time
import json
import sys
import socket

class SocketSend:
    ctx = None
    sock = None
    
    def __init__(self):
        self.ctx = zmq.Context()
        self.sock = self.ctx.socket(zmq.PUB)
        
        try:
            self.sock.bind("tcp://*:9559")
        except zmq.error.ZMQError as e:
            print e
            sys.exit(-1)
    
    def __del__(self):
        self.sock.close()
        self.ctx.destroy()
    
    def receive_values(self):
        try:
            json_msg = self.sock.recv()
            wp_dict = json.loads(json_msg)
            return wp_dict
        except Expection as e:
            print e
            sys.exit(-1)
            
    def close(self):
        self.sock.close()
        self.ctx.term()

class SocketReceivesSignal:
    
    ctx = None
    sock = None
    
    def __init__(self):
        self.ctx = zmq.Context()
        self.sock = self.ctx.socket(zmq.REP)
        
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        try:
            self.sock.connect("tcp://%s:1235" % local_ip)
            self.sock.subscribe('')
        except Exception as e:
            print e
            sys.exit(-1)
        
    def __del__(self):
        self.sock.close()
        self.ctx.destroy()
    
    def receive(self):
        try:
            msg = self.sock.recv(flags = zmq.NOBLOCK)
            print(str(msg))
            
            self.sock.send_string('Received ' +str(msg))
            if msg:
                return msg
            else:
                return None
        except zmq.Again as e:
            return None
    
    def close(self):
        self.sock.close()
        self.ctx.term()
