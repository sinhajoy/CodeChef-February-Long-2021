# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:42:14 2021

@author: joysi
"""
try:
    c= int(input())
    a=c
    l=[]
    for i in range(a):
        x=[]
        b=int(input())
        a=input().split()
        for i in a:
            x.append(int(i))
        x.sort()
        l.append(x)   

    for j in range(c):
        y=l[j]
        y.sort()
        final=[]
        final.append(y[0])
        final.append(y[1])
        final.append(y[-1])

        res = abs(final[0]-final[1])+abs(final[1]-final[2])+abs(final[2]-final[0])
        print(res)
        
except:
    pass
