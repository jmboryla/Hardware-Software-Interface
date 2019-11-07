# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:28:23 2019

@author: jmbor
"""

#Open all files for reading an writing
a = open('1.txt','r')
b = open('2.txt','r')
c = open('3.txt','w')

#Read in lines of file '1.txt' and '2.txt' and store them in a list of lines
a_lines = a.readlines()
b_lines = b.readlines()

#Initialize lists for storing different values 
seen_master = []
sorted_a = []

#For loops to break apart each line and remove the new line character
for line in a_lines:
    new_word=[]
    words = line.split(', ')
    for word in words:
        word = word.replace('\n','')
        new_word.append(word)
    sorted_a.append(new_word)

#For loops to format lines of objects to append and remove duplicates from list
for line in b_lines:
    seen=[]
    words = line.split(', ')
    for word in words:
        word=word.replace('\n','')
        if word not in seen:
           seen.append(word)
        else:
            pass
    seen_master.append(seen)

#Zip together the file path and objects lists
zipped = zip(sorted_a,seen_master)

#For loop combines items in zip and writes to file
for file, name in zipped:
    c.write(file[0] + ' ' + ', '.join(name[:]) + '\n')