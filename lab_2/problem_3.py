# -*- coding: utf-8 -*-
"""
Problem 3: Write a Python function that accepts a string and calculate the number ofupper case letters and lower case letters.
Created on Fri Feb 22 17:48:22 2019
@author: Jonathan Boryla
"""

#Define a dictionary to store the amount of upper and lower case characters 
d={"UPPER_CASE":0,"LOWER_CASE":0}
#Defining function to test string for upper and lower case characters
def string_test(s):
    #Break down string into a list for processing
    s_list=list(s)
    #Iterate through every item in the string list
    for item in s_list:
        #Check to make sure the item is an alphabet character
        if item == ' ' or item.isalpha():
            #use isupper function to check if item in the list is an uppercase character
            if item.isupper():
                #increment uppercase character variable
                d['UPPER_CASE']+=1
            #If the item in the list is a lowercase character
            elif item.islower():
                #increment the lowercase variable
                d['LOWER_CASE']+=1
            elif item == ' ':
                pass
        #If the item is not an alphabet character then display error message
        else:
            print('You have entered numbers where number not expected.\nPlease enter only alphabet characters.')
            return
    #Output the original string, and the count of upper and lowercase characters
    print('Orignial String: ' + s +'\n'+ 'No. of Upper case chars: '+str(d['UPPER_CASE'])+\
          '\n'+'No. of Lower case chars: '+str(d['LOWER_CASE']))
#input string to string test
string_test('Hardware Software Interface Lab')