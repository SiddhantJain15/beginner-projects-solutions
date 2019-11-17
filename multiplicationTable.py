# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:34:46 2019

@author: Admin
"""

def print_numwithspaces(num):
    length = len(str(num))
    print(num, end = "")
    for i in range(0, 5 - length):
        print(" ", end = "")
def mult_table(num):
    for i in range(0, num + 1):
        print_numwithspaces(i)
    print()
    for i in range(1, num + 1):
        print_numwithspaces(i)
        for j in range(1, num + 1):
            print_numwithspaces(i * j)
        print()
num = int(input("Enter the size of the table: "))
mult_table(num)