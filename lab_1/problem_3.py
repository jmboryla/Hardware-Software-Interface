# -*- coding: utf-8 -*-
"""
Problem 3: Draw a Game Board
@author: Jonathan Boryla
"""


#Define a function to draw a gamebaord
def drawboard():
    #Get user input for size of gameboard
    size = input("What size do you want to draw?")
    #convert size to integer
    size = int(size)
    #define strings to draw game board vertical and horizontal boundaries
    stringA=['---']
    stringB=['|']
    #loops to drow different sections of gameboard
    for i in range(size+1):
        stringB.append('|')
    for i in range(size):
        stringA.append('---')
    #Joining drawings for borders with appropriate spaces
    stringA='   '.join(stringA)
    stringB='     '.join(stringB)
    #loop to print out game board
    for i in range(size):
        print('  '+str(stringA)+'\n'+str(stringB)+'\n')
    print('  '+str(stringA))
#Call function and print board
drawboard()
