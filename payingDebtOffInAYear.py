#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 13:46:08 2026

@author: rafal
"""

#Example variables
#balance = 484
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

# Calculate monthly interest rate (annual / 12)
monthlyInterestRate = annualInterestRate / 12.0

# Loop for 12 months
for month in range(12):
    # Calculate the minimum payment
    minPayment = balance * monthlyPaymentRate
    
    # Calculate the unpaid balance after payment
    unpaidBalance = balance - minPayment
    
    # Calculate the new balance by adding interest
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)

# Print the result rounded to 2 decimal places
print("Remaining balance: " + str(round(balance, 2)))