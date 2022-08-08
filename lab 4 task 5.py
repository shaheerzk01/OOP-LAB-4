# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 16:07:56 2021

@author: 21A-003-SE
"""

a = eval(input("Enter any integer : "))
max = a
max_count = 0
while a != 0:
    if a>=max:
        if a == max:
            max_count = max_count + 1
        else:
            max = a
            max_count = 1        
    a = eval(input("Enter any integer : "))
print("max is",max)
print(max_count)

