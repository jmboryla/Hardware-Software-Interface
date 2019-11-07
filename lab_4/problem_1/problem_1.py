# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:27:41 2019

@author: jmbor
"""
#Import json library
import json

#Define json_practice function for storing data to json file
def json_practice():
    #Initialize dictionary for output to json file
    final={}
    
    #Define boolean variable to control loop
    done = False
    
    #While loop using doine varibale to control times run
    while done == False:
        
        #Get user input and save it in variable user_input
        user_input=input('Enter data or type "done" to save all\n')
        
        #If user input is not equal to the string 'done' continue to save input to json file
        if user_input.upper()!='DONE':
            
            #Append brackets to beginning and end of user_input to save entry as a dictionary
            final.update(json.loads('{' + user_input + '}'))
        
        #If user enters done enter else loop
        else:               
            
            #Changes done boolean variable to 'True' to exit from while loop
            done = True  
    
    #When user is done inputting information all inputted info is dumped to the dictionary 'final'
    with open('data.json', 'w') as f:        
        json.dump(final, f)
        
    #the 'final' dictionary is then loaded to the output json file named 'data.json' and printed ot console
    with open ('data.json' , 'r') as f:
        data = json.load(f)
        print(data)

json_practice()