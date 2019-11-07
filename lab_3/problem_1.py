# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:09:44 2019

@author: jmbor
"""

List_1 = [1, 2, [3, [4, 5], 6], 7, 8, ['hardware'], [['Software'], 'Inference']]
#Define a function to flatten a list
def flatten_list(lst):
    
    ''' The algorithm for this function is to convert a list to a string so
    that it can use the replace function to repalce the unneeded brackets and
    convert it back to a string by splitting at the comma delimiter'''
    
    lst=str(lst)
    lst=lst.replace("[","")
    lst=lst.replace("]","")
    lst=lst.replace('\'','')
    return list(lst.split(', '))  


def flatten_list_one_line(lst):
    
    '''The flatten list one line function is similar to the regular flatten function
    except it is all accomplished in one line'''
    
    return str(lst).replace('[','').replace(']','').replace('\'','').split(', ')

List_1=flatten_list(List_1)