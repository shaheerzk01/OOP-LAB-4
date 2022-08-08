# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:01:23 2021

@author: 21A-003-SE
"""

n = int(input("enter no of times : "))
for i in range(0,n):
    n = 1
    for j in range(0,i+1):
        print(n,end=" ")
        n = n+1
    print("\r")