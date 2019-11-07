# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 12:08:21 2019
Problem 1: Fibonacci Number
@author: borylaj
"""
#Define function to generate Fibonacci numbers
def gen_fib():
    #Initialize variables for the function    
    F0 = 1    
    F1 = 1
    Fn = 0
    #Initaialze list to return from the function
    F = []
    #Get user input and store in count
    count= input("How many Fibonacci numbers would you like to generate?: ")
    #Check that user input a number and enter loop if no number is input
    while count == '':
        #Get user input and store in count
        count= input("Please input an integer: ")
    #Convert input and round
    count = round(float(count))
    #Enter loop if user input a negative number
    while count == '' or float(count) <=0:
        #Get user input and store to count
        count = input("Please input a POSITIVE INTEGER: ")
    #Convert input to float and round
    count = round(float(count))
    #Loop for the amount specified by user
    for i in range(count):
        #Append F0 to F
        F.append(F0)  
        #Add two current numbers and shift by one
        Fn = F1 + F0
        F0 = F1
        F1 = Fn
    #Return F from function
    return F  
#Print the list returned from the function and convert to a string
print (str(gen_fib()))