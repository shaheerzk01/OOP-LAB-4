# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = eval(input("enter any integer : "))
b = eval(input("enter any integer : "))
c = eval(input("enter any integer : "))
if a<b<c:
    print(a,b,c)
elif a>b>c:
    print(c,b,a)
elif b>c>a:
    print(a,c,b)
elif b>a>c:
    print(c,a,b)
elif c>a>b:
    print(b,a,c)
    
