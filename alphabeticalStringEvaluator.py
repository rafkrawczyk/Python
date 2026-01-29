#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:49:09 2026

@author: rafal
"""

s = input("Please enter a string: ")

if not s:
    print("String is empty")
else:
    longest_substring = s[0]
    current_substring = s[0]
    
    for i in range(1, len(s)):
        if s[i] >= s[i-1]:
            current_substring += s[i]
        else:
            current_substring = s[i]
            
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    print("Longest substring in alphabetical order is:", longest_substring)