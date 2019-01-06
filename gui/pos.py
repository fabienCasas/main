'''
Created on 7 juil. 2018

@author: Fab
'''
import random
from .resources import Event

class Pos :
    
    def __init__(self, x, y, step, max_width, max_height):
        self.x = x
        self.y = y
        self.step = step
        self.max_width = max_width
        self.max_height = max_height
        self.out_of_bounds = False
        
    def randomize(self):
        self.x = round(random.randrange(0, self.max_width -self.step))
        self.y = round(random.randrange(0, self.max_height -self.step))
                        
    def move (self, direction):
        if not self.out_of_bounds :
            if direction == Event.KEY_UP :
                self.y = self.y - self.step
                if self.y < 0 : 
                    self.out_of_bounds = True  
                   
            if direction == Event.KEY_DOWN :
                self.y = self.y + self.step
                if self.y > self.max_height : 
                    self.out_of_bounds = True 
                   
            if direction == Event.KEY_LEFT :
                self.x = self.x - self.step
                if self.x < 0 : 
                    self.out_of_bounds = True 
                   
            if direction == Event.KEY_RIGHT :
                self.x = self.x + self.step
                if self.x > self.max_width : 
                    self.out_of_bounds = True
                
    def in_area (self, rect):
        is_in = False
        if (self.x >= rect.left and self.x <= rect.left + rect.width) or (self.x + self.step >= rect.left and self.x + self.step <= rect.left + rect.width):
            if (self.y >= rect.top and self.y <= rect.top + rect.height) or (self.y + self.step >= rect.top and self.y + self.step <= rect.top + rect.height) :
                is_in = True
        return is_in