# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:36:34 2021

@author: joysi
"""

try:
    import math
    for t in range(int(input())):
        n=int(input())
        w=list(map(int,input().split()))
        l=list(map(int,input().split()))
        ind={}
        x=0
        for i in range(1,n+1):
            ind[i]=w.index(i)
        for i in range(2,n+1):
            t1=ind[i]
            t2=ind[i-1]
            t=0
            if t1<=t2:
                t=(math.ceil((t2+1-t1)/l[t1]))
            x+=t
            ind[i]+=t*(l[t1])
                
        print(x)
    
except:
    pass