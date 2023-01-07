# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:32:39 2023

@author: Tomek
"""

def kg_to_lbs():
    masa = float(input("Podaj mase w kg: \n"))
    print('%.*f kg to inaczej %.*f lbs' % (1, masa, 1, masa*2.205))
kg_to_lbs()     #wywołanie