# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:43:31 2021

@author: joysi
"""
a=input()
lis=[]
lis1=[]
for i in range(len(a)):
    if(a[i]=='('):
        lis.append(a[i])
    if(a[i]==')'):
        lis1.append(a[i])

if (len(lis1)==len(lis)):
    print(len(lis1))
else:
    print(abs(len(l)))
      
print(lis1)
print(lis)