# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:56:32 2021

@author: USER
"""

s=[]
x = int(input("學生數量?"))
g = 0
for i in range(x):
    y = int(input("學生成績?"))
    s.append(y)
    g = g+y
    
print(s)
print(g/x)  
   