# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:15:42 2021

@author: 21A-003-SE
"""

i=0
positive_count = 0
negative_count = 0
zero_count = 0
summ = 0
while True:
    a = eval(input("enter any number : "))
    summ = summ + a
    if a > 0:
        positive_count = positive_count + 1
    elif a < 0:
        negative_count = negative_count + 1
    if a==0:
        break
average = summ/positive_count + negative_count
print("positive number were",positive_count)
print("negative number were",negative_count)
print("total sum is",summ)
print("average is",average)