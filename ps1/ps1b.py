#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:42:11 2024

@author: ryanpham
"""

def house_hunting():
    """
    program to calculate how many months it will take you
    to save up enough money for a down payment
    """
    #portion of the cost
    portion_down_payment = 0.25
    #investments earn a return of r = 0.04 (4%).
    r = 0.04
    current_savings = 0.0
    
    annual_salary = float(input('Enter your annual salary:​ '))
    portion_saved = float(input('Enter the percent of your salary to save, as a decimal:​ '))
    total_cost = float(input('Enter the cost of your dream home:​ '))
    semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))
    down_payment = total_cost * portion_down_payment
    
    month = 0 #Iterator
    salary_raise = 0
    while current_savings < down_payment:        
        if salary_raise == 6:
            salary_raise = 0
            annual_salary = (annual_salary * semi_annual_raise) + annual_salary
        
        monthly_investment = current_savings*r/12
        monthly_salary = annual_salary/12    
        monthly_portion = monthly_salary * portion_saved
        
        #return of investment
        current_savings += monthly_investment
        #percentage of ​monthly salary
        current_savings += monthly_portion
        
        month += 1
        salary_raise += 1
        
    print(f"Number of months:​ {month}")
    
house_hunting()

"""
Test Case 1
>>>
Enter your starting annual salary:​ 120000
Enter the percent of your salary to save, as a decimal:​ .05 
Enter the cost of your dream home: ​500000
Enter the semi­annual raise, as a decimal:​ .03
Number of months:​ 142
>>>
Test Case 2
>>>
Enter your starting annual salary:​ 80000
Enter the percent of your salary to save, as a decimal:​ .1 
Enter the cost of your dream home: ​800000
Enter the semi­annual raise, as a decimal:​ .03
Number of months:​ 159
>>>
Test Case 3
>>>
Enter your starting annual salary:​ 75000
Enter the percent of your salary to save, as a decimal:​ .05 
Enter the cost of your dream home:​ 1500000
Enter the semi­annual raise, as a decimal:​ .05
Number of months:​ 261
>>>
"""