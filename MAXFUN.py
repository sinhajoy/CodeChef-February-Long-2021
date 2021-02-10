# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:42:14 2021

@author: joysi
"""

a= int(input())

l=[]
for i in range(a):
    x=[]
    b=int(input())
    a=input().split()
    for i in a:
        x.append(int(i))
    x.sort()
    l.append(x)

print(l)       
        

for i in range(a):
    y=l[i]
    y.sort()

    print(y)

    final=[]
    final.append(y[0])
    final.append(y[1])
    final.append(y[-1])

    res = abs(final[0]-final[1])+abs(final[1]-final[2])+abs(final[2]-final[0])
    print(res)