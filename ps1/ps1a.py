#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:41:29 2024

@author: ryanpham
"""
#portion of the cost
portion_down_payment = 0.25
#investments earn a return of r = 0.04 (4%).
r = 0.04

def house_hunting():
    annual_salary = float(input('Enter your annual salary:​ '))
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal:​ '))
    total_cost = float(input('Enter the cost of your dream home:​ '))*portion_down_payment
    current_savings = 0
    monthly_investment = (current_savings*r)/12
    monthly_salary = annual_salary/12
    
    month = 0 #Iterator
    while current_savings < total_cost:
        #return of investment
        current_savings += monthly_investment
        #percentage of ​monthly salary
        current_savings += (monthly_salary)*portion_saved
        month += 1
        
    print(f"Number of months:​ {month}")
        

    
    
house_hunting()

"""
Test Case 1
>>>
Enter your annual salary:​ 120000
Enter the percent of your salary to save, as a decimal:​ .10 
Enter the cost of your dream home:​ 1000000
Number of months:​ 183
>>>

Test Case 2
>>>
Enter your annual salary:​ 80000
Enter the percent of your salary to save, as a decimal:​ .15 E
nter the cost of your dream home:​ 500000
Number of months:​ 105
>>>
"""