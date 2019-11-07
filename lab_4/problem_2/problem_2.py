# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:04:25 2019

@author: jmbor
"""

import pandas as pd
from pandas import DataFrame

#Import each excel file useing pandas to a seperate variable
data1 = pd.read_excel('employee.xlsx',sheet_name = 'Sheet1')
data2 = pd.read_excel('employee.xlsx',sheet_name = 'Sheet2')
data3 = pd.read_excel('employee.xlsx',sheet_name = 'Sheet3')
data4 = pd.read_excel('combine.xlsx' ,sheet_name = 'Sheet1')

#Part One
def after_hire_date(data,after_date):

    print(data[data['hire_date']>after_date])
        
#Part Two
def sort_data(data,sort_index):
    data = data.sort_values(by = sort_index)
    return data
    
#Part Three
def between_hire_date(data,after_date,before_date):
    
     data = data[data['hire_date'] < before_date]
     print(data[data['hire_date'] > after_date])


#Part Four
def new_index(data,new_sort_index):
    data = data.sort_values(by = new_sort_index)
    data = data.set_index(new_sort_index)
    return data

#Part Five
def concatenate_data(output_file,*data_files):
    output_file = pd.DataFrame()
    for file in data_files:
        output_file = output_file.append(file)
    output_file = output_file.reset_index()
    return output_file

data4 = concatenate_data(data4,data1,data2,data3)
data4.to_excel('combine.xlsx', sheet_name='Sheet1')