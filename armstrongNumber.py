"""
Created on Sat Nov  9 12:22:55 2019

@author: SiddhantJain15
"""

def checkArmstrong(num):
    n = len(num)
    if n == 1:
        return 1 #all one digit numbers are Armstrong numbers
    sum = 0
    num = int(num)
    newnum = num
    while newnum != 0:
        digit = newnum % 10
        sum += digit ** n
        newnum = newnum // 10 #// is used for integer division
    if(sum == num):
        return 1
    else:
        return 0
if(checkArmstrong(input("Enter the number to check Armstrong: "))):
    print("It is an Armstrong number")
else:
    print("Not an Armstrong number")
