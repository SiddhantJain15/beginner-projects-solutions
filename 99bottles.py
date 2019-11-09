"""
Created on Sat Nov  9 12:06:46 2019

@author: SiddhantJain15
"""

for i in range(99, -1, -1):
    if(i == 0):
        print("No more bottles of beer on the wall, No more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
    elif(i == 1):
        print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, No more bottles of beer on the wall.\n")
    elif(i == 2):
        print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n")
    else:
        print(i," bottles of beer on the wall, ",i," bottles of beer.\nTake one down and pass it around, ",i-1," bottles of beer on the wall.\n")
