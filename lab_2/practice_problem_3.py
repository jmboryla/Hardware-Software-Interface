# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:49:29 2019

@author: jmbor
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
        try:
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
        except TypeError:
            print('You have entered numbers where number not expected.\nPlease enter only alphabet characters.')
    #Output the original string, and the count of upper and lowercase characters
    print('Orignial String: ' + s +'\n'+ 'No. of Upper case chars: '+str(d['UPPER_CASE'])+\
          '\n'+'No. of Lower case chars: '+str(d['LOWER_CASE']))
#input string to string test
string_test('1Hardware Software Interface Lab')