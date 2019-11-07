# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:54:50 2019

@author: borylaj
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(key):
    if key in d:
        print(str(key)+' is present in the dictionary')
    else:
        print(str(key)+' is not present in the dictionary')
is_key_present()