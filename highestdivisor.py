#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:32:27 2021

@author: user
"""
a=int(input())

div=[]

for i in range(1,a+1):
    if a%i==0:
        div.append(i)
        
ran=[]
for i in div:
    if (1<=i and 10>=i):
        ran.append(i)
print(max(ran))