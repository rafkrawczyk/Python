#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:24:23 2026

@author: rafal
"""

def genPrimes():
    primes = []
    candidate = 2
    
    while True:
        # Check if candidate is prime by testing against all known primes
        is_prime = True
        for p in primes:
            if candidate % p == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(candidate)
            yield candidate
        
        candidate += 1