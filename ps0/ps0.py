#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:12:13 2024

@author: ryanpham
1. Asks the user to enter a number “x” 
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”. 
4. Prints out the log (base 2) of “x”.
"""

import math

def userInput():
    x = int(input("X: enter a number: "))
    y = int(input ("Y: enter a number: "))
    q3 = int(math.pow(x, y))
    q4 = int(math.log(x,2))
    print(f"X**y = {q3}")
    print(f"log(x) = {q4}")
    

userInput()
#test: x = 2; y = 3; 
#expect: X**y = 8; log(x) = 1