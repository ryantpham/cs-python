#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:42:51 2024

@author: ryanpham
"""

def calculate_optimal_savings_rate():
    """
    a program to calculate the best savings rate, 
    as a function of your starting salary.
    """
    semi_annual_raise = 0.07
    annual_return = 0.04
    portion_down_payment = 0.25
    total_cost = 1000000
    
    annual_salary = float(input('Enter the starting salary:​ '))
    down_payment = total_cost * portion_down_payment
    
    
    
    

calculate_optimal_savings_rate()

"""
Test Case 1
>>>
Enter the starting salary:​ 150000 
Best savings rate:​ 0.4411
Steps in bisection search:​ 12 
>>>
Test Case 2
>>>
Enter the starting salary:​ 300000 
Best savings rate:​ 0.2206
Steps in bisection search:​ 9
>>>
Test Case 3
>>>
Enter the starting salary:​ 10000
It is not possible to pay the down payment in three years. >>>
"""
