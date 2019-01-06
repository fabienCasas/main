'''
Created on 7 juil. 2018

@author: Fab
'''
import pygame
from .pos import Pos
from .resources import Event

class Snake:
    
    def __init__(self, res):
        self.res = res
        self.dir = Event.KEY_UP
        self.head = Pos(0,0,res.snake_girth, res.display_width, res.display_height)
        self.head.randomize()
        self.tail = []
        self.do_increase = False
    
    def increase(self):
        self.do_increase = True
        
    
    def draw(self, display):
        # head
        display.blit( self.res.head[self.dir] , (self.head.x, self.head.y))
        # tail
        for el in self.tail:
            pygame.draw.rect(display, self.res.snake_color, [ el.x,el.y, self.res.snake_girth, self.res.snake_girth])     
        
    def move(self, direction):
        # forbid U-turn
        if self.dir + direction :
            self.dir = direction
        old_head_x = self.head.x
        old_head_y = self.head.y
        self.head.move(self.dir)
        
        collision = False
        if self.head.out_of_bounds :
            collision = True
        if len(self.tail) :
            for el in self.tail :
                if self.head.x == el.x and self.head.y == el.y :
                    collision = True         
        # tail
        if len(self.tail) :
            last_x = self.tail[-1].x
            last_y = self.tail[-1].y
            for i in reversed(range (1, len(self.tail))):
                self.tail[i].x = self.tail[i-1].x            
                self.tail[i].y = self.tail[i-1].y
            self.tail[0].x = old_head_x
            self.tail[0].y = old_head_y
        else:
            last_x = old_head_x
            last_y = old_head_y
        if self.do_increase :
            new = Pos(last_x, last_y, self.res.snake_girth, self.res.display_width, self.res.display_height)
            self.tail.append(new)
            self.do_increase = False     
        
        return collision
    
    def get_pos(self):
        h = pygame.Rect(self.head.x, self.head.y, self.res.snake_girth, self.res.snake_girth)
        rect_list = [h]
        for el in self.tail :
            rect_list.append(pygame.Rect(el.x, el.y, self.res.snake_girth, self.res.snake_girth))
