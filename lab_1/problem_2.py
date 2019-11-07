# -*- coding: utf-8 -*-
"""
Problem 2: List Overlap
@author: Jonathan Boryla
"""
#Declare lists to sent to function
a = [1,1,2,3,5,8,13,21,34,55,89,]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#List store return list from function
c = []
#Define function to take two lists and return the common elements
def common_element(x,y):
    #List for return from function
    z = []
    #Check length of two lists and run loop on smaller list
    if len(x) <= len(y):
        #loop through the length of the list
        for i in range (len(x)):
            #chech if x[i] is in list y and not in the output list already
            if x[i] in y and x[i] not in z:
                #Append new element to the list
                z.append(x[i])
    #Else
    else:
        #For loop checks all elements in y
        for i in range (len(y)):
            #If y[i] is in x and not in z then its added to the list
            if y[i] in x and y[i] not in z:
                z.append(y[i])
    #Return z containing list of common elements                            
    return z
#call common_element function and save result to c
c = common_element(a,b)
#Print result of common elements
print ('Overlap: ' + str(c))