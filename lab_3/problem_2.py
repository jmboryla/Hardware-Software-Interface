# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:05:16 2019

@author: jmbor
"""
#Importing numpy library for creating a matrix
import numpy as np

    
    '''The build_2d function builds a two dimensional array of size NxN, and uses 
    the fill function to fill the designated rows and columns that are the outside
    of the array'''
    
def build_2d():
    
    N = int(input('Please input the shape N: '))
    if N < 3:
        print('N must be larger than 2')
    elif N >= 3:
        mat=np.zeros([N,N],dtype=int)
        mat[0].fill(1)
        mat[N-1].fill(1)
        mat[:,0].fill(1)
        mat[:,N-1].fill(1)
        print(mat)
        return mat

ori_array=build_2d()

'''The set_diagonal function fills the two diagonals of the array with 1's
by use of the of the fill diagonal function as well as the fliplr function
to flip the matrix to fill the other diagonal'''
    
def set_diagonal(ori_array):
    
    np.fill_diagonal(ori_array,1)
    ori_array=np.fliplr(ori_array)
    np.fill_diagonal(ori_array,1)
    print(ori_array)
    return ori_array
ori_array = set_diagonal(ori_array)

'''The cal_zeros function calculates the zeros in an array by use of the count_nonzeros
but instead of looking for non-zero elements, the function parameter tells the function to
look for the zeros'''

def cal_zeros(ori_array):
    count =  np.count_nonzero(ori_array == 0)
    print(count)
    return count
cal_zeros(ori_array)