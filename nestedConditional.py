#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 22:46:05 2026

@author: rafal
"""

x = int(input('Enter an integer: '))
if x % 2 == 0:
    if x % 3 == 0:
        print('')
        print('Divisible by 2 and 3')
    else:
        print('')
        print('Divisible by 2 but not 3')
elif x % 3 == 0:
    print('Divisible by 3 but not 2')
else:
    print('Not divisible by either 2 or 3')
print('Done with conditional')