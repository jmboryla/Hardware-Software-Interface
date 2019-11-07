# -*- coding: utf-8 -*-
"""
Problem 2:Write a Python function to check whether a number is perfect or not. 
Created on Fri Feb 22 15:18:41 2019
@author: Jonathan Boryla
"""
#Define function to check if number 'x' is a perfect number
def perfect_number(x):
    #Print the purpose of the function
    print('Is the number ' +str(x)+ ' a perfect number?')
    #initialize sum variable to 0
    sum = 0;
    #in the range of one less than number input
    for i in range(x-1,0,-1):
        #if x is evenly divisible by i then add i to the sum
        if x%i == 0:
            sum = sum + i
    #if the number 'x' is equal to the sum of its divisors
    if sum == x:
        #Then 'x' is a perfect number
        print('True')
        #else if x does not equal to the sum of its divisors
    else:
        #'x' is not a perfect number
        print('False')
#Ask user for number and check it in the perfect number function
perfect_number(int(input('Please input a random number:')))