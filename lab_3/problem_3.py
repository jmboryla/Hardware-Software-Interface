# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:59:49 2019

@author: jmbor
"""

#Import numpy library for matrix manipulation
import numpy as np
return_array=np.array([])
array_1 = np.array([1,2,2,1,1,2,1])

#Function to check the monotonic changes of an array of numbers
def monotonic_check(ori_array):
    indices_array=[]
    if len(ori_array) < 3:
        return np.array(indices_array)
    
    for i in range(2,len(ori_array)):
        
        if ori_array[i-2] >= ori_array[i-1] and ori_array[i-1] < ori_array[i]:
            indices_array.append(i-1)
            
        elif ori_array[i-2] <= ori_array[i-1] and ori_array[i-1] > ori_array[i]:
            indices_array.append(i-1)
            
    return np.array(indices_array)

return_array=monotonic_check(array_1)