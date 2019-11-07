# -*- coding: utf-8 -*-
"""
Problem 1:Write a function to remove duplicates from Dictionary:student_data.
Created on Fri Feb 22 13:38:40 2019
@author: Jonathan Boryla
"""
#Initialize dictionary elements
student_data ={'id1':{
                    'name':['Sara'],
                    'class':['V'],
                    'subject_integration':['english, math, science']},
               'id2':{
                    'name':['David'],
                    'class':['V'],
                    'subject_integration':['english, math, science']},
                'id3':{
                    'name':['Sara'],
                    'class':['V'],
                    'subject_integration':['english, math, science']},
                'id4':{
                    'name':['Surya'],
                    'class':['V'],
                    'subject_integration':['english, math, science']},
                'id5':{
                    'name':['Sara'],
                    'class':['V'],
                    'subject_integration':['english, math, science']},
                'id6':{
                    'name':['David'],
                    'class':['V'],
                    'subject_integration':['english, math, science']},
                }
#Define function to remove duplicate elemnets
def remove_du(dictionary):
    #initialize variable to store duplicate entries before removing
    duplicate =''
    #While loop is active unitl first duplicate is found
    while duplicate == '':
        #For loops to compare all items in dictionary against each other
        for key1 in dictionary:
            for key2 in dictionary:
                #Check for all conditions to verify that entries match exactly
                if key1 != key2:
                    if dictionary[key1]['name'] == dictionary[key2]['name'] and\
                       dictionary[key1]['class'] == dictionary[key2]['class'] and\
                       dictionary[key1]['subject_integration'] == dictionary[key2]['subject_integration']:
                           #Once a duplicate is found it is stored to variable duplicate
                           duplicate = key1
        #Break from while loop if all dictionary items have been checked and no duplicates found
        break
    #Chcck if something is stored in variable duplcate
    if duplicate != '':
        #Delete dictionary item stored at the duplicate location
        del dictionary[duplicate]
        #Recursive function call
        remove_du(dictionary)
#Call function
remove_du(student_data)
#Print dictionary items
print(str(student_data)+'\n')