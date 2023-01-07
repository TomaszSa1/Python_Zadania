# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:33:37 2023

@author: Tomek
"""

def czyIntPlus(s):
    return (s.isdigit() and int(s) > 0) or ((float(s) == int(s) and int(s) > 0))

print(czyIntPlus('1'))     
print(czyIntPlus('0'))
print(czyIntPlus('-1'),'\n')

def czyLiczba(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(czyLiczba('50'))
print(czyLiczba('1.'))
print(czyLiczba('abc'))
print(czyLiczba('a1.2b0'))