#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:59:45 2021

@author: user
"""

s=int(input())
for i in range(s):
    a=input().split()
    li=[]
    while (int(a[0])!=int(a[-1])):
        a[0]=a[0]+1
        li.append(a[0])
        
        print(li)
                