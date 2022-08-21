# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 11:28:46 2022

@author: Dalciana
"""

class Rectangle:
    shape = "Rectangle"
    
    #Constructor initialization 
    def __init__(self,w, h):
        self.width= w
        self.height= h
        # if self.width != self.height:
        #     self.shape = "Rectangle"
        # else: 
        #     self.shape = "Square"
            
    #Height and width setting methods
    def set_width(self,w):
        self.width = w
    
    def set_height(self,h):
        self.height = h
    
    #Calculations method
    def get_area(self):
        return (self.width * self.height )
        
    def get_perimeter(self):
        return  (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return  ( ((self.height ** 2) + (self.width ** 2)) ** 0.5 )
    
    
    #Get picture method
    def get_picture(self):
        """
        Returns a string that represents the shape using lines of "*".
        The number of lines should be equal to the height 
        and the number of "*" in each line should be equal to the width.
        There should be a new line (\n) at the end of each line.
        If the width or height is larger than 50, 
        this should return the string: "Too big for picture.".
        """
        if self.width>50 or self.height>50:
            return ("Too big for picture.")
        else:
            display=""
            for x in range (self.height):
                display = display + "*" *self.width + '\n'
            
            return display
            
            
    def get_amount_inside(self, cat_shape):
        """ Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit inside
        the shape (with no rotations).
        For instance, a rectangle with a width of 4 
        and a height of 8 could fit in two squares with sides of 4.
        """
        cat_shape.width
        int_width = self.width //cat_shape.width
        int_height = self.height //cat_shape.height
        n_shapes = int_width*int_height
        return n_shapes 
    
    
    def __str__(self):
        """
        Additionally, if an instance of a Rectangle 
        is represented as a string,it should look like: 
            Rectangle(width=5, height=10)
        """
        
        return (self.shape + 
                "(width=" + str(self.width)  +
                ", height=" + str(self.height) + ")" )
    
    
class Square(Rectangle):
    shape = "Square"
    
    #Constructor initialization 
    def __init__(self, s):
      self.width = s
      self.height = s
    
    #Set side method
    def set_side(self, s):
      self.width = s
      self.height = s 
    
    #Set height method
    def set_height(self, h):
      self.height = h
      self.width = h
    
    #Set width method
    def set_width(self, w):
      self.width = w
      self.height = w
    
    #Return value
    def __str__(self):
        display =  (self.shape + 
        "(side=" + str(self.width)  + ")"
        )
        return display
