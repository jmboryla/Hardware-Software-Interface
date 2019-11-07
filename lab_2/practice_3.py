# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:05:53 2019

@author: borylaj
"""

color_dict ={'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}

def sort_dict(dic):
    colors = sorted(dic)
    dict_update= {}
    for color in colors:
        temp = {color:color_dict[color]}
        dict_update.update(temp)
    dic = {}
    dic.update(dict_update)
    return dic
print(sort_dict(color_dict))