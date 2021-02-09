#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:23:07 2021

@author: user
"""
# cook your dish here

try:
    a=int(input())
    if (1<=a and 50>=a):
        print(100)
        
    elif(51<=a and 100>=a):
        print(50)
    
    else:
        print(0)
        
except:
    pass