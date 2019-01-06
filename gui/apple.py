'''
Created on 7 juil. 2018

@author: Fab
'''
import pygame
from .pos import Pos

class Apple:
    
    
    def __init__(self, res):
        self.res = res
        self.pos = Pos(0, 0, res.apple_size, res.display_width, res.display_height)
        self.move()
        
    def move(self):
        self.pos.randomize()
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.res.apple_size, self.res.apple_size)
        
    def get_pos(self):
        return self.rect
        
    def draw(self, display):
        pygame.draw.rect(display, self.res.red, self.rect)
        