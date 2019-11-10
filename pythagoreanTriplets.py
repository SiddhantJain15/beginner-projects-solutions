# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:56:55 2019

@author: SiddhantJain15
"""

def isPythagorean(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    if((a * a + b * b == c * c) | (b * b + c * c == a * a) | (c * c + a * a == b * b)):
        return 1
    else:
        return 0
def func():
    a, b, c = input("Enter three sides of the triangle separated by space\n").split()
    if(isPythagorean(a, b, c)):
        print("The triangle is a Pythogorean Triple")
    else:
        print("The triangle is not a Pythagorean Triple")
    if(input("Do you to continue? Enter Y/N\n").upper() == 'Y'):
        func()
    else:
        print("Ending the program")
func()