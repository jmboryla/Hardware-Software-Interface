# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:31:38 2019

@author: jmbor
"""

'''The class Rectangle defines an object as a reactangle, the rectangle_perimeter
function returns the area of the rectangle, and the rectangle_area function returns
the area of the rectangle'''

class Rectangle():
    def __init__(self,height,width):
        self.h = height
        self.w = width
    
    def rectangle_perimeter(self):
        self.perimeter = (self.h + self.w)*2
        return self.perimeter
    
    def rectangle_area(self):
        self.area = self.h * self.w
        return self.area

Rectangle_1 = Rectangle(12,10)
print(Rectangle_1.rectangle_perimeter())

'''The class Circle defines an object as a circle, the circle_area function returns
the area of that circle, and the perimeter function returns the perimeter of the defined
circle'''
      
class Circle():
    def __init__(self,radius):
        self.r = radius
        
    def area(self):
        self.area = self.r*self.r*3.14
        return self.area
    def perimeter(self):
        self.perimeter = 2 * self.r * 3.14
        return self.perimeter
Circle_1 = Circle(8)
print(Circle_1.perimeter())
